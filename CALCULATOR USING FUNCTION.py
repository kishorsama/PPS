print('''   Addition = 1
   subtraction = 2
   multiplication = 3
   division = 4
   exponent = 5
   factorial = 6''')

def addition (first,second):
    return first+ second
def sub (first, second):
    return first-second
def mul(first, second):
    return first*second
def div(first, second):
    return first/second
def power (first, second):
    return first**second

while True:
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
        print(addition(first,second))

    #condition for subtraction of 2 numbers
    elif opr==2:
        #output of subtraction of 2 numbers``
        print(sub(first,second))
    
    elif opr==3:
        print(mul(first,second))

    elif opr==4:
        print(div(first,second))

    #condition for exponent of a number    
    elif opr==5:
        #output of exponent of a number
        print(power(first,second))

    #condition for factorial of a numberk. 
    elif opr==6:
        #using for loop 
        for k in range (1,first+1):
            #multiplying each number less than equal to given number
            fact=fact*k
            #output factorial of given number
            print(fact)
    conti=int(input('Continue= 1, Exit= 2: '))
    if conti<=0:
        print('See you soon...')
        break

    if conti==1:
        continue

    if conti>=2:
        print('See you soon...')
        break



    #condition if none of above conditions are satisfied
    #else:
    #    #output if none of above condition are satisfied
    #    print("Something went wrong. Try again later...")
