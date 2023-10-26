print('''   Addition = 1
            subtraction = 2
            multiplication = 3
            division = 4''')

first=float(input('Enter the first number: '))
second=float(input('Enter the second number: '))
opr=input("enter the operation you wanna perform: ")

if opr==1:
    print(first+second)
elif opr==2:
    print(first-second)
elif opr==3:
    print(first*second)
elif opr==4:
    print(first/second)
else:
    print("Something went wrong. Try again later...")