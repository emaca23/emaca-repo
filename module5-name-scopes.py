#shadowing- python sees temporary variables with different values
#global variables can be the same name as other variables
#can use global in definitions- instructs to not use shadowing
#using global can do more harm than good, so try to avoid using it
#

def show_truth():
    mysterious_var.append ('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)