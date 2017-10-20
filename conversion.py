#abbreviations
#MI = miles
#KM = kilometers
#F = fahrenheit
#C = celsius
#G = gallons
#L = liters
#LB = pounds
#KG = kilograms
#IN = inches
#CM = centimeters

#conversions
#1MI = KM/1.6
#C = (F-32)*5/9
#1G = L/3.9
#1LB = KG/0.45
#1IN = CM/2.54

#1KM = MI/0.625
#F = (C*9/5)+32
#1L = 3.9*G
#1KG = LB/2.22
#1CM = 2.54*IN

#variables
MI = 1.0
KM = 1.0
F = 1.0
C = 1.0
G = 1.0
L = 1.0
LB = 1.0
KG = 1.0
IN = 1.0
CM = 1.0

#defaults
program = 'run'


#program start
print('Hello.' + '\n' + "If you would like to convert from metric to imperial, please enter 'metric'." + '\n' + "If you would like to convert from imperial to metric, please enter 'imperial'.")
while program=='run':        
    #system selection
    selection1 = str(input('Convert from metric or imperial?: '))
    if selection1=='metric':
        print('Would you like to convert kilometers, Celsius, liters, kilograms, or centimeters?')
                
    elif selection1=='imperial':
        print('Would you like to convert miles, Fahrenheit, gallons, pounds, or inches?')
    else:
        print('Invalid input. Please attempt to enter a unit for conversion.')
                    
    #unit selection
    selection2 = str(input('I would like to convert: '))

    #kilometers to miles
    if selection2=='kilometers':
        KM = float(input('Please enter the number of kilometers: '))
        MI = KM/1.6
        print(KM, 'kilometers is approxiamately equal to', format(MI, '.2f'), 'miles.')

    #Celsius to Fahrenheit
    elif selection2=='Celsius' or selection2=='celsius':
        C = float(input('Please enter the temperature in Celsius: '))
        F = (C*9/5)+32
        print(C, 'degrees Celsius is approxiamately equal to', format(F, '.2f'), 'degrees Fahrenheit.')

    #liters to gallons
    elif selection2=='liters':
        L = float(input('Please enter the number of liters: '))
        G = L/3.9
        print(L, 'liters is approxiamately equal to', format(G, '.2f'),'gallons.')
                        
    #kilograms to pounds
    elif selection2=='kilograms':
         KG = float(input('Please enter the number of kilograms: '))
         LB = KG/0.45
         print(KG, 'kilograms is approxiamately equal to', format(LB, '.2f'), 'pounds.')

    #centimeters to inches
    elif selection2=='centimeters':
        CM = float(input('Please enter the number of centimeters: '))
        IN = CM/2.54
        print(CM, 'centimeters is approxiamately equal to', format(IN, '.2f'), 'inches.')

    #miles to kilometers
    elif selection2=='miles':
        MI = float(input('Please enter the number of miles: '))
        KM = MI/0.625
        print(MI, 'miles is approxiamately equal to', format(KM, '.2f'), 'kilometers.')

    #Fahrenheit to Celsius
    elif selection2=='Fahrenheit' or selection2=='fahrenheit':
        F = float(input('Please enter the temperature in Fahrenheit: '))
        C = (F-32)*5/9
        print(F, 'degrees Fahrenheit is approxiamately equal to', format(C, '.2f'), 'degrees Celsius.')

    #gallons to liters
    elif selection2=='gallons':
        G = float(input('Please enter the number of gallons: '))
        L = G*3.9
        print(G, 'gallons is approxiamately equal to', format(L, '.2f'), 'liters.')

    #pounds to kilograms
    elif selection2=='pounds':
        LB = float(input('Please enter the number of pounds: '))
        KG = LB/2.22
        print(LB, 'pounds is approxiamately equal to', format(KG, '.2f'), 'kilograms.')

    #inches to centimeters
    elif selection2=='inches':
        IN = float(input('Please enter the number of inches: '))
        CM = IN*2.54
        print(IN, 'inches is approxiamately equal to', format(CM, '.2f'), 'centimeters.')

    else:
        print('Invalid submission. Please try again.')

    selection3 = str(input('Would you like to make another conversion?' + '\n' + 'Please enter yes or no: '))
    if selection3=='yes':
         program = 'run'
    else:
        program = 'end'
        print('Goodbye.')
