#! python3

import sys

#pour la premiere partie
# A = X(1) -> Rock
# B = Y(2) -> paper
# C = Z(3) -> siceaux 

# 0 perdu
# 3 egalité
# 6 victoire

# not very nice code here
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

# but better here 

#first part
dic = {'X': 1, 'Y': 2, 'Z': 3}
def shapeScore(me):
    return dic[me]

#for the second part
# X(1) -> need to lose
# Y(2) -> need to draw 
# Z(3) -> need to win 

dicToWin = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'},
}

def whatToPlay(other, me):
    return dicToWin[me][other]

def day_two(lst, part):
    aPlay = []
    score = 0
    for i in lst:
        aPlay = i.split(' ')
        print(aPlay)
        playScore = 0
        if part == 1:
            playScore = calcScore(aPlay[0], aPlay[1]) + shapeScore(aPlay[1])
        elif part == 2:
            whatToPlayToken = whatToPlay(aPlay[0], aPlay[1])
            playScore  = calcScore(aPlay[0], whatToPlayToken) + shapeScore(whatToPlayToken)
        else :
            Exception()
        score += playScore
        #data = input (f"jeu : lui  {aPlay[0]} code secret {aPlay[1]} ce que je joue : {whatToPlayToken} total {playScore} partie total {score} \n")
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

    day_two(lst, 2)

    fd.close()
    

if __name__ == '__main__':
    main(sys.argv)
