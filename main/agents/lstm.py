import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import json

import os
LOG_DIR = os.path.join(os.path.dirname(__file__), 'log')
if os.path.exists(LOG_DIR) is False:
    os.mkdir(LOG_DIR)
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
if os.path.exists(MODEL_DIR) is False:
    os.mkdir(MODEL_DIR)

np.random.seed(0)
tf.set_random_seed(1234)

class LSTM():
    def __init__(self):
        self.stop = EarlyStopping()

    '''
    データの生成
    '''
    def create_data(self):
        file_json = open("bids.json", 'r')
        json_data = json.load(file_json) #JSON形式で読み込む
        f = json_data["data"]
        f = [i[:3] for i in f]
        #for f_in in f:
        #    f_in = [{1:True, 0:False}[i] for i in f_in]
        print(f)
        length_of_sequences = len(f)
        self.maxlen = 25

        data = []
        target = []
        for i in range(0, length_of_sequences - self.maxlen):
            data.append(f[i: i + self.maxlen])
            target.append(f[i + self.maxlen])

        X = np.array(data).reshape(len(data), self.maxlen, len(f[0])) #len(f[0])
        Y = np.array(target).reshape(len(data), len(f[0])) #len(f[0])

        # データ設定
        self.N_train = int(len(data) * 0.9)
        self.N_validation = len(data) - self.N_train

        self.X_train, self.X_validation, self.Y_train, self.Y_validation = \
            train_test_split(X, Y, test_size=self.N_validation)

        #N_train = int(len(X) * 0.9)
        #N_validation = len(X) - N_train

        #X_train, X_test, Y_train, Y_test = \
        #    train_test_split(X, Y, train_size=N_train)

        #X_train, X_validation, Y_train, Y_validation = \
        #    train_test_split(X_train, Y_train, test_size=N_validation)

    '''
    モデル設定
    '''
    def create_model(self):
        def inference(x, n_batch, maxlen=None, n_hidden=None, n_out=None):
            def weight_variable(shape, name):
                initial = tf.truncated_normal(shape, stddev=0.01)
                return tf.Variable(initial, name=name)

            def bias_variable(shape, name):
                initial = tf.zeros(shape, dtype=tf.float32)
                return tf.Variable(initial, name=name)

            cell = tf.contrib.rnn.LSTMCell(n_hidden, forget_bias=1.0)
            initial_state = cell.zero_state(n_batch, tf.float32)

            state = initial_state
            outputs = []  # 過去の隠れ層の出力を保存
            with tf.variable_scope('LSTM'):
                for t in range(maxlen):
                    if t > 0:
                        tf.get_variable_scope().reuse_variables()
                    (cell_output, state) = cell(x[:, t, :], state)
                    outputs.append(cell_output)

            output = outputs[-1]

            V = weight_variable([n_hidden, n_out], 'w')
            b = bias_variable([n_out], 'b')
            y = tf.matmul(output, V, name='y') + b  # 線形活性

            return y
        def loss(y, t):
            mse = tf.reduce_mean(tf.square(y - t))
            return mse
            #cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=t, logits=y))
            #return cross_entropy

        def training(loss):
            optimizer = \
                tf.train.AdamOptimizer(learning_rate=0.001, beta1=0.9, beta2=0.999)

            train_step = optimizer.minimize(loss)
            return train_step

        n_in = len(self.X_train[0][0])  # 9?
        n_hidden = 30
        n_out = len(self.Y_train[0])  # 9?

        self.x = tf.placeholder(tf.float32, shape=[None, self.maxlen, n_in], name='x')
        self.t = tf.placeholder(tf.float32, shape=[None, n_out], name='t')
        #self.x = tf.placeholder(tf.bool, shape=[None, self.maxlen, n_in], name='x')
        #self.t = tf.placeholder(tf.bool, shape=[None, n_out], name='t')
        self.n_batch = tf.placeholder(tf.int32, shape=[])

        self.y = inference(self.x, self.n_batch, maxlen=self.maxlen, n_hidden=n_hidden, n_out=n_out)
        self.loss = loss(self.y, self.t)
        self.train_step = training(self.loss)

        self.early_stopping = EarlyStopping(patience=10, verbose=1)
        self.history = {
            'val_loss': []
        }

    def model_load(self):
        saver = tf.train.Saver()
        self.sess = tf.Session()
        saver.restore(self.sess, MODEL_DIR + '/model.ckpt')

        #with tf.name_scope('loss'):
        #    # 検証データを用いた評価
        #    val_loss = self.loss.eval(session=sess, feed_dict={
        #        self.x: self.X_validation,
        #        self.t: self.Y_validation,
        #        self.n_batch: self.N_validation
        #    })
        #    print('validation loss:', val_loss)

    def predict(self):
        file_json = open("bids.json", 'r')
        json_data = json.load(file_json) #JSON形式で読み込む
        f = json_data["data"]
        f = [i[:3] for i in f]
        length_of_sequences = len(f)

        data = []
        target = []
        for i in range(0, length_of_sequences - self.maxlen):
            data.append(f[i: i + self.maxlen])
            target.append(f[i + self.maxlen])

        #X = np.array(data).reshape(len(data), self.maxlen, 1)
        #Y = np.array(target).reshape(len(data), 1)
        X = np.array(data).reshape(len(data), self.maxlen, len(f[0]))
        Y = np.array(target).reshape(len(data), len(f[0]))
        '''
        出力を用いて予測
        '''
        truncate = self.maxlen
        Z = X[:1]  # 元データの最初の一部だけ切り出し

        original = [f[i] for i in range(self.maxlen)]
        predicted = [None for i in range(self.maxlen)]

        for i in range(length_of_sequences - self.maxlen + 1):
            # 最後の時系列データから未来を予測
            z_ = Z[-1:]
            y_ = self.y.eval(session=self.sess, feed_dict={
                self.x: Z[-1:],
                self.n_batch: 1
            })
            # 予測結果を用いて新しい時系列データを生成
            sequence_ = np.concatenate((z_.reshape(self.maxlen, len(f[0]))[1:], y_), axis=0) \
                .reshape(1, self.maxlen,len(f[0]))
            #sequence_ = np.concatenate((z_.reshape(self.maxlen, 1)[1:], y_), axis=0) \
            #    .reshape(1, self.maxlen, 1)
            Z = np.append(Z, sequence_, axis=0)
            predicted.append(y_.reshape(-1))

        '''
        グラフで可視化
        '''
        predicted.pop()
        for i, data, predict in zip(range(len(f)), f, predicted):
            if predict is not None:
                print(i, ":", data, predict)
            else:
                print(i, ":", data)
        #print("f size:", len(f))
        #print("predicted size:",len(predicted))
        #print(predicted[201])
        #print(len(predicted), ":", len(original))
        #for y, t in zip()
        #   print()
        #plt.rc('font', family='serif')
        #plt.figure()
        #plt.ylim([-1.5, 1.5])
        #plt.plot(toy_problem(T, ampl=0), linestyle='dotted', color='#aaaaaa')
        #plt.plot(original, linestyle='dashed', color='black')
        #plt.plot(predicted, color='black')
        #plt.show()

    '''
    モデル学習
    '''
    def epoch_training(self):
        epochs = 100
        batch_size = 10

        init = tf.global_variables_initializer()
        saver = tf.train.Saver()
        sess = tf.Session()

        #file_writer = tf.summary.FileWriter(LOG_DIR, sess.graph)
        #summaries = tf.summary.merge_all()
        #tf.summary.FileWriter(LOG_DIR, sess.graph) # TensorBoard
        sess.run(init)
        n_batches = self.N_train // batch_size

        for epoch in range(epochs):
            X_, Y_ = shuffle(self.X_train, self.Y_train)
            with tf.name_scope('train'):
                for i in range(n_batches):
                    start = i * batch_size
                    end = start + batch_size
                    sess.run(self.train_step, feed_dict={
                        self.x: X_[start:end],
                        self.t: Y_[start:end],
                        self.n_batch: batch_size
                    })

            with tf.name_scope('loss'):
                # 検証データを用いた評価
                val_loss = self.loss.eval(session=sess, feed_dict={
                    self.x: self.X_validation,
                    self.t: self.Y_validation,
                    self.n_batch: self.N_validation
                })
                #tf.summary.scalar('reduce_mean', val_loss)
                self.history['val_loss'].append(val_loss)
                print('epoch:', epoch,
                      ' validation loss:', val_loss)

            # Early Stopping チェック
            if self.early_stopping.validate(val_loss):
                break
        model_path = saver.save(sess, MODEL_DIR + '/model.ckpt')
        print('Model saved to:', model_path)

class EarlyStopping():
    def __init__(self, patience=0, verbose=0):
        self._step = 0
        self._loss = float('inf')
        self.patience = patience
        self.verbose = verbose

    def validate(self, loss):
        if self._loss < loss:
            self._step += 1
            if self._step > self.patience:
                if self.verbose:
                    print('early stopping')
                return True
        else:
            self._step = 0
            self._loss = loss
        return False

if __name__ == '__main__':
    #file_json = open("bids.json", 'r')
    #json_data = json.load(file_json) #JSON形式で読み込む
    #f = json_data["data"]
    #f = [i[0] for i in f]
    #length_of_sequences = len(f)
    #self.maxlen = 25
#
    #data = []
    #target = []
    #for i in range(0, length_of_sequences - self.maxlen):
    #    data.append(f[i: i + self.maxlen])
    #    target.append(f[i + self.maxlen])
#
    #X = np.array(data).reshape(len(data), self.maxlen, 9)
    #Y = np.array(target).reshape(len(data), 9)

    lstm = LSTM()
    lstm.create_data()
    lstm.create_model()
    lstm.epoch_training()
    lstm.model_load()
    lstm.predict()
