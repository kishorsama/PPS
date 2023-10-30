print('''   Addition = 1
   subtraction = 2
   multiplication = 3
   division = 4
   exponent = 5
   factorial = 6''')

#enter first number
first=int(input('Enter the first number: '))

#enter second number
second=float(input('Enter the second number: '))

#select operator
opr=input("enter the operation you wanna perform: ")

#set fact=1
fact=1

#condition for addition of 2 numbers
if opr==1:
    #output of addition of 2 numbers
    print(first+second)

#condition for subtraction of 2 numbers
elif opr==2:
    #output of subtraction of 2 numbers
    print(first-second)

#condition for multiplication of 2 numbers
elif opr==3:
    #output of multiplication of 2 numbers
    print(first*second)

#condition for division of 2 numbers    
elif opr==4:
    #output of division of 2 numbers
    print(first/second)

#condition for exponent of a number    
elif opr==5:
    #output of exponent of a number
    print(first**second)

#condition for factorial of a number
elif opr==6:
    #using for loop 
    for k in range (1,first+1):
        #multiplying each number less than equal to given number
        fact=fact*k
        #output factorial of given number
        print(fact)

#condition if none of above conditions are satisfied
else:
    #output if none of above condition are satisfied
    print("Something went wrong. Try again later...")