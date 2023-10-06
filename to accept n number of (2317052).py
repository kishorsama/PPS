#to accept n number from users. Compute and display maximum in list, minimum in list, sum and average of numbers.


#take total number of input from user
length=int(input('How many numbers you want to enter? : '))

#make a blank list
list1=[]

#use for loop in range of length
for i in range (length):
    #take each input corresponding to total number of input
    Number= int(input('Enter a number: '))
    #add each element to end of list
    list1.append(Number)
#just a space
print(" ")

#calculate summation of entered numbers
addition=sum(list1)

#calculate max number from entered numbers
max_num=max(list1)

#calculate min number from entered numbers
min_num=min(list1)

#calculate average of from entered numbers
average=addition/length

#show entered numbers
print('Entered number are = '),
print(list1)

#show addition of numbers
print('Summation of entered number = '),
print(addition)

#show maximum number
print("Maximum number from entered number = "),
print(max_num)

#show minimum number
print('Minimum number from entered number = '),
print(min_num)

#show average of numbers
print('Average of entered number = '),
print(average)
