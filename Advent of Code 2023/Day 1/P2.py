import numpy as np
with open('input.txt') as f:
    brokenLines=f.readlines()

digitNames = ['twone','zerone','sevenine','eighthree','eightwo','fiveight','oneight','threeight','nineight','one','two','three','four','five','six','seven','eight','nine','zero']
digits = ['21','01','79','83','82','58','18','38','98','1','2','3','4','5','6','7','8','9','0']

lines = []

for i in brokenLines:
    for j in range(len(digitNames)):
        if digitNames[j] in i:
            i=i.replace(digitNames[j],digits[j])
    lines.append(i)

outsides = []

for i in lines:
    outside = []
    for j in range(0,len(i)+1,1):
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

print(outsides)


print(sum(outsides))
