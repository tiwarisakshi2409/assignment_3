# Write a Python program to read an entire text file.
file_path = 'path_to_your_file.txt' 

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
