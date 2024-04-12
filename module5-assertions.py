#can raise excceptions by ourselves
#Assertions are assumptions in our program that should always be true.
# Use assertions
    #1 for debugging/testing your code
    #2 for documenting your code
#DO NOT use assertions for
    #1 Validate user input with assertions
    #2 Handle AssertionErrors in try..except
def calculate_inverse(number):
    assert (number != 0), 'Got 0 as a number!'
    return 1/number
calculate_inverse(0)