import os

def task1(path):
    '''
    Write a Python program to list only directories, files and all directories, files in a specified path.
    '''

    print([name for name in os.listdir(path)]) # lists dirs and files
    print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # lists dirs
    print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) # lists files


def task2(path):
    '''
    Write a Python program to check for access to a specified path. 
    Test the existence, readability, writability and executability of the specified path
    '''

    if os.path.exists(path):
        result = 'Path is '

        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '

        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '

        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'

        print(f'Path {path} exists\n{result}')

    else:
        print(f'Path {path} does not exists')



def task3(path):
    '''
    Write a Python program to test whether a given path exists or not. 
    If the path exist find the filename and directory portion of the given path.
    '''

    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')

def task4(path):
    '''
    Write a Python program to count the number of lines in a text file.
    '''

    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')

def task5(path, l):
    '''
    Write a Python program to write a list to a file.
    '''

    with open(path, 'w') as file:
        file.write(' '.join(l))

def task6():
    '''
    Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
    '''

    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'{letter}.txt', 'w'):
            pass

    # delete these 26 files
    # for letter in ascii_uppercase:
    #     os.remove(f'{letter}.txt')
        


def task7(path1, path2):
    '''
    Write a Python program to copy the contents of a file to another file
    '''

    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read())

def task8(path):
    '''
    Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
    '''

    if os.access(path, os.F_OK):
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")