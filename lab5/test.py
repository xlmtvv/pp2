import re

# товары в которых есть литр или флакон

with open('row.txt', 'r') as file:
    st = file.readlines()

pattern = re.compile('мл|фл')

for s in st:
    if pattern.search(s):
        print(' '.join(s.split()[0:-1]))