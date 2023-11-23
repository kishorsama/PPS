number=int(input('Enter a number: '))
reversing=0
while(number>0):
    digit_separation=number%10
    reversing=reversing*10+digit_separation
    number=number//10
print(reversing)