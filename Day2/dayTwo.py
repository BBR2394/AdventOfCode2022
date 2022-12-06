#! python3

import sys

def workOnList(lst):
    maxNum = 0
    totalSum = 0
    lstRes = []


    for i in lst:

        if len(i) == 0:
            print(f'tetal {totalSum} et maxNum actuel est : {maxNum}')
            #data = input ("suivant ?\n")
            lstRes.append(totalSum)
            if totalSum > maxNum:
                maxNum = totalSum
                totalSum = 0
            else:
                totalSum = 0
        else:
            totalSum += int(i)

    print(f'le maxNumimum est : {maxNum} ..')
    lstRes.sort()
    lstRes.reverse()
    print(f'lezs trois premier sont : {lstRes[0]} {lstRes[1]} {lstRes[2]}')

# A = X(1) -> Rock
# B = Y(2) -> paper
# C = Z(3) -> siceaux 

# 0 perdu
# 3 egalité
# 6 victoire

def calcScore(other, me):
    if other == 'A':
        if me == 'X':
            return 3
        elif me == 'Y':
            return 6
        elif me == 'Z':
            return 0
    if other == 'B':
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        elif me == 'Z':
            return 6
    if other == 'C':
        if me == 'X':
            return 6
        elif me == 'Y':
            return 0
        elif me == 'Z':
            return 3

dic = {'X': 1, 'Y': 2, 'Z': 3}
def shapeScore(me):
    return dic[me]

def day_two(lst):
    aPlay = []
    score = 0
    for i in lst:
        aPlay = i.split(' ')
        print(aPlay)
        playScore = calcScore(aPlay[0], aPlay[1]) + shapeScore(aPlay[1])
        score += playScore
        data = input (f"jeu : lui  {aPlay[0]} moi {aPlay[1]} total {playScore} partie total {score} \n")
        aPlay.clear()
    
    print(f"jeu : score total {score} \n")

def main(av):
    print("hello")
    if len(av) >= 2:
        fd = open(av[1], 'r')
    else:
        fd = open ("./input.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    day_two(lst)

    fd.close()
    

if __name__ == '__main__':
    main(sys.argv)
