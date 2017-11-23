#abbreviations
#mi = miles
#km = kilometers
#f = fahrenheit
#c = celsius
#g = gallons
#l = liters
#lb = pounds
#kg = kilograms
#iN = inches
#cm = centimeters

#initialize variables
#unit variables
mi = float
km = float
f = float
c = float
g = float
l = float
lb = float
kg = float
iN = float
cm = float

#conversion factor variables
#kilometers and miles
kmMiConFact = 0.625
#celsius and fahrenheit
cConFact = 9/5
fConFact = 5/9
#liters and gallons
lGConFact = 3.9
#pounds and kilograms
kgLbConFact = 0.45
#inches and centimeters
cmInConFact = 2.54

#import conversion module
import unitConverterPython_module

def main():
    #defaults
    program = 'run'
    print('Hello.' + '\n' + "If you would like to convert from metric to imperial, please enter 'metric'." + '\n' + "If you would like to convert from imperial to metric, please enter 'imperial'.")
    while program=='run':        
        #system selection
        selection1 = str(input('Convert from metric or imperial?: '))
        while selection1 != 'metric' and selection1 != 'imperial':
            selection1 = str(input('Invalid input. Please choose metric or imperial: '))
        if selection1=='metric':
            print('Would you like to convert kilometers, Celsius, liters, kilograms, or centimeters?')            
        else:
            print('Would you like to convert miles, Fahrenheit, gallons, pounds, or inches?')          
        #unit selection
        selection2 = str(input('I would like to convert: '))
        
        #kilometers to miles
        if selection2=='kilometers':
            km = float(input('Please enter the number of kilometers: '))
            while km<0:
                km = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.kilometersToMi(km, kmMiConFact)
            print(km, 'kilometers is approxiamately equal to', format(total, '.2f'), 'miles.')

        #Celsius to Fahrenheit
        elif selection2=='Celsius' or selection2=='celsius':
            c = float(input('Please enter the temperature in Celsius: '))
            while c>537:
                c = float(input('Invalid selection. Please enter a value less than or equal to 537: '))
            total = unitConverterPython_module.degreesCToF(c, cConFact)
            print(c, 'degrees Celsius is approxiamately equal to', format(total, '.2f'), 'degrees Fahrenheit.')

        #liters to gallons
        elif selection2=='liters':
            l = float(input('Please enter the number of liters: '))
            while l<0:
                l = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.litersToG(l, lGConFact)
            print(l, 'liters is approxiamately equal to', format(total, '.2f'),'gallons.')
                        
        #kilograms to pounds
        elif selection2=='kilograms':
             kg = float(input('Please enter the number of kilograms: '))
             while kg<0:
                 kg = float(input('Invalid selection. Please enter a positive value: '))
             total = unitConverterPython_module.kilogramsToLb(kg, kgLbConFact)
             print(kg, 'kilograms is approxiamately equal to', format(total, '.2f'), 'pounds.')

        #centimeters to inches
        elif selection2=='centimeters':
            cm = float(input('Please enter the number of centimeters: '))
            while cm<0:
                cm = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.centimetersToIn(cm, cmInConFact)
            print(cm, 'centimeters is approxiamately equal to', format(total, '.2f'), 'inches.')

        #miles to kilometers
        elif selection2=='miles':
            mi = float(input('Please enter the number of miles: '))
            while mi<0:
                mi = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.milesToKm(mi, kmMiConFact)
            print(mi, 'miles is approxiamately equal to', format(total, '.2f'), 'kilometers.')

        #Fahrenheit to Celsius
        elif selection2=='Fahrenheit' or selection2=='fahrenheit':
            f = float(input('Please enter the temperature in Fahrenheit: '))
            while f>1000:
                f = float(input('Invalid selection. Please enter a value less than or equal to 1000: '))
            total = unitConverterPython_module.degreesFToC(f, fConFact)
            print(f, 'degrees Fahrenheit is approxiamately equal to', format(total, '.2f'), 'degrees Celsius.')

        #gallons to liters
        elif selection2=='gallons':
            g = float(input('Please enter the number of gallons: '))
            while g<0:
                g = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.gallonsToL(g, lGConFact)
            print(g, 'gallons is approxiamately equal to', format(total, '.2f'), 'liters.')

        #pounds to kilograms
        elif selection2=='pounds':
            lb = float(input('Please enter the number of pounds: '))
            while lb<0:
                lb = float(input('Invalid selection. Please enter a positive value: '))
            total = unitConverterPython_module.poundsToKg(lb, kgLbConFact)
            print(lb, 'pounds is approxiamately equal to', format(total, '.2f'), 'kilograms.')

        #inches to centimeters
        elif selection2=='inches':
            iN = float(input('Please enter the number of inches: '))
            while iN<0:
                iN = float(input('Invalid selection. Please enter a positive value: '))
            unitConverterPython_module.inchesToCm(iN, cmInConFact)
            print(iN, 'inches is approxiamately equal to', format(total, '.2f'), 'centimeters.')

        else:
            print('Invalid submission. Please try again.')

        #Convert another unit or terminate program
        selection3 = str(input('Would you like to make another conversion?' + '\n' + 'Please enter yes or no: '))
        if selection3=='yes':
             program = 'run'
        else:
            program = 'end'
            print('Goodbye.')

#Call main    
main()
