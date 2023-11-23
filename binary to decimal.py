binary_number=str(input('Enter a binary number ex. 1010: '))
list1=list(binary_number)
list1.reverse()
sum=0
for i in range(len(list1)):
    sum=sum+int(list1[i])*2**i
print(sum)