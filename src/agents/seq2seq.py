import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import json
import copy
import itertools
import os
LOG_DIR = os.path.join(os.path.dirname(__file__), 'log')
if os.path.exists(LOG_DIR) is False:
    os.mkdir(LOG_DIR)
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
if os.path.exists(MODEL_DIR) is False:
    os.mkdir(MODEL_DIR)



class SEQ2SEQ():
    def __init__(self):
        np.random.seed(0)
        tf.set_random_seed(1234)
        np.set_printoptions(formatter={'float': '{: 0.3f}'.format}) #桁を揃える
        pass

    def init_model(self, encoder, bid, decoder):
        #self.length_of_encoder = 30
        #self.length_of_bid = 6
        #self.length_of_bid = 18
        #self.length_of_decoder = 2
        self.length_of_encoder = encoder
        self.length_of_bid = bid
        self.length_of_decoder = decoder
        #self.length_of_decoder = 6

    '''
    データの生成
    '''
    def create_data(self, encoder):
        file_json = open("bids1.json", 'r')
        json_data = json.load(file_json) #JSON形式で読み込む
        f = json_data["data"]
        f = [i[3:] for i in f]
        self.length_of_data = len(f)
        self.length_of_encoder = encoder
        self.length_of_bid = len(f[0])
        self.length_of_decoder = sum(f[0])

        data = []
        target = []
        for i in range(0, self.length_of_data - self.length_of_encoder):
            data.append(f[i: i + self.length_of_encoder])

            target.append([])
            target_store = [0] * self.length_of_bid
            for j, f_j in enumerate(f[i + self.length_of_encoder]):
                target_store[j] = f_j
                if f_j == 1:
                    target[i].append(copy.deepcopy(target_store))
                    target_store = [0] * self.length_of_bid

        self.X = np.array(data).reshape(len(data), self.length_of_encoder, self.length_of_bid) #len(f[0])
        self.Y = np.array(target).reshape(len(data), self.length_of_decoder, self.length_of_bid) #len(f[0])

        ## データ設定
        self.N_train = int(len(data) * 0.9)
        self.N_validation = len(data) - self.N_train
        self.X_train, self.X_validation, self.Y_train, self.Y_validation = \
            train_test_split(self.X, self.Y, test_size=self.N_validation)

    '''
    モデル設定
    '''
    def create_model(self):
        def loss(y, t):
            cross_entropy = \
                tf.reduce_mean(-tf.reduce_sum(
                               t * tf.log(tf.clip_by_value(y, 1e-10, 1.0)),
                               reduction_indices=[1]))
            return cross_entropy

        def training(loss):
            optimizer = \
                tf.train.AdamOptimizer(learning_rate=0.001, beta1=0.9, beta2=0.999)
            train_step = optimizer.minimize(loss)
            return train_step

        def accuracy(y, t):
            correct_prediction = tf.equal(tf.argmax(y, -1), tf.argmax(t, -1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            return accuracy

        def inference(x, y, n_batch, is_training,
                      input_digits=None, output_digits=None,
                      n_hidden=None, n_out=None):
            def weight_variable(shape, name):
                initial = tf.truncated_normal(shape, stddev=0.01)
                return tf.Variable(initial, name=name)

            def bias_variable(shape, name):
                initial = tf.zeros(shape, dtype=tf.float32)
                return tf.Variable(initial, name=name)

            # Encoder
            encoder = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)
            state = encoder.zero_state(n_batch, tf.float32)
            encoder_outputs = []
            encoder_states = []

            with tf.variable_scope('Encoder'):
                for t in range(input_digits):
                    if t > 0:
                        tf.get_variable_scope().reuse_variables()
                    (output, state) = encoder(x[:, t, :], state)
                    encoder_outputs.append(output)
                    encoder_states.append(state)

            # Decoder
            decoder = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)
            state = encoder_states[-1]
            decoder_outputs = [encoder_outputs[-1]]

            # 出力層の重みとバイアスを事前に定義
            V = weight_variable([n_hidden, n_out], 'decoder_w')
            c = bias_variable([n_out], 'decoder_b')
            outputs = []

            with tf.variable_scope('Decoder'):
                for t in range(1, output_digits):
                    if t > 1:
                        tf.get_variable_scope().reuse_variables()

                    if is_training is True:
                        (output, state) = decoder(y[:, t-1, :], state)
                    else:
                        # 直前の出力を入力に用いる
                        linear = tf.matmul(decoder_outputs[-1], V) + c
                        out = tf.nn.softmax(linear)
                        outputs.append(out)
                        out = tf.one_hot(tf.argmax(out, -1), depth=output_digits)
                        (output, state) = decoder(out, state)

                    decoder_outputs.append(output)

            if is_training is True:
                output = tf.reshape(tf.concat(decoder_outputs, axis=1),
                                    [-1, output_digits, n_hidden])

                linear = tf.einsum('ijk,kl->ijl', output, V) + c
                # linear = tf.matmul(output, V) + c
                return tf.nn.softmax(linear)
            else:
                # 最後の出力を求める
                linear = tf.matmul(decoder_outputs[-1], V) + c
                out = tf.nn.softmax(linear)
                outputs.append(out)

                output = tf.reshape(tf.concat(outputs, axis=1),
                                    [-1, output_digits, n_out])
                return output

        n_in = self.length_of_bid
        #n_hidden = 128
        n_hidden = 64
        n_out = self.length_of_bid

        self.x = tf.placeholder(tf.float32, shape=[None, self.length_of_encoder, n_in])
        self.t = tf.placeholder(tf.float32, shape=[None, self.length_of_decoder, n_out])
        self.n_batch = tf.placeholder(tf.int32, shape=[])
        self.is_training = tf.placeholder(tf.bool)

        self.y = inference(self.x, self.t, self.n_batch, self.is_training,
                      input_digits=self.length_of_encoder,
                      output_digits=self.length_of_decoder,
                      n_hidden=n_hidden, n_out=n_out)
        self.loss = loss(self.y, self.t)
        self.train_step = training(self.loss)

        self.acc = accuracy(self.y, self.t)

        self.history = {
            'val_loss': [],
            'val_acc': []
        }

    '''
    モデル学習
    '''
    def traning(self):
        epochs = 100
        batch_size = 20
        early_stopping = EarlyStopping(patience=1, verbose=True)

        init = tf.global_variables_initializer()
        saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(init)

        n_batches = self.N_train // batch_size


        for epoch in range(epochs):
            print('=' * 10)
            print('Epoch:', epoch)
            print('=' * 10)

            X_, Y_ = shuffle(self.X_train, self.Y_train)

            for i in range(n_batches):
                start = i * batch_size
                end = start + batch_size

                self.sess.run(self.train_step, feed_dict={
                    self.x: X_[start:end],
                    self.t: Y_[start:end],
                    self.n_batch: batch_size,
                    self.is_training: True
                })

            # 検証データを用いた評価
            val_loss = self.loss.eval(session=self.sess, feed_dict={
                self.x: self.X_validation,
                self.t: self.Y_validation,
                self.n_batch: self.N_validation,
                self.is_training: False
            })
            val_acc = self.acc.eval(session=self.sess, feed_dict={
                self.x: self.X_validation,
                self.t: self.Y_validation,
                self.n_batch: self.N_validation,
                self.is_training: False
            })

            self.history['val_loss'].append(val_loss)
            self.history['val_acc'].append(val_acc)
            print('validation loss:', val_loss)
            print('validation acc: ', val_acc)

            # 検証データからランダムに問題を選んで答え合わせ
            #for i in range(1):
            #    index = np.random.randint(0, self.N_validation)
            #    question = self.X_validation[np.array([index])]
            #    answer = self.Y_validation[np.array([index])]
            #    prediction = self.y.eval(session=self.sess, feed_dict={
            #        self.x: question,
            #        # t: answer,
            #        self.n_batch: 1,
            #        self.is_training: False
            #    })
            #    print('-' * 10)
            #    #print('Q:  ', question)
            #    print('Answ:  ', answer[0, 0].astype(np.float16), answer[0, 1].astype(np.float16))
            #    print('Pred:  ', prediction[0, 0], prediction[0, 1])
            #print('-' * 10)

            if early_stopping.validate(val_loss):
                break

        model_path = saver.save(self.sess, MODEL_DIR + '/model.ckpt')
        print('Model saved to:', model_path)

    def load(self):
        saver = tf.train.Saver()
        self.sess = tf.Session()
        saver.restore(self.sess, MODEL_DIR + '/model.ckpt')

    '''
    出力を用いて予測
    '''
    def predict(self, data:np.array, issue_size_list, predict_num=1000):
        Z = data
        predicted = []
        issue_size = len(issue_size_list)
        predicted_prob = data.reshape(self.length_of_encoder, self.length_of_bid)
        #Z = self.X[:1]
        #predicted = self.X[:1].reshape(self.length_of_encoder, self.length_of_bid)
        #predicted_prob = self.X[:1].reshape(self.length_of_encoder, self.length_of_bid)

        #for i in range(len(self.Y)):
        for i in range(predict_num):
            # 最後の時系列データから未来を予測
            z = Z[-1:]
            y_ = self.y.eval(session=self.sess, feed_dict={
                self.x: z,
                #self.t: answer,
                self.n_batch: 1,
                self.is_training: False
            })

            # 予測結果を用いて新しい時系列データを生成
            rand_list = np.random.rand(self.length_of_decoder)
            predict_ = np.zeros(self.length_of_bid)
            predict_bid = [0] * issue_size
            for j, (y, rand) in enumerate(zip(y_[0], rand_list)):
                prob_sum = 0
                for k, probability in enumerate(y):
                    prob_sum += probability
                    if prob_sum >= rand:
                        predict_[k] = 1
                        predict_bid[j] = k - sum(issue_size_list[:j])
                        break
            z = z.reshape(self.length_of_encoder, self.length_of_bid)[1:]
            sequence_ = np.concatenate((z, predict_.reshape(1, self.length_of_bid)), axis=0) \
                .reshape(1, self.length_of_encoder, self.length_of_bid)
            Z = np.append(Z, sequence_, axis=0)
            #predicted = np.concatenate((predicted, predict_.reshape(1, self.length_of_bid)), axis=0)
            predicted.append(copy.deepcopy(predict_bid))
            T = np.zeros(self.length_of_bid)
            for y in y_[0]:
                T += y
            predicted_prob = np.concatenate((predicted_prob, T.reshape(1, self.length_of_bid)), axis=0)
        #predicted = predicted[self.length_of_encoder:]
        predicted_prob = predicted_prob[self.length_of_encoder:]
        return predicted, predicted_prob

        '''
        予測の可視化
        '''
        #for i, predict in enumerate(predicted):
        #    print(i)
        #    #T = np.zeros(self.length_of_bid)
        #    #for y in self.Y[i]:
        #    #    T += y
        #    #print("  answ:", T.astype(np.float16))
        #    print("  pred:", predict)
        #    print("  prob:", predicted_prob[i])

        #predicted.pop()
        #for i, data, predict in zip(range(len(f)), f, predicted):
        #    if predict is not None:
        #        #print(i, ":", data, predict)
        #        print(i, ":")
        #        for d, p in zip(data, predict):
        #            print("\t", d, ",", p)
        #    else:
        #        print(i, ":", data)
        #for y, t in zip()
        #   print()
        #plt.rc('font', family='serif')
        #plt.figure()
        #plt.ylim([-1.5, 1.5])
        #plt.plot(toy_problem(T, ampl=0), linestyle='dotted', color='#aaaaaa')
        #plt.plot(original, linestyle='dashed', color='black')
        #plt.plot(predicted, color='black')
        #plt.show()

    def predict_all_possibility(self, data:np.array, issue_size_list):
        def create_all_bid(issue_size_list):
            issue_size = len(issue_size_list)
            index_set_list = []
            for i, size in enumerate(issue_size_list):
                index_set_list.append([j+sum(issue_size_list[:i]) for j in range(size)])
            answer_list = index_set_list[0]
            for i in range(1, issue_size):
                answer_list = list(itertools.product(answer_list, index_set_list[i]))
            ans_bid = [0] * sum(issue_size_list)
            ans_bid_list = [[copy.deepcopy(ans_bid) for j in range(issue_size) ] for i in range(np.prod(issue_size_list))]
            for answer, bid in zip(answer_list, ans_bid_list):
                index = -1
                bid[index][answer[1]] = 1
                ans_temp = answer[0]
                while isinstance(ans_temp, tuple):
                    index -= 1
                    bid[index][ans_temp[1]] = 1
                    ans_temp = ans_temp[0]
                bid[0][ans_temp] = 1
            return ans_bid_list

        Z = data.reshape(1, self.length_of_encoder, self.length_of_bid)
        answer_bid_list = create_all_bid(issue_size_list)
        #print(answer_bid_list)
        #predicted_prob = data.reshape(self.length_of_encoder, self.length_of_bid)

        #Z = self.X[:1]
        #predicted = self.X[:1].reshape(self.length_of_encoder, self.length_of_bid)
        #predicted_prob = self.X[:1].reshape(self.length_of_encoder, self.length_of_bid)

        #for i in range(len(self.Y)):
        result = []
        for answer in answer_bid_list:
            # 最後の時系列データから未来を予測
            #print(answer)
            ans = np.array(answer, np.int32).reshape(1, self.length_of_decoder, self.length_of_bid)
            y_ = self.y.eval(session=self.sess, feed_dict={
                self.x: Z,
                self.t: ans,
                self.n_batch: 1,
                self.is_training: True
            })
            result.append(y_)
        y_ = self.y.eval(session=self.sess, feed_dict={
            self.x: Z,
            #self.t: ans,
            self.n_batch: 1,
            self.is_training: False
        })



        for r in result:
            print(r[0][-1])
        print(y_[0][-1])




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

def create_data(encoder):
    file_json = open("bids1.json", 'r')
    json_data = json.load(file_json) #JSON形式で読み込む
    f = json_data["data"]
    f = [i[3:] for i in f]
    length_of_data = len(f)

    length_of_encoder = encoder
    length_of_bid = len(f[0])
    length_of_decoder = sum(f[0])
    print(length_of_bid)
    print(length_of_decoder)

    data = []
    for i in range(0, length_of_data - length_of_encoder):
        data.append(f[i: i + length_of_encoder])
    X = np.array(data).reshape(len(data), length_of_encoder, length_of_bid) #len(f[0])
    return X

if __name__ == '__main__':
    seq2seq = SEQ2SEQ()
    print("init model")
    seq2seq.init_model(30, 32, 7)
    print("create data")
    seq2seq.create_data(30)
    print("create model")
    seq2seq.create_model()
    #print("training")
    #seq2seq.traning()
    print("load model")
    seq2seq.load()
    print("predict negotiation")
    #print(create_data().shape) #(1, 30, 6)
    #seq2seq.predict(issue_size_list=[3, 3], data=create_data())
    #seq2seq.predict(issue_size_list=[3, 3], data=create_data()[0])
    #seq2seq.predict_all_possibility(issue_size_list=[3, 3], data=create_data()[-3])
    #seq2seq.predict_all_possibility(issue_size_list=[3, 3], data=[1,1])
    seq2seq.predict_all_possibility(issue_size_list=[5, 4, 4, 4, 4, 7, 4], data=create_data(30)[-3])
