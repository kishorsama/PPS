#armstrong number

#take a input
number=int(input('Enter a number: '))

#set sum as a variable
sum=0

#copy input number as num
num=number

#set power as length of given number
power=len(str(number))

#while loop
while(number>0):
    
    #take modu;us of given digit
    digit=number%10

    #set sum as given digit to the length of given number
    sum+=digit**power

    #take floor division of number
    number=number//10

#if condition is satisfied    
if(sum==num):
    #print armstrong
    print('Armstrong')

#if condition not satisfied
else:
    #print armweak
    print('Armweak')