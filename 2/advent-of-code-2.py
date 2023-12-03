LIMIT_RED = 12
LIMIT_BLUE = 14
LIMIT_GREEN = 13

def analyseGame(game):
    for extr in game:
        for xr in extr.strip().split(','):
            t = xr.split()
            if t[1] == 'red':
                if int(t[0]) > LIMIT_RED: return False
            elif t[1] == 'green':
                if int(t[0]) > LIMIT_GREEN: return False
            elif t[1] == 'blue':
                if int(t[0]) > LIMIT_BLUE: return False
    return True


def parseInput():
    games = {}
    with open('advent-of-code-2.txt', "r") as f:
        for line in f:
            games[int(line[4:line.index(':')])] = line[(line.index(':')+2):].strip().split(';')
    
    return games

def part1():
    games = parseInput()
    total = 0
    for id, game in games.items():
        if analyseGame(game):
            total += id
            print('valid game: ' + str(id))
    print('Total: ' + str(total))

#part1()

#-----------------------------------------------------------------------------------------------------------------------
def findPower(aggrExtr):
    minR = 0
    minG = 0
    minB = 0
    for extr in aggrExtr:
        xr = extr.split()
        if xr[1] == 'red':
            if int(xr[0]) > minR: minR = int(xr[0])
        if xr[1] == 'blue':
            if int(xr[0]) > minB: minB = int(xr[0])
        if xr[1] == 'green':
            if int(xr[0]) > minG: minG = int(xr[0])
    return minR*minG*minB


def aggregateList(game):
    aggr = []
    for extr in game:
        for xr in extr.strip().split(','):
            aggr.append(xr)
    return aggr


def part2():
    games = parseInput()
    total = 0
    for _, game in games.items():
        total += findPower(aggregateList(game))

    print('Total: ' + str(total))

part2()