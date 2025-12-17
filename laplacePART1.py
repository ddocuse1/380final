#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 11:36:59 2025

@author: dustindocusen
"""

import numpy as np
from matplotlib import pyplot as pp
from matplotlib.animation import FuncAnimation as FA


dx = dy = 0.1
a,b = 10,10
maxV = 1
x = np.arange(0, dx + a, dx, dtype=float)
y = np.arange(0, dy + b, dy, dtype=float)
n = len(x)

X,Y = np.meshgrid(x,y)

V = np.zeros_like(X)

fig = pp.figure()
ax = pp.axes(xlim=[0,a],ylim=[0,b])

def init():
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    return []

def update(m):
    global V
    newV = np.zeros_like(V)
    newV[:,0] = 0
    newV[:,-1] = 0
    newV[-1,:] = 0
    newV[0,:] = 1

    for i in range(1, V.shape[0]-1):
        for j in range(1, V.shape[1]-1):
            newV[i,j] = (1/4)*(
                V[i+1,j] + V[i-1,j] +
                V[i,j+1] + V[i,j-1]
                )
            
    V = newV
    ax.cla()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    cont = ax.contourf(X, Y, V, levels=100)
    

    return cont.collections


myanim = FA(fig,update,init_func=init,interval=1)

pp.show()