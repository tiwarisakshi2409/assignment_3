# Write a Python program to append text to a file and display the text.
file = open("filename.txt", "a")

text = input("Enter text to append: ")

file.write(text)

file.close()

file = open("filename.txt", "r")

contents = file.read()

print("Contents of the file:")
print(contents)

file.close()
