# Write a Python program to count the frequency of words in a file. 
import string

def count_word_frequency(filename):
    try:
        word_frequency = {}
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                words = [word.strip(string.punctuation) for word in words]
                
                for word in words:
                    word = word.lower()  
                    if word:
                        if word in word_frequency:
                            word_frequency[word] += 1
                        else:
                            word_frequency[word] = 1
        return word_frequency
    except FileNotFoundError:
        return None 
    except Exception as e:
        print(f"An error occurred: {e}")
        return None 

file_name = input("Enter the name of the text file: ")

result = count_word_frequency(file_name)

if result is None:
    print(f"File '{file_name}' does not exist or an error occurred while reading the file.")
else:
    print("Word Frequency in the file:")
    for word, frequency in result.items():
        print(f"{word}: {frequency}")
