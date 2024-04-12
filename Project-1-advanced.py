#FOUNDATIONAL
#Create a script that generates a list of dictionaries about files in the working directory. Then print the list.
#Push your code to GitHub and include the link in your write up.

#ADVANCED
#Modify the script into a function such that any path can be passed as a parameter.  
#This parameter should be optional and should default to working directory when the variable is not passed. 
#The function should then create the list of dictionaries about files from that path. 
#The function should also return information on files nested in folders (recursive).

# This code creates dictionaries representing files and then deletes 'user' and 'date' keys from them

def path (file_list):
   
path = (['dictionary.py', 'hello_world.py', 'lists.py','README.md','test_name.py'])
    
# Create a dictionary named 'file'
    file = {}
    
    # Add key-value pairs to the 'file' dictionary
    file = {'name': 'dictionary.py', 'user': 'ec2-user', 'size': '600kb', 'date': 'Feb8'}
    
    # Delete the 'user' key from the 'file' dictionary
    del file['user']
    
    # Delete the 'date' key from the 'file' dictionary
    del file['date']
    
    # Print the data type and contents of the 'file' dictionary
    print(type(file), file)
    
    # Repeat the same process for four more files ('hello_world.py', 'lists.py', 'README.md', 'test_name.py')
    file = {'name': 'hello_world', 'user': 'ec2-user', 'size': '108kb', 'date': 'Feb7'}
    del file['user']
    del file['date']
    print(type(file), file)
    
    file = {'name': 'lists.py', 'user': 'ec2-user', 'size': '594kb', 'date': 'Feb8'}
    del file['user']
    del file['date']
    print(type(file), file)
    
    
    file = {'name': 'README.md', 'user': 'ec2-user', 'size': '26kb', 'date': 'Jan31'}
    del file['user']
    del file['date']
    print(type(file), file)
    
    file = {'name': 'test_name.py', 'user': 'ec2-user', 'size': '68kb', 'date': 'Feb7'}
    del file['user']
    del file['date']
    print(type(file), file)