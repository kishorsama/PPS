#to accept a student's five marks and compute his/her result.
    #Student is passing if he/she scores marks equal to and above 40 in each course.
    #If student scores aggregate greater than 75%, then the grade is distinguished.
    #If aggregate is 60>= and <75 then the grade of first division.
    #If aggregate is 50>= and <60 then the grade of Second division.
    #If aggregate is 40>= and <50 then the grade of third division.


#input marks obtained in 1st subject
sub1=int(input("Enter your marks of 1st subject: "))
    #fail if 1st subject have less than 35 marks
if sub1<=34:
    print('You failed the exam')
    print('Grade = F')
    exit()
#input marks obtained in 2nd subject
sub2=int(input("Enter your marks of 2nd subject: "))
    #fail if 2nd subject have less than 35 marks
if sub2<=34:
    print('You failed the exam')
    print('Grade = F')
    exit()

#input marks obtained in 3rd subject
sub3=int(input("Enter your marks of 3rd subject: "))
    #fail if 3rd subject have less than 35 marks
if sub3<=34:
    print('You failed the exam')
    print('Grade = F')
    exit()

#input marks obtained in 4th subject
sub4=int(input("Enter your marks of 4th subject: "))
    #fail if 4th subject have less than 35 marks
if sub4<=34:
    print('You failed the exam')
    print('Grade = F')
    exit()

#input marks obtained in 5th subject
sub5=int(input("Enter your marks of 5th subject: "))
    #fail if 5th subject have less than 35 marks
if sub5<=34:
    print('You failed the exam')
    print('Grade = F')
    exit()

#calculate percentage
perc= (sub1+sub2+sub3+sub4+sub5)/5

#black obejct = grade
grade=""

#condition if percentage is equal to or greater than 80, give grade A
#if not then check 2nd condition
#if not then check 3rd conditon
#if not print 4th condition
if perc>=80:
    grade='A'

elif perc>=60:
    grade='B'

elif perc>=35:
    grade='C'
    
else:
    print('You failed the exam')

#print percentage
print("Your percentage is: ", perc)

#print grade
print('And your grade is: ', grade)