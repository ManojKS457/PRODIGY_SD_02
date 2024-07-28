import random

def guess_number_game():
  
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    
    while not guessed_correctly:
     
        guess = input("Enter your guess: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
            print(f"It took you {attempts} attempts to guess the number.")

guess_number_game()
