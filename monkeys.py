# This program allows the user to input how much food each of three monkeys ate
# during each day on the week and stores it in a 2d list. It will then print
# the list in a tabular form and display the average amount of food each monkey ate 

MONKEYS = 3  # rows
DAYS = 7  # columns


def main():
    # initialize 2d array
    food = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]


    # get amount fo food eaten by monkeys
    getFood(food)

    # display amount of food eaten
    displayFood(food)

    # find the average each monkey ate per week
    averages = calcAverage(food)

    # print averages
    avgM1 = print('Monkey 1 ate an average of ', format(averages[0], '.1f'))
    avgM2 = print('Monkey 2 ate an average of ', format(averages[1], '.1f'))
    avgM3 = print('Monkey 3 ate an average of ', format(averages[2], '.1f'))
    

def getFood(food):
    # User enters amount of food each monkey has eaten. Must be an amount 0 or greater.
    monkeyNumber = 0
    for r in range(MONKEYS):
        monkeyNumber += 1
        dayNumber = 0
        for c in range(DAYS):
            dayNumber += 1
            print('Enter the amount of food monkey #', \
                   monkeyNumber, 'ate on day #', \
                   dayNumber, ':')
            amount = float(input())
            while amount < 0:
                amount = float(input('Amount eaten must be greater than 0: '))
            food[r][c] = amount
    print()


def displayFood(food):
    # prints a header for days, then the amount of food each monkey had each day
    print('\t\tDay 1\t Day 2    Day 3    Day 4    Day 5    Day 6    Day 7')
    monkeyNumber = 0
    for r in range(MONKEYS):
        if r != 0:
            print('\n')
        monkeyNumber += 1
        print('Monkey #', monkeyNumber, ':', end=' ')
        for c in range(DAYS):
            print(format(food[r][c], '8.1f'), end=' ')
    print('\n')

def calcAverage(food):
    averages = []
    for r in range(MONKEYS):
        avg = sum(food[r])/DAYS
        averages.append(avg)
    return averages
        
main()
