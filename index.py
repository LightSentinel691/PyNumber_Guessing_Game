import random

def get_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    choice = input("Enter 1, 2 or 3: ")
    return {"1": 10, "2": 7, "3": 5}.get(choice, 10)  # Default to Easy if input is invalid

def provide_hint(number):
    hints = []
    if number % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")
    if number % 3 == 0:
        hints.append("The number is divisible by 3.")
    if number % 5 == 0:
        hints.append("The number is divisible by 5.")
    return random.choice(hints)

def update_high_scores(username, attempts_used):
    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{username}: {attempts_used} attempts\n")
    except Exception as e:
        print("Error saving score:", e)

def main():
    print("🎮 Welcome to the Guessing Game!")
    username = input("Enter your username: ")
    max_attempts = get_difficulty()
    number = random.randint(1, 100)
    attempts = 0
    wrong_tries = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess (1–100): "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        attempts += 1
        if guess == number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            update_high_scores(username, attempts)
            break
        elif guess < number:
            print("Too Low!")
        else:
            print("Too High!")

        wrong_tries += 1
        if wrong_tries == 3:
            print("💡 Hint:", provide_hint(number))

        if attempts == max_attempts:
            print(f"❌ Game Over! The number was {number}. Better luck next time.")

if __name__ == "__main__":
    main()
