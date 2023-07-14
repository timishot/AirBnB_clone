#!/usr/bin/python3

def greet(name):
    """Print a personalized greeting"""
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def main():
    """Main function."""
    name = input("Enter your name: ")
    greet(name)
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print(f"The average is: {average}")


if __name__ == "__main__":
    main()
