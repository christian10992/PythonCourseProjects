# Program to convert Feet to miles

# initialize variables
feet = 0.0
miles = 0.0


def main():
    #default
    program = 'run'
    # get the number of feet
    feet = float(input('Please input the number of feet: '))
    # validate the feet
    while program == 'run':
        if feet < 0:
            program = 'run'
            print('Number of feet cannot be negative.')
            feet = float(input('Please input the number of feet: '))
        else:
            print(feet)
            feetToMiles(feet)
            program = 'stop'

def feetToMiles(feet):
    # Calculate and display the corresponding number of miles
    miles = feet / 5280
    print(feet,'feet is', format(miles, '.2f'), 'miles')

main()
