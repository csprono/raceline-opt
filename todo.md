# Spline Generation
## Centreline Generation
- [x] fix centreline generation
    - need to change order of x coords
    - maybe use dfs
- [x] generate splines 
    - [ ] make more accurate
      - ideas:
        -  adjust the smoothing: find difference between centreline points and spline points. Make difference small as possible
           -  maybe make dynamic (different parts of track have different smoothing) (not sure if possible)
        - use different spline type
          - e.g. cubic spline

# Spline Calculations
## Trajectory Calculation
- trajectory = heading of spline
  - [x] calculate bearing of tangents
    - create triangle using north for 1 line
- use tangent of curve at a point
  - [x] calculate slope and y intercept of tangent
    - slope of tangent at a point on spline = derivative ($f^\prime(x)$)
    - y int = $y-y_1 = f^\prime(x_1)*(x-x_1)$
  - [ ] visualise tangent
    - [x] find series of coords starting from a point on spline
    - [ ] ensure tangent coords create line of specific length

## Normal Calculation
- perpendicular to trajectory and spline
- utilise previous tangent calculations
  - [x] calculate slope and y intercept of normal
    - slope of tangent at a point on spline = negative reciprocal of derivative ($\frac{-1}{f^\prime(x_1)}$)
    - y int = $y-y_1 = \frac{-1}{f^\prime(x_1)}*(x-x_1)$
  - [ ] visualise normal
    - [x] find series of coords starting from a point on spline
    - [ ] ensure normal coords create line of specific length

# Documentation
- [ ] centreline generation: [[generate_centreline]]
- [ ] generate splines: [[generate_spline]]
- [ ] spline calculation: [[spline_calculations]]
- [ ] repo readme: [[reademe]]

# Misc
## Line Plotting
- [x] plotting function (plot_line())
  - input spline x values, slope, y intercept, desired length of lines
  - calculate y coords of line
  - input to LineCollection
  - add to axes

## Calculate Bearings
- [x] bearing calculation function (calc_bearings())
  - input slope
  - method:
    - iterate through array
    - if slope > 0
      - bearing = arctan(slope)
    - elif slope < 0 
      - bearing = 180 - arctanc(abs(slope))
    - elif slope = 0
      - bearing = 90
    - else slope = undefined
      - bearing = 0 
    - NB: maybe investigate using np.where()


# Velocity Profile
- [ ] calculate curvature of turns
  - $\kappa=\left\| \frac{d T}{ds} \right\|$
    - size of rate of change of tangent vector with respect to arc length
  - 
- [ ] calculate max velocity around curves 
- [ ] 