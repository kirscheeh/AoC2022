#!/usr/bin/env python

data = "input/day_08.txt"
import sys
with open(data) as f:
    columns = [list(map(int, list(x))) for x in f.read().splitlines()]

# make a list of lists but vertical not horizontal
rows = [[] for x in range(len(columns[0]))]
for row in columns:
    for i in range(len(row)):
        rows[i].append(row[i])
  
#outer = 2*len(columns)+2*len(columns[0])-4
max_scenic=0
visible=[[True for x in columns] for row in columns[0]]
for x in range(1, len(columns[0])-1):
    for y in range(1, len(columns)-1):
        vis=False
        # left
        counter_left=0
        helper_left =columns[x][:y]
        helper_left.reverse()
        print(helper_left)
        for index, elem in enumerate(helper_left):
            counter_left+=1
            if elem < columns[x][y] and elem > helper_left[index-1]:
                pass 
            else:
                break
        print("counter left", counter_left)
        if not [*filter(lambda a: a >= columns[x][y], columns[x][:y])]:
            vis=True
        
        # right
        counter_right=0
        for index, elem in enumerate(columns[x][y+1:]):
            if elem < columns[x][y] and elem > columns[x][y+1:][index-1]:
                counter_right+=1
            else:
                counter_right+=1
                break
        print("counter right", counter_right)
        if not [*filter(lambda a: a >= columns[x][y], columns[x][y+1:])]:
            vis=True
            
        # up
        counter_up=0
        helper_up =rows[y][:x]
        helper_up.reverse()
        print(helper_up)
        for index, elem in enumerate(helper_up):
            if elem < columns[x][y] and elem > helper_up[index-1]:
                counter_up+=1
            else:
                counter_up+=1
                break
        print("counter up", counter_up)
        if not [*filter(lambda a: a >= rows[y][x], rows[y][:x])]:
            vis=True
            
        # down
        counter_down=0
        for index, elem in enumerate(rows[y][x+1:]):
            if elem < columns[x][y] and elem>rows[y][x+1:][index-1]:
                counter_down+=1
            else:
                counter_down+=1
                break
        print("counter down", counter_down)
        if not [*filter(lambda a: a >= rows[y][x], rows[y][x+1:])]:
            vis=True
            
        visible[x][y]=vis
        print(vis)
        curr_scenic = counter_down*counter_left*counter_right*counter_up
        print(curr_scenic)
        if curr_scenic >max_scenic:
            max_scenic=curr_scenic
        input()
            
flat_list = [item for sublist in visible for item in sublist]
print(max_scenic)
print(sum(flat_list))
        
    