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

def main(av):
    print("hello")
    if len(av) >= 2:
        fd = open(av[1], 'r')
    else:
        fd = open ("./input.txt", 'r')
    input = fd.read()
    lst = input.split('\n')
    workOnList(lst)

    fd.close()
    

if __name__ == '__main__':
    main(sys.argv)
