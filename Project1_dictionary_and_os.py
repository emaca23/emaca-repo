import os


def get_file_info(directory): #creates a dictionry with with file name and size

  file_info = {} # creates dictionary
  
  for root, _, files in os.walk(directory): #iterates the root for files(outer loop) , os.walk generates the filenames in a directory tree
    
    for filename in files:                  #(inner loop)
      file_path = os.path.join(root, filename) #completes the file path by joining current directory and the file name
      
      if os.path.isfile(file_path): #checks if provided path exists and refers to a regular file
        
        file_size = os.path.getsize(file_path) # retrieve the size of the file and stores it in file_info
        file_info[filename] = file_size
  
  return file_info

directory = "."  # sets the current working directory as directory
file_info = get_file_info(directory)

for filename, file_size in file_info.items(): # for loop that iterates over the file_info dictionary
  print(f"Filename: {filename}, Size: {file_size} bytes")
  
