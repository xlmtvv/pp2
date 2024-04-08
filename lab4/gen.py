def squares_gen(n):
    for i in range(1, n + 1):
        yield i * i

# generator = squares_gen(5)
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())

def print_even():
    n = int(input('n = '))
    def even_gen(n):
        for i in range(0, n + 1, 2):
            yield i

    even_numbers = ', '.join(str(num) for num in even_gen(n))
    print(even_numbers)

# print_even()
    
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for i in divisible_by_3_and_4(25):
    print(i)


# for num in divisible_by_3_and_4(30):
#     print(num)


def squares_from_a_to_b(a, b):
    for i in range(a, b+1):
        yield i * i


# for num in squares_from_a_to_b(3, 6):
#     print(num)
        

def from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i
   

# for i in from_n_to_0(4):
#     print(i)