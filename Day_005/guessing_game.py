print("=========Welcome to the Guessing Game=========")
print("Rules: Guess the number between 1 and 100.")
print("Type '0' to quit")

secret_number = 21
attempts_left = 3

while True:

    while attempts_left > 0:

        user_guess = input("Enter the number: ")
        guess = int(user_guess)

        if guess == 0:
            print("Quit the game.")
            break

        if guess < 1:
            print("Please guess the number between 1 and 100.")
            continue

        if guess > 100:
            print("Please enter the valid number between 1 and 100. the number entered is high")

        if guess == secret_number:
            print("Successfully you have unlocked it, Well Done!")
            attempts_left = 0

        else:
            attempts_left = attempts_left - 1
            print("Incorrect Guess")
            print(f"attempts left :  {attempts_left}")

print("======Game Over======")

while True:

    play_again = input("do you want to play again: (yes/no): ")

    if play_again == "yes":
        print("Ready to play")
        attempts_left = 3

        continue

    else:

        print("Bye")

        break