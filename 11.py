# Write a Python program to copy the contents of a file to another file
def copy_file(file_txt, destination_file):
    try:
        with open(file_txt, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
        print(f"Contents copied from '{file_txt}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"File '{file_txt}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_txt_name = "file.txt"
destination_file_name = "Python.txt"

copy_file(file_txt_name, destination_file_name)
