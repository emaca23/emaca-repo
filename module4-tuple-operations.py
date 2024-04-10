user_data = ('john', 'american', 1964)
print(len(user_data))

user_data = ('john', 'american', 1964)
if 'american' in user_data:
    print('this person comes from the US!')
    
user_data = ('john', 'american', 1964)
for element in user_data:
    print (element)
    
user_data = ('john', 'american', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

#lists are used when we want to use many values of the same data type
#example - male_names = ['Adam', 'Jerry','Mark']
#example- berlin_temps = [13, 17.5, 12.0]

#tuples- used for values of different types that are somehow related and together form bigger data
#example- user_data = ('john', 'american', 1964)
#also used to perform Python operations quicker- like swap operation below
#first = 5
#second = 7
#first, second = second, first