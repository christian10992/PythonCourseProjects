# Program to convert Euros to US Dollars, or vice versa
#    1 euro = 1.14 US dollars

# constants
EUROS_TO_DOLLARS = 1
DOLLARS_TO_EUROS = 2
QUIT_CHOICE = 3

def main():
    #initialize variables
    choice = 0
    euros = 0.0
    dollars = 0.0
    
    while choice != QUIT_CHOICE:
        # display the menu
        display_menu()

        # get user_selecetion
        choice = int(input('Enter your choice: '))
    

        # perform selections
        if choice == EUROS_TO_DOLLARS:
            # Convert euros to dollars
            try:
                euros, dollars = eurosToDollars()
            except ValueError:
                print('The number you enter must be a valid number.')
                print()
            else:
                print('$',format(euros, '.2f'),' euros is $', format(dollars, '.2f'),' US dollars', sep='')
                print()

        elif choice == DOLLARS_TO_EUROS:
            # Convert dollars to euros
            try:
                dollars, euros = dollarsToEuros()
            except ValueError:
                print('The number you enter must be a valid number.')
                print()
            else:
                print('$',format(dollars, '.2f'),' US dollars is $', format(euros, '.2f'),' euros', sep='')
                print()
        elif choice != EUROS_TO_DOLLARS and choice != DOLLARS_TO_EUROS and choice != QUIT_CHOICE:
            print('Invalid selection.')    
            print()
    print('Goodbye')
    
# convert euros to dollars
def eurosToDollars():
    euros = float(input('Please input the number of euros: '))
    print()
    while euros < 0:
        print('Number of euros must be non-negative')
        print()
        euros = float(input('Please input the number of euros: '))
        print()
    dollars = euros * 1.14
    return euros, dollars
    
# convert dollars to euros
def dollarsToEuros():
    dollars = float(input('Please input the number of US dollars: '))
    print()
    while dollars < 0:
        print('Number of US dollars must be non-negative')
        print()
        dollars = float(input('Please input the number of US dollars: '))
        print()
    euros = dollars / 1.14
    return dollars, euros

# display the menu
def display_menu():
    print(' MENU ')
    print('1) Euros to Dollars')
    print('2) Dollars to Euros')
    print('3) Quit')
    print()
main()
