#Objective- Get file information (name and size) for files in a single directory
import os


def get_file_info_in_dir(directory): #defining the function to be called


  file_info = {}
  for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
      file_size = os.path.getsize(file_path)
      file_info[filename] = file_size
  return file_info

# Example usage
directory = "."  # Replace with the desired directory path
file_info = get_file_info_in_dir(directory)

if not file_info:
  print(f"Directory not found: {directory}")

for filename, file_size in file_info.items():
  print(f"Filename: {filename}, Size: {file_size} bytes") #    A dictionary with filename as key and file size in bytes as value, 
    # or an empty dictionary if the directory is not found.