import random

# Set the min and max
min_value = 1
max_value = 99
target_number = random.randint(min_value, max_value)

# Welcome the user
print("Welcome to the number guessing game!")

# The main game loop
guess_count = 0
while True:
    user_guess = int(input("Guess a number between 1 and 99: "))
    guess_count += 1
    if user_guess == target_number:
        print(f"Congratulations! You guessed it right in {guess_count} tries.")
        break
    elif user_guess < target_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
