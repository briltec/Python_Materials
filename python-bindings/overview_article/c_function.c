#include <stdio.h>
#include "c_function.h"


float c_function(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("    In c_func: int: %d float %.1f returning  %.1f\n", int_param,
            float_param, return_value);
    return int_param * float_param;
}

