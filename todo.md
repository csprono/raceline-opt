# Spline Generation
- [x] fix centreline generation
    - need to change order of x coords
    - maybe use dfs
- [x] generate splines
    - [ ] make more accurate
      -  adjust the smoothing 
         -  find difference between centreline points and spline points. Make difference small as possible
      -  maybe make dynamic? (not sure if possible)
         -  different parts of track have different smoothing

# Spline Calculations
## Trajectory Calculation
- trajectory = heading of spline
- use tangent to curve at a point
    - derivative = slope of tangent at a point
    - equation: $y-y_1 = f^\prime(x_1)*(x-x_1)$
    - 

## Normal Calculation
- perpendicular to trajectory and spline
- equation: $y-y_1 = \frac{-1}{f^\prime(x_1)}*(x-x_1)$

# Documentation
- [ ] centreline generation: [[generate_centreline]]
- [ ] generate splines: [[generate_spline]]
- [ ] spline calculation: [[spline_calculations]]
- [ ] repo readme: [[reademe]]



