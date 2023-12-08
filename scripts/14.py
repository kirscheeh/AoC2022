#!/usr/bin/env python

import re, sys

data = open("input/day_14.txt").read().splitlines()

# transform data into tuples of edge points
for line in data:
    coords = re.findall("[0-9]{1,3},[0-9]{1,3}", line)
    coords = [tuple(map(int, x.split(","))) for x in coords]

print(coords)

maximal_x=0
maximal_y=0

# draw grid
grid={}
for index in range(len(coords)-1):
    start_x, start_y = coords[index]
    stop_x, stop_y  = coords[index+1]
    
    grid[]
    
    if start_x == stop_x:
        start = min(start_y, stop_y)
        stop = max(start_y, stop_y)+1
        if stop > maximal_y:
            maximal_y = stop-1
        for dist in range(start, stop):
            grid[(start_x, dist)]="#"
    elif start_y == stop_y:
        start = min(start_x, stop_x)
        stop = max(start_x, stop_x)+1
        if stop > maximal_x:
            maximal_x = stop-1
        for dist in range(start, stop):
            grid[(dist, start_y)]="#"
    else:
        print("oops, something went wrong!")

print(grid)
print(maximal_x, maximal_y)
sys.exit()

units=0

print(maximal_x, maximal_y)
while True:
    x=500 
    y=0
    while (x, y) not in grid.keys():
        print(x,y)
        if y >= maximal_y:
            break
        inside=True
        # down
        if (x, y+1) not in grid.keys():
            y+=1
        else:
            # diagonally left
            if (x-1, y+1) not in grid.keys():
                x-=1
                y+=1
            # diagonally right
            elif (x+1, y+1) not in grid.keys():
                x+=1
                y+=1
            else:
                if (x, y) in grid.keys():
                    print("FINAL", units)
                    break
                grid[(x, y)]="o"
                units+=1
    print(grid)        
    if  y >= maximal_y:
            break
print(units)       