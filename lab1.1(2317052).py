a=float(input('1st language marks: '))
if float(a) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

b=float(input('English marks: '))
if float(b) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

c=float(input('Physics marks: '))
if float(c) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

d=float(input('Chemistry marks: '))
if float(d) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

e=float(input('Math marks: '))
if float(e) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

f=float(input('Optional subject marks: '))
if float(f) not in range(0,100):
    print('''Warning: marks should be in 0 to 100
          try again later...''')
    exit()

k=(a+b+c+d+e+f)
percent=(k/6)
print('You got'),
print(percent),
print('%'),
print('in you exam.')