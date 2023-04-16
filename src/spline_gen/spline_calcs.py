import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt 


def get_slope(splinerep_tck:tuple, u):
    dx, dy = interpolate.splev(u, splinerep_tck, der=1)
    return dy/dx    

# #v1
# def calc_tangents(splinerep_tck:tuple, u, x, y):
#     tan_slope = get_slope(splinerep_tck, u)
       
#     y_int = y - tan_slope * x
#     tangent_y = lambda x: tan_slope * x + y_int

#     return tangent_y

# #v2
# def calc_tangents(splinerep_tck:tuple, u, x_vals, y_vals):
#     tan_slopes = get_slope(splinerep_tck, u) #array of slopes at each point 
       
#     y_ints = y_vals - tan_slopes * x_vals #array of y_ints for tangents at each point
#     find_tan_y = lambda x,slope,intercept: (slope * x) + intercept 
    
#     tan_len = 6
#     pt_scalars = range(-tan_len//2,tan_len//2)
    
#     tan_xs = [x+pt_scalars for x in [x for x in x_vals]]
#     tan_ys = []
    
#     for slope,y_int,x in zip(tan_slopes, y_ints, tan_xs):
#         tan_ys.append(np.column_stack((x,find_tan_y(x, slope, y_int))))

#     tan_ys = np.array(tan_ys)
    
#     return tan_ys

def calc_tangents(splinerep_tck:tuple, u, x_vals, y_vals):
    tan_slopes = get_slope(splinerep_tck, u) #array of slopes at each point 
       
    y_ints = y_vals - tan_slopes * x_vals #array of y_ints for tangents at each point
        
    return tan_slopes, y_ints


# #v1
# def calc_normals(splinerep_tck:tuple, u):
#     norm_slope = -1/get_slope(splinerep_tck, u)
    
#     y_int = y - norm_slope * x
#     norm_y = lambda x: norm_slope * x + y_int

#     return norm_y

# # v2
# def calc_normals(splinerep_tck:tuple, u, x_vals, y_vals):
#     norm_slopes = -1/get_slope(splinerep_tck, u) #array of slopes at each point 
    
#     y_ints = y_vals - norm_slopes * x_vals #array of y_ints for tangents at each point
#     find_norm_y = lambda x,slope,intercept: (slope * x) + intercept 
    
#     tan_len = 6
#     pt_scalars = range(-tan_len//2,tan_len//2)
    
#     norm_xs = [x+pt_scalars for x in [x for x in x_vals]]
#     norm_ys = []
    
#     for slope,y_int,x in zip(norm_slopes, y_ints, norm_xs):
#         norm_ys.append(np.column_stack((x,find_norm_y(x, slope, y_int))))

#     norm_ys = np.array(norm_ys)
    
#     return norm_ys

def calc_normals(splinerep_tck:tuple, u, x_vals, y_vals):
    norm_slopes = -1/get_slope(splinerep_tck, u) #array of slopes at each point 
    
    y_ints = y_vals - norm_slopes * x_vals #array of y_ints for tangents at each point
        
    return norm_slopes, y_ints