import numpy as np

x_vals = np.array(range(1,11))
slopes = np.array(range(2,21,2))
y_ints = np.array(range(3,31,3))

pt_scalars = range(-5,5)

find_tan_y = lambda x,slope,intercept: (slope * x) + intercept 


tan_xs = [x+pt_scalars for x in [x for x in x_vals]]

 
result = []

for slope,y_int in zip(slopes,y_ints):
    for x in tan_xs:
        result.append((find_tan_y(x, slope, y_int)))

result = np.array(result)

print(result)
print(result.shape)

# print(np.transpose(np.array([(x,test(x)) for x in [x+vectors for x in [x for x in x_vals]]])))

