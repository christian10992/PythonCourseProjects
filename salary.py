#this program will allow a person to enter an employee and calculate their pay based off of rate and hours worked
#it will adjust the gross pay according to deductions based on the amount and give a result net pay

#enter initial employee
employeeName = str(input('Enter employee name: '))

#Enter number of hours worked
hoursWorked = float(input('Enter the amount of hours employee worked this pay period: '))
while hoursWorked<10:
    hoursWorked = float(input('Invalid submission. Please enter a value of 10 or greater: '))

#Enter employee's hourly pay rate
hourlyRate = float(input("Enter the employee's hourly rate: $"))
while hourlyRate<9:
    hourlyRate = float(input('Invalid submission. Please enter a value of 9 or greater: '))

#Calculate gross pay
grossPay = hoursWorked * hourlyRate

#Calculate deductions
if grossPay<4000:
    taxDeduction = grossPay*.12
    socialSecurity = grossPay*.04
    medicalRate = grossPay*.01
    retirementRate = grossPay*.06
        
elif 4000<=grossPay<8000:
    taxDeduction = grossPay*.20
    socialSecurity = grossPay*.07
    medicalRate = grossPay*.03
    retirementRate = grossPay*.06

elif 8000<=grossPay<16000:
    taxDeduction = grossPay*.30
    socialSecurity = grossPay*.09
    medicalRate = grossPay*.05
    retirementRate = grossPay*.06
else:
    taxDeduction = grossPay*.38
    socialSecurity = grossPay*.11
    medicalRate = grossPay*.07
    retirementRate = grossPay*.06
        
#Calculate net pay
netPay = grossPay - taxDeduction - socialSecurity - medicalRate - retirementRate

#Print results
print('')
print('Summary of monthly period for ', employeeName, ':', sep='')
print('')
print('Gross Wage' + '\t \t' + '$',format(grossPay, '.2f'), sep='')
print('Tax Deductions' + '\t \t' + '-$',format(taxDeduction, '.2f'), sep='')
print('Social Security' + '\t \t' + '-$',format(socialSecurity, '.2f'), sep='')
print('Medical Deduction' + '\t' + '-$',format(medicalRate, '.2f'),sep='')
print('Retirement Plan' + '\t \t' + '-$',format(retirementRate, '.2f'),sep='')
print('\t \t \t' + '--------')
print('Net Pay' + '\t \t \t' + '$',format(netPay, '.2f'),sep='')
