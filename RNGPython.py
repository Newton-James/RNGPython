import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Random Number Generator!")
    print("I will generate a random number between 1 and 100.")
    random_number = generate_random_number()
    print(f"Generated Number: {random_number}")

if __name__ == "__main__":
    main()