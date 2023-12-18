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

score = sum(2**(wins-1) for wins in roundWins if wins!=0)
print(score)
            
