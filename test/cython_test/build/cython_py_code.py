# -*-encode: utf-8-*-

import time
import numpy as np
import cython_code

if __name__ == "__main__":
    start_t = time.time()

    arr_a = [i for i in range(1000)]
    arr_b = [i for i in range(1000)]

    res = cython_code.cy_algo(np.array(arr_a), np.array(arr_b))
    print(res)

    all_time = time.time() - start_t
    print("Execution time:{0} [sec]".format(all_time))
