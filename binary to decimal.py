#take input from user as binary number
binary_number=str(input('Enter a binary number ex. 1010: '))

#adding input in list
list1=list(binary_number)

#reverse the list
list1.reverse()
#set sum as zero
sum=0

#using for loop
for i in range(len(list1)):
    sum=sum+int(list1[i])*2**i
print(sum)
