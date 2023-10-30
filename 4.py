# Write a Python program to read last n lines of a file
def read_last_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()[-n:]
        for line in lines:
            print(line.strip())

read_last_lines('file.txt', 5)
