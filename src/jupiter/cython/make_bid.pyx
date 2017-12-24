cimport numpy as np

def get_bid_above_concession_value(list weight_list_list, list random_number_list, double concession_value):
    cdef size_t random_number_size = len(random_number_list[0])
    cdef size_t issue_size = len(weight_list_list)
    # cdef double bid_value = 0
    # cdef double bid_value_max = 0

    bid_index_list = [None] * issue_size
    bid_value_list = [0] * issue_size

    for j in range(0, issue_size):
        bid_index_list[j] = random_number_list[j][0]
        bid_value_list[j] = weight_list_list[j][random_number_list[j][0]]

    for i in range(1, random_number_size):
        if sum(bid_value_list) + 0.001 >= concession_value:
            break
        for j in range(0, issue_size):
            if bid_value_list[j] < weight_list_list[j][random_number_list[j][i]]:
                bid_value_list[j] = weight_list_list[j][random_number_list[j][i]]
                bid_index_list[j] = random_number_list[j][i]
            if sum(bid_value_list) + 0.001 >= concession_value:
                break

    return bid_index_list

# def get_bid_above_concession_value(list weight_list_list, list random_number_list, float concession_value):
#     # cdef int res = 0
#     cdef size_t random_number_size = len(random_number_list[0])
#     cdef size_t issue_size = len(weight_list_list)
#     cdef float bid_value = 0
#     cdef float bid_value_max = 0
#
#     bid_index_list = [None] * issue_size
#     bid_index_list_max = [None] * issue_size
#     for i in range(0, random_number_size):
#         # print(i, bid_value)
#         if  bid_value > bid_value_max:
#             bid_value_max = bid_value
#             for j in range(0, issue_size):
#               bid_index_list_max[j] = bid_index_list[j]
#         if bid_value >= concession_value:
#             # print("end")
#             break
#         bid_value = 0
#         for j in range(0, issue_size):
#             # print(random_number_list[j][i], weight_list_list[j][random_number_list[j][i]])
#             bid_index_list[j] = random_number_list[j][i]
#             bid_value += weight_list_list[j][random_number_list[j][i]]
#             # ran = np.random.randint(0, size-1)
#             # bid_value += weight_list_list[i][ran]
#             # bid_index_list[i] = ran
#     return bid_index_list_max
