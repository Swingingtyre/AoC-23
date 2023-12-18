import numpy as np
with open('input.txt') as f:
    lines=f.readlines()

rounds=[]
#Collect Information
for i in lines:
    winningNums = []
    draws = []
    readWinning = False
    readDraws = False
    tempNum = ''
    for j in range(len(i)):
        if i[j]==':':
            readWinning = True
        if readWinning:
            if i[j] == ' ' and tempNum != '':
                winningNums.append(tempNum)
                tempNum = ''
            if i[j].isdigit():
                tempNum = tempNum+i[j]
            if i[j] == '|':
                readWinning = False
                readDraws = True
                tempNum = ''
        if readDraws:
            if i[j] == ' ' and tempNum != '':
                draws.append(tempNum)
                tempNum = ''
            if i[j].isdigit():
                tempNum = tempNum+i[j]
            if i[j] == '\n':
                readDraws = False
                draws.append(tempNum)
                tempNum = ''
    rounds.append([winningNums,draws])

roundWins=[]
for round in rounds:
    wins = sum(draw in round[0] for draw in round[1])
    roundWins.append(wins)

initCardCountList = [1 for _ in range(len(rounds))]

cardCountList=[]
while initCardCountList:
    cardScore=roundWins[0]
    cardCount=initCardCountList[0]
    for i in range(cardScore+1):
        initCardCountList[i]+=cardCount
    roundWins.pop(0)
    initCardCountList.pop(0)
    cardCountList.append(cardCount)

print(sum(cardCountList))