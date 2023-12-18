import numpy as np
with open('input.txt') as f:
    lines=f.readlines()

lineNums = []
#Number Positions
for i in lines:
    i=i+'.'
    tempNum = ''
    nums = []
    startPos = ''
    endPos = ''
    for j in range(0,len(i)+1):
        try:
            int(i[j])
            tempNum=str(tempNum)+str(i[j])
            if startPos == '':
                startPos = j
        except:
            if tempNum != '':
                endPos = j
                nums.append((tempNum,startPos,endPos))
                startPos = ''
                endPos = ''
            tempNum = ''
    lineNums.append(nums)

lineSyms = [[]]
#Symbol Positions
for i in lines:
    i=i+'.'
    syms=[]
    for j in range(0,len(i)):
        if i[j] != '.' and i[j] != ' ' and i[j] != '\n':
            try:
                int(i[j])
                pass
            except:
                syms.append(j)
    lineSyms.append(syms)
lineSyms.append([])

adjNums = []
j=1
for nums in lineNums:
    for num in nums:
        for i in range(num[1]-1,num[2]+1):
            if i in lineSyms[j-1] or i in lineSyms[j] or i in lineSyms[j+1]:
                adjNums.append(int(num[0]))
    j+=1

print(sum(adjNums))