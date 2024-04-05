answer_c = input('Has the item broken down on its own y/n? ')
if answer_c == 'y':
    print('You can get a refund')
answer_a = int(input('How many days ago have you purchased the item? ') )
answer_b = input('Have you used the item at all y/n? ')
if answer_a <10 and answer_b == 'n' or answer_c == 'y':
    print('You can get a refund')
else:
    print('You cannot get a refund')
        
 
  