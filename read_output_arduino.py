# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:09:47 2016

@author: gabrielfior
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int1

file1 = '/Users/gabrielfior/Dropbox/techfest/trajec_calculation/try3.txt'

with open(file1) as f:
    x= f.readlines()
    

count=0

for i in x:
    if 'Time' in i:
        break
    count=count+1
    
x = x[count:]

accx=[]#m/s2
accy=[]
accz=[]
time_list=[]
gyrox=[]#dgs
gyroy=[]
gyroz=[]

for ii in x:
    
    if 'Time' in ii:
        time_list.append(int(ii.split(' ')[-1]))
    
    elif 'Accel' in ii: #acceleremoter data
        accx.append(np.double(filter(None,ii.split(' '))[2]))   
        accy.append(np.double(filter(None,ii.split(' '))[4]))
        accz.append(np.double(filter(None,ii.split(' '))[6]))

    elif 'Gyro' in ii: #acceleremoter data
        try:
            gyrox.append(np.double(filter(None,ii.split(' '))[2]))   
            gyroy.append(np.double(filter(None,ii.split(' '))[4]))
            gyroz.append(np.double(filter(None,ii.split(' '))[6]))
        except IndexError:
            pass

arrayx = np.array(gyroz)
fftx = np.fft.fft(arrayx)


#plt.figure(1)
#plt.plot(time_list,accx)
#plt.figure(2)
#plt.plot(time_list,accy)
#plt.figure(3)
#plt.plot(time_list,accz,'o')
#plt.figure(4)
#plt.plot(time_list[:-1],gyroz)

## Calculate z height

while len(accz) != len(time_list):
    if len(accz)>len(time_list):
        del accz[-1]
    else:
        del time_list[-1]

time_list_new=[]
t0 = time_list[0]
time_list_new[:] = [0.001*(x - t0) for x in time_list]


ylist=[]
time=0
z0=0.
vz0 = 0
list_dt=[]
listz=[]
az0=0.
    
plt.plot(listz)
plt.figure(2)
plt.plot(gyroz)
plt.plot(gyrox)
plt.plot(gyroy)
plt.plot((np.sqrt(np.abs(gyroz)+np.abs(gyroy)+np.abs(gyrox))))
plt.show()