# from functions1 import str_permutations, has_33, guessNumber

# str_permutations("abc")

# print(has_33([1, 2, 3, 2, 1, 3, 3]))

# guessNumber()

zeroMap = [[0, '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def changeCoordinates(row, column):
    global zeroMap
    zeroMap[0][0] = '*'
    zeroMap[row][column] = 0

    for i in zeroMap:
        for j in i:
            print(j, end=" ")
        print()

changeCoordinates(1, 2)