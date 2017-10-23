cimport numpy as np

cdef extern from "cython_c_code.h":
    int c_algo(int *arr_a, int *arr_b, int size_a, int size_b)

def cy_algo(np.ndarray[int, ndim=1] arr_a, np.ndarray[int, ndim=1] arr_b):
    return c_algo(&arr_a[0], &arr_b[0], len(arr_a), len(arr_b))
