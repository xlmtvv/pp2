def task1(numbers):
    '''
    Write a Python program with builtin function to multiply all the numbers in a list
    '''


    return eval('*'.join(list(map(str, numbers))))


def task2(s):
    '''
    Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
    '''

    uppercasse = len([i for i in s if i.isupper()])

    lowercase = len([i for i in s if i.islower()])

    print(f'uppercase letters = {uppercasse}\nlowercase letters = {lowercase}')



def task3(s):
    '''
    Write a Python program with builtin function that checks whether a passed string is palindrome or not.
    '''

    print(True if s == s[::-1] else False)

def task4():
    '''
    Write a Python program that invoke square root function after specific milliseconds.
    '''
    from time import sleep

    num = int(input())
    sleepTime = int(input())

    sleep(sleepTime / 1000)

    print(f'Square root of {num} after {sleepTime} miliseconds is {num**0.5}')

def task5(tup):
    '''
    Write a Python program with builtin function that returns True if all elements of the tuple are true.
    '''
    return True if all(tup) else False

