# Spline Generation
- fix centreline generation
    - need to change order of x coords
    - maybe use dfs

# Spline Calculations
## Trajectory Calculation
- trajectory = heading of spline
- use tangent to curve at a point
    - derivative = slope of tangent at a point
    - equation: $y-y_1 = f^\prime(x_1)*(x-x_1)$

## Normal Calculation
- perpendicular to trajectory and spline
- equation: $y-y_1 = \frac{-1}{f^\prime(x_1)}*(x-x_1)$

# Documentation
- centreline generation: [[generate_centreline]]
- generate splines: [[generate_spline]]
- spline calculation: [[spline_calculations]]
- repo readme: [[reademe]]



