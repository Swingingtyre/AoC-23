import numpy as np
with open('input.txt') as f:
    lines=f.readlines()

outsides = []
for i in lines:
    outside = []
    for j in range(len(i)+1):
        try:
            outside.append(int(i[j]))
            break
        except:
            pass
    for j in range(len(i)+1,-1,-1):
        try:
            outside.append(int(i[j]))
            break
        except:
            pass
    outsides.append(int(str(outside[0])+str(outside[1])))

print(sum(outsides))