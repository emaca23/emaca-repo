first = input('enter first number: ')
second = input('enter second number: ')
print('before swapping: ', first, second)
temporary = first
first = second
second = temporary
print('after swapping: ', first, second)

first = input('enter first number: ')
second = input('enter second number: ')
print('before swapping: ', first, second)
first, second = second, first
print('after swapping: ', first, second)