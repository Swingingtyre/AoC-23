import numpy as np
with open('input.txt') as f:
    lines=f.readlines()

lineNums = []
#Number Positions
for i in lines:
    i = f'{i}.'
    tempNum = ''
    nums = []
    startPos = ''
    endPos = ''
    for j in range(len(i)+1):
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

lineStars = [[]]
#Star Positions
for i in lines:
    i = f'{i}.'
    stars=[]
    for j in range(len(i)):
        if i[j] not in ['.', ' ', '\n']:
            try:
                int(i[j])
            except:
                if i[j] == '*':
                    stars.append(j)
    lineStars.append(stars)
lineStars.append([])

adjNums = []
#Collecting the Stars that correspond with each starred value
#e.g. (672,1,0) relates the integer 672 to the first (0) star on the 2nd (1) line
for j, nums in enumerate(lineNums, start=1):
    for num in nums:
        for i in range(num[1]-1,num[2]+1):
            try:
                if i in lineStars[j-1]:
                    adjNums.append((int(num[0]),j-2,lineStars[j-1].index(i)))
            except IndexError:
                pass
            if i in lineStars[j]:
                adjNums.append((int(num[0]),j-1,lineStars[j].index(i)))
            try:
                if i in lineStars[j+1]:
                    adjNums.append((int(num[0]),j,lineStars[j+1].index(i)))
            except IndexError:
                pass
#Add product of starred values which both correspond to the same star
totalProduct=0
product=0
while adjNums:
    i=adjNums[0]
    for j in adjNums[1:]:
        if (i[1],i[2]) == (j[1],j[2]):
            product=i[0]*j[0]
            totalProduct += product
            break
    adjNums.pop(0)

print(totalProduct)