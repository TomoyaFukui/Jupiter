# coding:utf-8
import random
import sys
import numpy as np
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from collections import deque
from keras import backend as K
import tensorflow as tf
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import abstractAgent
import agentAction
import abstractUtilitySpace
import negotiationRule
import itertools
import bid


class ImprovementAgent(abstractAgent.AbstractAgent):
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num:int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__random = random
        self.__random.seed(0)
        self.__issue_size_list = self.__utility_space.get_issue_size_list()
        self.__is_first_turn = True
        self.__opponent_action = None
        self.__opponent_bid = None
        self.init_dqn()

    def init_dqn(self):
        self.DQN_MODE = 1    # 1がDQN、0がDDQNです
        # LENDER_MODE = 1 # 0は学習後も描画なし、1は学習終了後に描画する

        # env = gym.make('CartPole-v0')
        self.num_episodes = 100  # 総試行回数
        self.max_number_of_steps = 10  # 1試行のstep数
        self.goal_average_reward = 0.52  # この報酬を超えると学習終了
        self.num_consecutive_iterations = 10  # 学習完了評価をするために，用いるデータの数．平均計算を行う母数，試行回数
        self.total_reward_vec = np.zeros(num_consecutive_iterations)  # 各試行の報酬を格納
        self.gamma = 0.99    # 割引係数
        # islearned = 0  # 学習が終わったフラグ
        # isrender = 0  # 描画フラグ
        # ---
        self.hidden_size = 16               # Q-networkの隠れ層のニューロンの数
        self.learning_rate = 0.00001         # Q-networkの学習係数
        self.memory_size = 10000            # バッファーメモリの大きさ
        self.batch_size = 32                # Q-networkを更新するバッチの大記載

        # [5.2]Qネットワークとメモリ、Actorの生成--------------------------------------------------------
        self.mainQN = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)     # メインのQネットワーク
        self.targetQN = QNetwork(hidden_size=hidden_size, learning_rate=learning_rate)   # 価値を計算するQネットワーク
        # plot_model(mainQN.model, to_file='Qnetwork.png', show_shapes=True)        # Qネットワークの可視化
        self.memory = Memory(max_size=memory_size)
        self.actor = Actor()
        self.init_state()

    def init_state(self):
        self.is_initial_state = True
        self.state = [0, 1, 0, 0] #最大，最小，分散，平均時刻，(ドメインの大きさ)

    def get_state(self, time):
        if self.is_initial_state:
            self.is_initial_state = False

        pass

    # def define_searching_range(self):
    #     self.y = [x*0.1 for x in range(0, 11)].reverse()

    def make_parameters(self, point_num:int):
        #y = [x*0.1 for x in range(0, 11)].reverse()
        y = (x*0.1 for x in range(0, 11))
        y = list(itertools.permutations(y, 2))
        y = [[y1, y2] for y1, y2 in y if y1 >= y2 and y1 - y2 >= 0.35] #3だと端数でうまくいかない．端数のために3.5
        y.reverse()
        #param_list
        print(y)

    def get_conssetion_value(self):

    def get_action(self):
        # return (1.0 - self.__rule.get_time_now())
        # [5.3]メインルーチン--------------------------------------------------------
        # for episode in range(num_episodes):  # 試行数分繰り返す
        env.reset()  # cartPoleの環境初期化
        state, reward, done, _ = env.step(env.action_space.sample())  # 1step目は適当な行動をとる
        state = np.reshape(state, [1, 4])   # list型のstateを、1行4列の行列に変換
        episode_reward = 0

        targetQN = mainQN   # 行動決定と価値計算のQネットワークをおなじにする

        for t in range(max_number_of_steps + 1):  # 1試行のループ
            if (islearned == 1) and LENDER_MODE:  # 学習終了したらcartPoleを描画する
                env.render()
                time.sleep(0.1)
                print(state[0, 0])  # カートのx位置を出力するならコメントはずす

            action = actor.get_action(state, episode, mainQN)   # 時刻tでの行動を決定する
            next_state, reward, done, info = env.step(action)   # 行動a_tの実行による、s_{t+1}, _R{t}を計算する
            next_state = np.reshape(next_state, [1, 4])     # list型のstateを、1行4列の行列に変換

            # 報酬を設定し、与える
            if done:
                next_state = np.zeros(state.shape)  # 次の状態s_{t+1}はない
                if t < 195:
                    reward = -1  # 報酬クリッピング、報酬は1, 0, -1に固定
                else:
                    reward = 1  # 立ったまま195step超えて終了時は報酬
            else:
                reward = 0  # 各ステップで立ってたら報酬追加（はじめからrewardに1が入っているが、明示的に表す）

            episode_reward += 1 # reward  # 合計報酬を更新

            memory.add((state, action, reward, next_state))     # メモリの更新する
            state = next_state  # 状態更新


            # Qネットワークの重みを学習・更新する replay
            if (memory.len() > batch_size) and not islearned:
                mainQN.replay(memory, batch_size, gamma, targetQN)

            if DQN_MODE:
                targetQN = mainQN  # 行動決定と価値計算のQネットワークをおなじにする

            # 1施行終了時の処理
            if done:
                total_reward_vec = np.hstack((total_reward_vec[1:], episode_reward))  # 報酬を記録
                print('%d Episode finished after %f time steps / mean %f' % (episode, t + 1, total_reward_vec.mean()))
                break

        # 複数施行の平均報酬で終了を判断
        if total_reward_vec.mean() >= goal_average_reward:
            print('Episode %d train agent successfuly!' % episode)
            islearned = 1
            if isrender == 0:   # 学習済みフラグを更新
                isrender = 1

                # env = wrappers.Monitor(env, './movie/cartpoleDDQN')  # 動画保存する場合
                # 10エピソードだけでどんな挙動になるのか見たかったら、以下のコメントを外す
                # if episode>10:
                #    if isrender == 0:
                #        env = wrappers.Monitor(env, './movie/cartpole-experiment-1') #動画保存する場合
                #        isrender = 1
                #    islearned=1;

    def receiveAction(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__is_first_turn = False
            self.__opponent_action = agentAction_
            self.__opponent_bid = agentAction_.get_bid()

    def sendAction(self):
        if self.__opponent_action is not None and \
            self.get_conssetion_value() < self.__utility_space.get_utility(self.__opponent_bid) \
                and self.__is_first_turn == False:
            #self.get_conssetion_value() < self.__utility_space.get_utility_discounted(self.__opponent_bid, self.__opponent_action.get_time_offered()) \
            return agentAction.Accept(self.__agent_id)

        bid_offer = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        #while self.__utility_space.get_utility_discounted(bid_offer, self.__rule.get_time_now()) < self.get_conssetion_value():
        while self.__utility_space.get_utility(bid_offer) < self.get_conssetion_value():
            for i, size in enumerate(self.__issue_size_list):
                bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        print("start improve")
        self.init_state()

    def receive_end_negotiation(self):
        print("end improve")

    def get_name(self):
        return 'ImprovementAgent'




# [2]Q関数をディープラーニングのネットワークをクラスとして定義
class QNetwork:
    def __init__(self, learning_rate=0.01, state_size=4, action_size=45, hidden_size=10):
        # 損失関数の定義
        # 損失関数にhuber関数を使用します 参考https://github.com/jaara/AI-blog/blob/master/CartPole-DQN.py
        def huberloss(y_true, y_pred):
            err = y_true - y_pred
            cond = K.abs(err) < 1.0
            L2 = 0.5 * K.square(err)
            L1 = (K.abs(err) - 0.5)
            loss = tf.where(cond, L2, L1)  # Keras does not cover where function in tensorflow :-(
            return K.mean(loss)
        self.model = Sequential()
        self.model.add(Dense(hidden_size, activation='relu', input_dim=state_size))
        self.model.add(Dense(hidden_size, activation='relu'))
        self.model.add(Dense(action_size, activation='linear'))
        self.optimizer = Adam(lr=learning_rate)  # 誤差を減らす学習方法はAdam
        # self.model.compile(loss='mse', optimizer=self.optimizer)
        self.model.compile(loss=huberloss, optimizer=self.optimizer)

    # 重みの学習
    def replay(self, memory, batch_size, gamma, targetQN):
        inputs = np.zeros((batch_size, 4))
        targets = np.zeros((batch_size, 45))
        mini_batch = memory.sample(batch_size)

        for i, (state_b, action_b, reward_b, next_state_b) in enumerate(mini_batch):
            inputs[i:i + 1] = state_b
            target = reward_b

            if not (next_state_b == np.zeros(state_b.shape)).all(axis=1):
                # 価値計算（DDQNにも対応できるように、行動決定のQネットワークと価値観数のQネットワークは分離）
                retmainQs = self.model.predict(next_state_b)[0]
                next_action = np.argmax(retmainQs)  # 最大の報酬を返す行動を選択する
                target = reward_b + gamma * targetQN.model.predict(next_state_b)[0][next_action]

            targets[i] = self.model.predict(state_b)    # Qネットワークの出力
            targets[i][action_b] = target               # 教師信号
            self.model.fit(inputs, targets, epochs=1, verbose=0)  # epochsは訓練データの反復回数、verbose=0は表示なしの設定


# [3]Experience ReplayとFixed Target Q-Networkを実現するメモリクラス
class Memory:
    def __init__(self, max_size=1000):
        self.buffer = deque(maxlen=max_size)

    def add(self, experience):
        self.buffer.append(experience)

    # self.bufferリストからランダムにバッチサイズの数だけ要素を抽出
    def sample(self, batch_size):
        idx = np.random.choice(np.arange(len(self.buffer)), size=batch_size, replace=False)
        return [self.buffer[ii] for ii in idx]

    def len(self):
        return len(self.buffer)


# [4]カートの状態に応じて、行動を決定するクラス
class Actor:
    def get_action(self, state, episode, targetQN):   # [C]ｔ＋１での行動を返す
        # 徐々に最適行動のみをとる、ε-greedy法
        epsilon = 0.001 + 0.9 / (1.0+episode)

        if epsilon <= np.random.uniform(0, 1):
            retTargetQs = targetQN.model.predict(state)[0]
            action = np.argmax(retTargetQs)  # 最大の報酬を返す行動を選択する

        else:
            action = np.random.choice([0, 1])  # ランダムに行動する

        return action
