# -*-encode: utf-8-*-
import time

if __name__ == "__main__":
    start_t = time.time()

    arr_a = [i for i in range(1000)]
    arr_b = [i for i in range(1000)]

    res = 0
    for elem_a in arr_a:
        for elem_b in arr_b:
            res = res + elem_a + elem_b
    print(res)

    all_time = time.time() - start_t
    print("Execution time:{0} [sec]".format(all_time))
