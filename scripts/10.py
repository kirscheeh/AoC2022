#!/usr/bin/env python3

commands = open("input/day_10.txt").read().splitlines()
commands = [cmd.split() for cmd in commands]

dict_cycles={"noop":1, "addx":2}

coi=    [20, 60, 100, 140, 180, 220]
#start = [1, 41, 81, 121, 161, 201]
#end =   [40, 80, 120, 160,200,240]

cycle=1
x=1
sum_of_signal=0

CRT = "#,"*240
CRT =CRT.split(",")[:-1]

for cmd in commands: 
    try:
        cmd, curr_x = cmd
        curr_x = int(curr_x)
    except ValueError:
        curr_x = 0
        cmd=cmd[0]
    
    for i in range(dict_cycles[cmd]):
        if cycle in coi:
            sum_of_signal = sum_of_signal+cycle*x
        if cycle in [curr_x-1, curr_x, curr_x+1]:
            CRT[cycle]="."
        cycle+=1
        

    
    x+=curr_x 

print(sum_of_signal)

#print(CRT)

