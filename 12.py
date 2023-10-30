# Write python program that user to enter only odd numbers, else will raise an exception.
while True:
    try:
        user_input = int(input("Enter an odd number: "))
        if user_input % 2 == 0:
            raise ValueError("Even number entered. Please enter an odd number.")
        break 
    except ValueError as e:
        print(e)

print(f"You entered an odd number: {user_input}")
 