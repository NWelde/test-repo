#simple calculator
try :
    x = int(input('Enter num: '))
    y =int(input('enter num2: '))
except :
   print('i want numbers dumbass, try again')   
   x = int(input('Enter num: '))
   y =int(input('enter num2: '))

try :
    z =str(input('Enter operator: '))
except:
 print('do you not know what an operator is?, try again man.')    
 z =str(input('Enter operator: '))

if z == '+' :
 print(x+y)
elif z == '-' :
   print(x-y)
elif z == '*' :
 print(x*y)
elif z == '/' :
 print(x/y)



