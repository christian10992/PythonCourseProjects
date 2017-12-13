# This program will allow a user to enter the rainfall per month in inches.
# It will then tell them the average, total, minimum, and maximum rainfalls.

def main():
    rainfall = []
    rainfall = getRainfall(rainfall)
    displayAverage(rainfall)
    displayTotal(rainfall)
    displayMinMax(rainfall)


def getRainfall(rainfall):
    for x in range (1, 13):
        rainForMonth = float(input('Enter the rain in inches for month #' + str(x) + ': '))
        rainfall.append(rainForMonth)
    print('\n')
    return rainfall


def displayAverage(rainfall):
    avg = sum(rainfall)/12
    print('The average rainfall is', format(avg, '.2f'), 'inches per month.')


def displayTotal(rainfall):
    total = sum(rainfall)
    print('The total rainfall for the year is', total, 'inches.')


def displayMinMax(rainfall):
    print('The highest month had', max(rainfall), 'inches.')
    print('The lowest month had', min(rainfall), 'inches.')


main()
