from . import utilitySpace
from . import bid
# import utilitySpace
# import bid


class SummrizationOfUtilitySpace:
    '''
    utilitySpaceを統括する
    '''
    def __init__(self, file_name_list: [str]):
        '''
        :param List[str] file_name_list: 自動交渉に用いるファイルのパスのリスト
        '''
        self.__utility_num = len(file_name_list)
        self.__utility_space_list = []
        for i, file_name in enumerate(file_name_list):
            self.__utility_space_list.append(utilitySpace.UtilitySpace(file_name))

    def __print_all(self):
        for utility_space in self.__utility_space_list:
            utility_space.print_all()

    def is_valid_bid(self, bid_: bid.Bid) -> bool:
        '''
        Bidに正しい値が格納されているか調べる．

        :param bid_ Bid: Bidが正しい値が格納されているか調べる．
        :rtype: bool
        :return: Bidに正しい値が格納されているかどうか
        '''
        return self.__utility_space_list[0].is_valid_bid(bid_)

    def get_utility_space(self, index: int):
        '''
        指定したindexのAbstractUtilitySpaceを返す

        :param int index: 入手したいAbstractUtilitySpaceのインデックス
        :rtype: AbstractUtilitySpace
        :return: 効用ドメイン情報
        '''
        return self.__utility_space_list[index]

    def get_utility_num(self):
        '''
        効用ドメインファイルの数を返す

        :rtype: int
        :return: 効用ドメインファイルの数
        '''
        return self.__utility_num

    def get_weight_np_list(self):
        '''
        効用値情報のリストを返す

        :rtype: List[np.array]
        :return: 効用値情報のリスト
        '''
        weight_np_list = []
        for i in range(self.__utility_num):
            weight_np_list.append(self.__utility_space_list[i].get_weight_np_list())
        return weight_np_list

    def get_discount_factor_list(self):
        '''
        割引効用のリストを返す

        :rtype: List[float]
        :return: 割引効用のリスト
        '''
        discount_list = []
        for utility in self.__utility_space_list:
            discount_list.append(utility.get_discount_factor())
        return discount_list

    def get_reservation_value_list(self):
        '''
        留保価格のリストを返す

        :rtype: List[float]
        :return: 留保価格のリスト
        '''
        reservation_value_list = []
        for utility in self.__utility_space_list:
            reservation_value_list.append(utility.get_reservation_value())
        return reservation_value_list

# if __name__ == '__main__':
#     #utilities = SummrizationOfUtilitySpace('Domain2/Domain2_util1.xml',
#     #                                        'Domain2/Domain2_util2.xml')
#     utilities = SummrizationOfUtilitySpace('Jobs/Jobs_util1.xml',
#                                             'Jobs/Jobs_util2.xml')
