import numpy as np
# https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection

#The line is described by two points on it, la and lb
la = np.array([0,0,2]) # point 1 on line
lb = np.array([1,0,1]) #point 2 on line
lab = lb-la # vector from point 1 to point 2

# the line passing through la and lb is la + lab*t, where t is a scalar parameter

# the points on a plane can be described by three points: p0, p1, p2
p0 = np.array([0,0,0]) # point 0 on plane
p1 = np.array([1,0,0]) # point 1 on plane
p2 = np.array([0,1,0]) # point 2 on plane

p01 = p1-p0 # vector from point 0 to point 1
p02 = p2-p0 # vector from point 0 to point 2

# the plane passing through p0, p1, p2 is p0 + p01*u + p02*v, where u and v are scalar parameters

# There is a way to set this up as a system of linear equations and solving for t,u,v, explained in the wikipedia article

A = np.array([-lab, p01, p02]).T # the matrix of coefficients
b = np.array([la-p0]).T# the vector of constants

tuv = np.matmul(np.linalg.inv(A),b) # solve the system of linear equations

solution = la+lab*tuv[0] # the solution is the point of intersection
print(f"solution = {solution}")