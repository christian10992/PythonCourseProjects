# this program will calculate revenue based on ticket prices at each level

# initialize variables
matinee = 0
regular = 0
deluxe = 0
matineeCost = 8
regularCost = 9
deluxeCost = 15

def main ():
    #default
    program = 'run'
    #get input for tickets sold
    matinee = int(input('Enter the number of matinee tickets sold: '))
    regular = int(input('Enter the number of regular tickets sold: '))
    deluxe = int(input('Enter the number of deluxe tickets sold: '))
    print('')
    #validate input
    while program == 'run':                 
        if matinee<0 or regular<0 or deluxe<0:
            print('Error. Please check inputs. Each must be a positive integer or 0.')
            print('')
            matinee = int(input('Enter the number of matinee tickets sold: '))
            regular = int(input('Enter the number of regular tickets sold: '))
            deluxe = int(input('Enter the number of deluxe tickets sold: '))
            print('')
        else:
            calculateSales(matinee, regular, deluxe)
            program = 'stop'

def calculateSales(matinee, regular, deluxe):
    #calculate ticket sales
    matineeTotal = matinee*matineeCost
    regularTotal = regular*regularCost
    deluxeTotal = deluxe*deluxeCost
    #calculate grand total
    totalSales = matineeTotal + regularTotal + deluxeTotal
    #print results
    print('Matinee total' + '\t\t$', format(matineeTotal, '.2f'),sep='')
    print('Regular total' + '\t\t$', format(regularTotal, '.2f'), sep='')
    print('Deluxe total' + '\t\t$', format(deluxeTotal, '.2f'), sep='')
    print('\t\t\t'+'--------')
    print('Grand total' + '\t\t$', format(totalSales, '.2f'), sep='')

main()
