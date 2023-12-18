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

gameCubeLimit=[]

for game in games:
    maxRed = 0
    maxBlue = 0
    maxGreen = 0
    for round in game:
        if int(round.get('red')) >= maxRed:
            maxRed = int(round.get('red'))
        if int(round.get('blue')) >= maxBlue:
            maxBlue = int(round.get('blue'))
        if int(round.get('green')) >= maxGreen:
            maxGreen = int(round.get('green'))
    gameCubeLimit.append({'red':maxRed,'blue':maxBlue,'green':maxGreen})
    
gameProducts = []
for i in gameCubeLimit:
    gameProduct = int(i.get('red'))*int(i.get('blue'))*int(i.get('green'))
    gameProducts.append(gameProduct)

print(sum(gameProducts))