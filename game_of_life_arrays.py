#!/usr/bin/env python
# game of life
import random
import time
import os
import numpy as np
import time

# specify initial conditions

def initialize(tel,typestart):

    if(typestart=="random"):
        for i in range(1,n+1):
            for j in range(1,n+1):
               tel[i,j]=random.choice([0,1])
               newtel[i,j]=0

# glider
    elif(typestart=="glider"):

        start=10
        tel[start,start]=1
        tel[start+1,start]=1
        tel[start+2,start]=1
        tel[start+2,start+1]=1
        tel[start+1,start+2]=1
    else:
        raise ValueError("type of start must be specified")


def update_array(tel,newtel):
    offset=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            sum=0
            for nb in offset:
               sum += tel[i+nb[0],j+nb[1]]

            newtel[i,j]=tel[i,j]

            if tel[i,j]==1 :
                if sum < 2:
                  newtel[i,j]=0
                elif sum > 3:
                  newtel[i,j]=0

            else :
                if sum == 3:
                  newtel[i,j]=1

    tel[:]=newtel[:]

def update_array_noloop(tel,sumarray):

    sumarray[:]=0
    offset=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    for nb in offset:
        sumarray[1:n+1,1:n+1] += tel[1+nb[0]:n+1+nb[0],1+nb[1]:n+1+nb[1]]

    tel[ np.logical_or(sumarray < 2 , sumarray > 3)  ] = 0
    tel[ sumarray==3 ] = 1

def handle_boundary(tel):
# update ghost points  to impose periodic bc
    tel[0,0]     =tel[n,n]
    tel[n+1,0]   =tel[1,n]
    tel[n+1,n+1] =tel[1,1]
    tel[0,n+1]   =tel[n,1]

    for k in range(1,n+1):
        tel[k,0]   =tel[k,n]
        tel[n+1,k] =tel[1,k]
        tel[k,n+1] =tel[k,1]
        tel[0,k]   =tel[n,k]

    return

def handle_boundary_noloop(tel):
# update ghost points  to impose periodic bc
    tel[0,0]     =tel[n,n]
    tel[n+1,0]   =tel[1,n]
    tel[n+1,n+1] =tel[1,1]
    tel[0,n+1]   =tel[n,1]

    tel[1:n+1,0]   =tel[1:n+1,n]
    tel[n+1,1:n+1] =tel[1,1:n+1]
    tel[1:n+1,n+1] =tel[1:n+1,1]
    tel[0,1:n+1]   =tel[n,1:n+1]

    return

def print_array(tel):
    os.system("clear")
    print 2*(n+1)*"X"
    for j in range(1,n+1):
        print "X",
        for i in range(1,n+1):
               if tel[i,j]==1:
                 print "O",
               else:
                 print " ",
        print "X",
        print ""
    print 2*(n+1)*"X"
    time.sleep(0.1)

# begin main

n=60

tel = np.zeros((n+2,n+2),dtype=int)
newtel = np.zeros((n+2,n+2),dtype=int)
sumarray = np.zeros((n+2,n+2),dtype=int)

initialize(tel,"glider")

maxiterations=400
iteration=0

start=time.time()

while iteration<maxiterations:
    iteration=iteration+1
#    handle_boundary(tel)
#    update_array(tel,newtel)
    handle_boundary_noloop(tel)
    update_array_noloop(tel,sumarray)

    print_array(tel)

stop=time.time()

print("total time ",stop-start)
