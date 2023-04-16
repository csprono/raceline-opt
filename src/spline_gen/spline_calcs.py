import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt 


def get_slope(splinerep_tck:tuple, u):
    dx, dy = interpolate.splev(u, splinerep_tck, der=1)
    return dy/dx    

def calc_tangent(splinerep_tck:tuple, u, x, y):
    tan_slope = get_slope(splinerep_tck, u)
       
    y_int = y - tan_slope * x
    tangent_y = lambda x: tan_slope * x + y_int

    return tangent_y

# def calc_normal(splinerep_tck:tuple, x, y):
#     norm_slope = -1/get_slope(splinerep_tck, [x, y])
    
#     y_int = y - norm_slope * x
#     norm_y = lambda x: norm_slope * x + y_int

#     return norm_y

def calc_normal(splinerep_tck:tuple, u):
    norm_slope = -1/get_slope(splinerep_tck, u)
    
    y_int = y - norm_slope * x
    norm_y = lambda x: norm_slope * x + y_int

    return norm_y