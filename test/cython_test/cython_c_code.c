#include "cython_c_code.h"

int c_algo(int *arr_a, int *arr_b, int size_a, int size_b){
    int res = 0;
    for(int i=0; i < size_a; i++){
        for(int j=0; j < size_b; j++){
            res = res + arr_a[i]+arr_b[j];
        }
    }
    return res;
}
