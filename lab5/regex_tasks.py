'''
Python RegEx exercises

Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

Write a Python program to find sequences of lowercase letters joined with a underscore.

Write a Python program to find the sequences of one upper case letter followed by lower case letters.

Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

Write a Python program to replace all occurrences of space, comma, or dot with a colon.

Write a python program to convert snake case string to camel case string.

Write a Python program to split a string at uppercase letters.

Write a Python program to insert spaces between words starting with capital letters.

Write a Python program to convert a given camel case string to snake case.
'''

import re


def task1():
    '''
    Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
    '''
    pattern = re.compile(r'ab*')
    
    text = input()

    print("YES" if pattern.search(text) else "NO")



def task2():
    '''
    Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
    '''
    pattern = re.compile(r'ab{2,3}')

    text = input()

    print("YES" if pattern.search(text) else "NO")


def task3():
    '''
    Write a Python program to find sequences of lowercase letters joined with a underscore.
    '''

    pattern = re.compile(r'[a-z]+\_')

    text = input()

    print(pattern.findall(text))

    
def task4():
    '''
    Write a Python program to find the sequences of one upper case letter followed by lower case letters.
    '''

    pattern = re.compile(r'[A-Z]{1}[a-z]+')

    text = input()

    print(pattern.findall(text))

def task5():
    '''
    Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
    '''

    pattern = re.compile(r'a.+b\Z')

    text = input()

    print("YES" if pattern.search(text) else "NO")

def task6():
    '''
    Write a Python program to replace all occurrences of space, comma, or dot with a colon.
    '''

    pattern = re.compile(r'[ ,.]')

    text = input()

    print(pattern.sub(':', text))


def task7():
    '''
    Write a python program to convert snake case string to camel case string.
    '''
    def snake_to_camel(snake_case):
        return re.sub(r"_([a-z])", lambda s: s.group(1).upper(), snake_case)
    

    snakeCase = input()

    camelCase = snake_to_camel(snakeCase)

    print(camelCase)

def task8():
    '''
    Write a Python program to split a string at uppercase letters.
    '''

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())


def task9():
    '''
    Write a Python program to insert spaces between words starting with capital letters.
    '''

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())

def task10():
    '''
    Write a Python program to convert a given camel case string to snake case.
    '''

    def camelToSnake(snake_case):
        return re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), snake_case).lower()
    
    camelCase = input()

    snakeCase = camelToSnake(camelCase)

    print(snakeCase)

