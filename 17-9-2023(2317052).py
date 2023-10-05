#this code is about calculating in hand salary or gross salary an employee get after all allowance and tax deduction.

#Take input from user
basic_salary=float(input('Enter your CTC: '))
if float(basic_salary) not in range(0, 100000000):
    print('''Entered amount is not applicable
          Try again after 2 minutes... ''')
    exit()

#Value of house rent allowance (HRA)
HRA=0.10*basic_salary

#Value of Travel allowance (TA)
TA=0.05*basic_salary

#Value of providant fund (PF)
PF=0.02*basic_salary

#formula to calculate in hand salary
ihs=(basic_salary+HRA+TA-PF)

#Output
print('Your in hand salary is')
print(ihs),
print('rupees only')