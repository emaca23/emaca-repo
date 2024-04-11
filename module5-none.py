#function can cause effect, and can return a value
number = input('what is the number?')
print(number)
#
#
print_return = print('Hello World')
print(print_return)
#
#
x = None

if x:
    print("none is true")
elif x is False:
    print("none is false")
else:
    print('none is not true, or false, none is just none')
#
#
x = None
if x is None:
    print('yes')
if x == None:
    print('It does')
#
#
def greet ():
    print('hello')
    
x = greet()
print(x)
