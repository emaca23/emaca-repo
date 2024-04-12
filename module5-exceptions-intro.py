if True:
    print('hooray!')
#
#

#excpetions- event that occurs during the execution of a program that disrupts the normal flow of the program instructions.

#handle exceptions with this:

try:
   value = int(input('Enter an integer: '))
   print('The inverse of', value, 'is', 1/value)
except ValueError:
   print('You did not provide a number, so  i will not calculate the inverse')
except ZeroDivisionError:
   print('You provided 0 and division by 0 is not possible, sorry')
except:
   print('something strange happened here, sorry')

#2 errors can result in using 0.  zero division error and value error