# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:06:33 2020

@author: user
"""


##Tower of Hanoi suing recursive algorithm
#The algorithm goes as follows
#Step 1 − Move n-1 disks from source to aux
#Step 2 − Move nth disk from source to dest
#Step 3 − Move n-1 disks from aux to dest
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print('Move disk', n, 'from', from_rod, 'to', to_rod)
    else:
        tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
        print('move disk', n, 'from', from_rod, 'to', to_rod)
        tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)   
        
tower_of_hanoi(3, 'A', 'B', 'C')
        