#! python3

import sys

encode_dic = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

def day_three(lst):
    score = 0
    for i in lst:
        print("line : " + i)
        first = i[:int(len(i)/2)]
        second = i[int(len(i)/2):]
        charToFind = ''
        for j in first:
            if second.find(j) >= 0:
                charToFind = j
                break
        score += encode_dic[charToFind]
        print(f"first :  {first} \nsecond : {second} charactere a trouver : {charToFind} value : {encode_dic[charToFind]} ")
        #data = input (f"continué ? taille : {len(i)}\n")
    print(f"resultats {score}")

def compare_two_backpack(first, second):
    charToFind = []

    for j in first:
        if second.find(j) >= 0:
            charToFind.append(j)
    return charToFind

def compare_two_list(first, second):
    charToFind = []
    for j in first:
        try :
            temp = second.index(j)
            charToFind.append(j)
        except:
            pass
    return charToFind

def reduce_list(lst):
    reduced = []
    for i in lst:
        if reduced == []:
            reduced.append(i)
        else :
            try: 
                reduced.index(i)
            except:
                print("IL Y A UN E ERREUR dans les données ")
                break

    return reduced


def day_three_part_two(lst):
    one = []
    two = []
    three = []
    charsToFindList = []
    score = 0
    for i in lst:
        if one == [] or two == [] or three == []:
            print("l'un des trois est vide")
            if one == []:
                one = i
            elif two == []:
                two = i
            else :
                three = i
        else : 
            print("les trois sont plein ")
            print(f"un : {one} deux {two} trois {three}")
            firstChar = compare_two_backpack(one, two)
            secondChar = compare_two_backpack(one, three)
            compareAll = compare_two_list(firstChar, secondChar)
            reduced = reduce_list(compareAll)
            if len(reduced) > 1:
                raise Exception("Erreur avec les données")
            charsToFindList.append(reduced[0])
            #data = input (f"premier char : {firstChar}--{secondChar}--{compareAll}--{reduced}--{charsToFindList}\n")
            reduced = []
            one = i
            two = []
            three = []

    print("dernier tours")
    print(f"un : {one} deux {two} trois {three}")
    firstChar = compare_two_backpack(one, two)
    secondChar = compare_two_backpack(one, three)
    compareAll = compare_two_list(firstChar, secondChar)
    reduced = reduce_list(compareAll)
    data = input (f"premier char : {firstChar}--{secondChar}--{compareAll}--{reduced}-")
    if len(reduced) > 1:
        raise Exception("Erreur avec les données")
    charsToFindList.append(reduced[0])
    data = input (f"premier char : {firstChar}--{secondChar}--{compareAll}--{reduced}\n")
    for k in charsToFindList:
        score += encode_dic[k]

    print(score)

def wich_minimal(a, b):
    return a < b

def wich_bigger(a, b):
    return a < b

def day_four(lst):
    first_grp = []
    second_grp = []
    score = 0
    for i in lst:
        print(i)
        first_grp = i.split(',')[0]
        second_grp = i.split(',')[1]
        print(first_grp)
        print(second_grp)
        firstTab = first_grp.split('-')
        secondTab = second_grp.split('-')
        resTab = []
        print(firstTab)
        print(secondTab)
        resTab.append(int(firstTab[0]) <= int(secondTab[0]))
        resTab.append(int(firstTab[1]) >= int(secondTab[1]))

        print(resTab)
        if resTab[0] == resTab[1]:
            print("on augmente le score")
            score += 1
        
    print(f"le score est de {score}")
        

def main(av):
    print("hello")
    if len(av) >= 2:
        fd = open(av[1], 'r')
    else:
        fd = open ("./input.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    #day_three(lst)
    #day_three_part_two(lst)
    day_four(lst)
    
    fd.close()

if __name__ == '__main__':
    main(sys.argv)
