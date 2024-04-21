import os

def get_file_info(directory):
  file_data = []
  for root, _, files in os.walk(directory):
    for filename in files:
      file_path = os.path.join(root, filename)
      if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        file_data.append({"filename": filename, "size": file_size})
  return file_data

# Example usage
directory = "."  # Change this to the desired directory
file_data = get_file_info(directory)

# Access information from the list of dictionaries
for file_info in file_data:
  print(f"Filename: {file_info['filename']}, Size: {file_info['size']} bytes")
