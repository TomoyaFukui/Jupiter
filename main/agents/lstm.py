import numpy as np
import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import json



def loss(y, t):
    cross_entropy = \
        tf.reduce_mean(-tf.reduce_sum(
                       t * tf.log(tf.clip_by_value(y, 1e-10, 1.0)),
                       reduction_indices=[1]))
    return cross_entropy


def training(loss):
    optimizer = tf.train.AdamOptimizer(learning_rate=0.1,
                                       beta1=0.9,
                                       beta2=0.999)
    train_step = optimizer.minimize(loss)
    return train_step

def accuracy(y, t):
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return accuracy


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
    '''
    データの生成
    '''
    f = open("bids.json", 'r')
    json_data = json.load(f) #JSON形式で読み込む
    X = json_data["in"]
    Y = json_data["out"]

    N_train = int(len(X) * 0.9)
    N_validation = len(X) - N_train

    X_train, X_test, Y_train, Y_test = \
        train_test_split(X, Y, train_size=N_train)

    X_train, X_validation, Y_train, Y_validation = \
        train_test_split(X_train, Y_train, test_size=N_validation)

    #print(X_train[0])

    '''
    モデル設定
    '''
    #n_in = len(X[0])
    #n_in = [3, 3]
    #n_hiddens = [3, 1]  # 各隠れ層の次元数
    #n_out = len(Y[0])
    #n_out = 3

    np.random.seed(0)
    tf.set_random_seed(1234)

    x = tf.placeholder(tf.float32, shape=[None, 3])
    t = tf.placeholder(tf.float32, shape=[None, 2])

    #y = inference(x, n_in=n_in, n_hiddens=n_hiddens, n_out=n_out)
    w = tf.Variable(tf.zeros([3, 2]))
    b = tf.Variable(tf.zeros([2]))
    y = tf.nn.sigmoid(tf.matmul(x, w) + b)
    loss = loss(y, t)
    train_step = training(loss)

    accuracy = accuracy(y, t)
    early_stopping = EarlyStopping(patience=10, verbose=1)

    history = {
        'val_loss': [],
        'val_acc': []
    }

    '''
    モデル学習
    '''
    epochs = 10
    batch_size = 1

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    n_batches = N_train // batch_size

    for epoch in range(epochs):
        X_, Y_ = shuffle(X_train, Y_train)

        #for i in range(n_batches):
        #    start = i * batch_size
        #    end = start + batch_size
        #    sess.run(train_step, feed_dict={
        #        x: X_[start:end],
        #        t: Y_[start:end]
        #    })
        sess.run(train_step, feed_dict={
            x: X_,
            t: Y_
        })

        # 検証データを用いた評価
        val_loss = loss.eval(session=sess, feed_dict={
            x: X_validation,
            t: Y_validation
        })
        val_acc = accuracy.eval(session=sess, feed_dict={
            x: X_validation,
            t: Y_validation
        })

        # 検証データに対する学習の進み具合を記録
        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)

        print('epoch:', epoch,
              ' validation loss:', val_loss,
              ' validation accuracy:', val_acc)

        # Early Stopping チェック
        if early_stopping.validate(val_loss):
            break

    '''
    学習の進み具合を可視化
    '''
    plt.rc('font', family='serif')
    fig = plt.figure()
    plt.plot(range(len(history['val_loss'])), history['val_loss'],
             label='loss', color='black')
    plt.xlabel('epochs')
    plt.show()

    '''
    予測精度の評価
    '''
    accuracy_rate = accuracy.eval(session=sess, feed_dict={
        x: X_test,
        t: Y_test
    })
    print('accuracy: ', accuracy_rate)
