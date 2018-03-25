# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:17:34 2018

@author: careymcmanus
"""

from random import *

file = open('maze.txt', 'w')

height = randrange(100)
width = randrange(200)
start = [randrange(width), randrange(height)]
end = [randrange(width), randrange(height)]
obstacles = []
for i in range(randint(0,100)):
    obstacles.append([randrange(width - 1), randrange(height - 1), randrange(10), randrange(10)])


file.write(str(width)+','+str(height)+ '\n')
file.write(str(start[0])+','+str(start[1])+ '\n')
file.write(str(end[0])+','+str(end[1])+ '\n')
for member in obstacles:
    file.write(str(member[0]) + ',' + str(member[1]) + ',' + str(member[2]) + ',' + str(member[3]) + '\n')

file.close()