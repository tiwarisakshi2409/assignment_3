# Write a Python program to count the number of lines in a text file
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        return -1 
    except Exception as e:
        print(f"An error occurred: {e}")
        return -2 

file_name = input("Enter the name of the text file: ")

result = count_lines_in_file(file_name)

if result == -1:
    print(f"File '{file_name}' does not exist.")
elif result == -2:
    print("An error occurred while reading the file.")
else:
    print(f"Number of lines in the file '{file_name}': {result}")
