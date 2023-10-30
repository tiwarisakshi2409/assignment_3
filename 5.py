# Write a Python program to read a file line by line and store it into a list
file = open('file.txt', 'r')
lines = []

for line in file:
    lines.append(line.strip()) 

file.close()

print(lines)
