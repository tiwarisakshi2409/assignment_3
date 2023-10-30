# Write a Python program to read a file line by line store it into a variable. 
file = open('filename.txt', 'r')

lines = []
for line in file:
    lines.append(line.strip())

file.close()

for line in lines:
    print(line)
