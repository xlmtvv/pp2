def converter(grams):
    return 28.3495231 * grams


def toCelcius(f):
    print((5 / 9) * (f - 32))

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            print(num_chickens, num_rabbits)
            return
    print("No solution")



def filter_prime(nums: list):

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return False if n == 1 else True
    
    return list(filter(lambda x: isPrime(x), nums))

def str_permutations(s):
    from itertools import permutations
    [print(''.join(p)) for p in permutations(s)]
        
def changeOrder(s):
    print(' '.join(reversed(s.split())))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        
    return False

def sph_vol(r):
    from math import pi
    return (4/3) * pi * (r**3)


def uniqueList(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i) 
    return res

def is_pal(s):
    return True if s == s[::-1] else False

def hist(arr):
    for i in arr:
        print('*' * i)


def guessNumber():
    from random import randint
    rand = randint(1, 20)

    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
    counter = 0
    while True:
        num = int(input())
        counter += 1
        if num < rand:
            print('Your guess is too low.\nTake a guess.')
        elif num> rand:
            print('Your guess is too high.\nTake a guess.')
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break

