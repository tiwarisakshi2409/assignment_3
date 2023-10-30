# Write a Python program to write a list to a file.
def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = [1, 2, 3, 4, 5]

file_name = "Python.txt"

write_list_to_file(file_name, my_list)
