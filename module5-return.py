def get_average (input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
#typically write functions to return a value, but not print it in output

print('The average is: ', get_average ([5.0, 3.5, 7.8, 9.9, 10.0]))

#return will end the function, without returning anything of value
#
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
#
#
#
def get_average (input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')
get_average([2])
#
def is_fist_last_equal (number_list):
    if (number_list [0] == number_list [-1]):
        return True
    else:
        return False
print(is_fist_last_equal([10, 20, 30, 40, 10]))
print(is_fist_last_equal([10, 20, 30, 40, 50]))
#
#
def is_fist_last_equal (number_list):
    if len(number_list) == 0:
        return
    if (number_list [0] == number_list [-1]):
        return True
    else:
        return False
print(is_fist_last_equal([10, 20, 30, 40, 10]))
print(is_fist_last_equal([]))
