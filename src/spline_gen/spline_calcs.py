import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt 


def get_slope(splinerep_tck:tuple, point):
    slope = interpolate.splev(point, splinerep_tck, der=1)
    return slope   

def calc_tangent(splinerep_tck:tuple, ):
    tan_slope = get_slope(splinerep_tck, point)

    y_int = y - tan_slope * x
    
    tangent_y = lambda x: tan_slope * x + y_int


def calc_normal(splinerep_tck:tuple, point):
    norm_slope = -1/get_slope(splinerep_tck, point)

    y_int = y - norm_slope * x
    norm_y = lambda x: norm_slope * x + y_int