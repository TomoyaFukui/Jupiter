# -*-encode: utf-8-*-

import time
import numpy as np
import numpy.random as rand
import make_bid

if __name__ == "__main__":
    start_t = time.time()

    # arr_a = [i for i in range(10)]
    # arr_b = [i for i in range(10)]

    # res = cython_code.cy_algo(np.array(arr_a), np.array(arr_b))
    # print(res)
    weight_list_list = [[0.1, 0.2, 0.3], [0.7, 0.4, 0.5, 0.1, 0.4]]
    issue_size_list = [3, 5]
    random_number_list = []
    for size in issue_size_list:
        random_number_list.append(rand.randint(0, size, 100).tolist())
    # print(random_number_list)

    a = make_bid.get_bid_above_concession_value(weight_list_list, random_number_list, 0.9)
    print("-"*50)
    print(a)
    print(weight_list_list[0][a[0]], weight_list_list[1][a[1]])

    all_time = time.time() - start_t
    print("Execution time:{0} [sec]".format(all_time))
