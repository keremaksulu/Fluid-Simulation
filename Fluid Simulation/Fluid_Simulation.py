#Incompressible, 2D, 1000x1000 grid

import numpy as np
import matplotlib as plt
h = 1 # Grid Size
dt = 1
u = np.zeros(1000,1000)
v = np.zeros(1000,1000)

s = np.ones(1000,1000) #0 for obstacle 1 for fluid cells

for i in range(1000):
    for j in range(1000):
        divergence = u[i+1,j] - u[i,j] + v[i,j+1] - v[i,j]
        S = s[i+1,j] + s[i-1,j] + s[i,j+1] + s[i,j-1]
        
        u[i,j] = u[i,j] + divergence * s[i-1,j] / S
        u[i+1,j] = u[i+1,j] - divergence * s[i+1,j] / S
        v[i,j] = v[i+1,j] + divergence * s[i-1,j] / S
        v[i+1,j] = v[i+1,j] - divergence * s[i+1,j] / S

# Overrelaxation factor: multiply divergence by 1.9 to converge faster
overrelaxed = True
if overrelaxed:
    divergence = 1.9 * divergence

# Advection
v_avg = (v[i-1,j+1] + v[i,j+1] + v[i-1,j] + v[i,j-1]) * 0.25
x = i - dt * u[i,j]
y = j - dt * v_avg

# General Grid Interpolation
w00 = 1 - x/h
w01 = x/h
w10 = 1 - y/h
w11 = y/h
v_bar = w00*w10*v[i,j] + w01*w10*v[i+1,j] + w00*w11*v[i,j+1] + w01*w11*v[i+1,j+1]



# Create cylindirical solid with center at x,y
# Create cubic solid with center at x,y
# Create Uniform flow 