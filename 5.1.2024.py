import os # allows us to with with the os

cwd = os.getcwd() #current working directory path and stores it as cwd

files = os.listdir()


for file in files:
    file_size = os.path.getsize(file)
    print(f' {file}: {file_size} bytes')
    
  