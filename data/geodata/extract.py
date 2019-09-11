import numpy as np


landcover = open('statsland.txt').readlines()
temp = {}
sum = 0
for line in landcover:
    temp[line.split()[1]] = int(line.split()[2])
    sum += int(line.split()[2])

forest = (temp['3']*100)/sum
print(sum, temp['3'], forest)


