#this program will display an inverted right triangle with a base of 10

for r in range(10):
    for c in range(10-r):
        print('*', end='')
    print()
