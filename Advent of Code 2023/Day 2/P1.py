import numpy as np
with open('input.txt') as f:
    lines=f.readlines()

colors = ['red','green','blue']

games = []
for i in lines:
    sets = i.split(' ')
    rounds = []
    round = {'red':0, 'green':0, 'blue':0}
    for j in range(len(sets)):
        for k in colors:
            if k in sets[j]:
                round[str(k)] = sets[j-1]
        if ';' in sets[j] or j >= len(sets)-1:
            rounds.append(round)
            round = {'red':0, 'green':0, 'blue':0}
    games.append(rounds)

for i in games:
    print(i)

gameIndex = 0
validGameSum=0

for game in games:
    sumFlag = True
    gameIndex+=1
    for round in game:
        if int(round.get('red')) > 12 or int(round.get('green')) > 13 or int(round.get('blue')) > 14:
            sumFlag = False
            print(gameIndex,'impossible')
            break
    if sumFlag==True:
        validGameSum+=gameIndex
        print(gameIndex,'possible')

print(validGameSum)