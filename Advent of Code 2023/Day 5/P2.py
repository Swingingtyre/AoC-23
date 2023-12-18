import numpy as np
with open('input.txt') as f:
    lines=f.readlines()
category = []
digits = []
tempNum = ''
for i in lines:
    for j in range(len(i)):
        if i[j] == ':':
            if digits != []:
                category.append(digits)
            digits=[]
        if i[j].isdigit():
            tempNum+=i[j]
        if i[j] in [' ', '\n']:
            if tempNum != '':
                digits.append(int(tempNum))
            tempNum = ''

seeds = category[0]
category.pop(0)

def getMaps(array):
    subArray = []
    outArray = []
    for i in array:
        subArray.append(i)
        if len(subArray) == 3:
            outArray.append(subArray)
            subArray = []
    return outArray

def getPositions(array,map):
    out=[]
    for i in array:
        mapFound=False
        for j in map:
            if i-j[1]<=j[2] and j[1]<i:
                out.append(j[0]+(i-j[1]))
                mapFound=True
        if mapFound == False:
            out.append(i)
    return out

maps = [getMaps(map) for map in category]

for map in maps:
    seeds = getPositions(seeds,map)

print(min(seeds))