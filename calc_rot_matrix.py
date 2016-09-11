# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:41:52 2016

@author: gabrielfior
"""

import math
import numpy as np
import numpy.linalg as la

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def skew(v):
    if len(v) == 4: v = v[:3]/v[3]
    skv = np.roll(np.roll(np.diag(v.flatten()), 1, 1), -1, 0)
    return skv - skv.T

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))



 

def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)
#a=[-0.03028276087608503, -0.012924023470128339, ]

#Accel X: -0.30          Y: -0.39        Z: -10.12  
#a = [-0.3,-0.39,-10.12] 
a =  [1,0,0]
#b=[0,0, -1]
b = [0,1,0]
#%Normalizing vectors
anorm = a/np.linalg.norm(a)
bnorm = b/ np.linalg.norm(b)

#Calculate mapping

v=np.cross(a,b)
s = np.linalg.norm(v)
c = np.dot(a,b)
skew1 = skew(v)

RU = np.eye(3) + skew1 + (skew1*skew1*((1.-c)/(1)))


x = [a[1]*b[2] - b[1]*a[2],a[2]*b[0] - b[2]*a[0],a[0]*b[1] - b[0]*a[1]]
x = x/np.linalg.norm(x);
theta = np.arccos(np.cross(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)));
A = [[0    ,-x[2],  x[1]],
     [x[2],0,-x[0]],
     [-x[1],x[0],0]]
R = np.eye(3) + np.sin(theta)*A + (1-np.cos(theta))*A*A;


#theta = angle_between(a,b)
#c, s = np.cos(theta), np.sin(theta)
#R = np.matrix('{} {} {}; {} {} {}; {} {} {}'.format(c, -s, s, c))