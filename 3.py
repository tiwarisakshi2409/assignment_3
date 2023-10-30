# Write a Python program to read first n lines of a file.  
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

file_path = "file.txt"  
n = 5 

read_first_n_lines(file_path, n)
