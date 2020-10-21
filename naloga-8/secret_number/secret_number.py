secret = 15

guess = int(input("Guess the secret number (between 1-20): "))

if guess == secret:
    print("Congratulation, you guessed the correct number! ")
else:
    print("Sorry, you didn't guess the correct number! It's not " + str(guess) + "!")

print("Konec programa! ")


