cimport numpy as np

def get_bid_above_concession_value(list weight_list_list, list random_number_list, double concession_value):
    cdef size_t random_number_size = len(random_number_list[0])
    cdef size_t issue_size = len(weight_list_list)
    # cdef double bid_value = 0
    # cdef double bid_value_max = 0

    bid_index_list = [None] * issue_size
    bid_index_list_max = [None] * issue_size
    # bid_value = [0] * issue_size
    bid_value_list = [0] * issue_size

    for j in range(0, issue_size):
        bid_index_list[j] = random_number_list[j][0]
        # bid_value[j] = weight_list_list[j][random_number_list[j][0]]
        bid_value_list[j] = weight_list_list[j][random_number_list[j][0]]

    for i in range(1, random_number_size):
        if sum(bid_value_list) >= concession_value:
            break
        for j in range(0, issue_size)
            if sum(bid_value_list) >= concession_value:
                break
            if bid_value_list[j] < weight_list_list[j][random_number_list[j][i]]:
                bid_value_list[j] = weight_list_list[j][random_number_list[j][i]]
                bid_index_list[j] = random_number_list[j][i]

    return bid_index_list

# def get_bid_above_concession_value(list weight_list_list, list random_number_list, double concession_value):
#     cdef size_t random_number_size = len(random_number_list[0])
#     cdef size_t issue_size = len(weight_list_list)
#     cdef double bid_value = 0
#     cdef double bid_value_max = 0
#
#     bid_index_list = [None] * issue_size
#     bid_index_list_max = [None] * issue_size
#     for i in range(0, random_number_size):
#         if  bid_value > bid_value_max:
#             bid_value_max = bid_value
#             for j in range(0, issue_size):
#               bid_index_list_max[j] = bid_index_list[j]
#         if bid_value >= concession_value:
#             break
#         bid_value = 0
#         for j in range(0, issue_size):
#             bid_index_list[j] = random_number_list[j][i]
#             bid_value += weight_list_list[j][random_number_list[j][i]]
    # return bid_index_list_max
