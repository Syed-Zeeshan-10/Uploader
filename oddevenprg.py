def check_even_odd():
    # Input: number from the user
    number = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

if __name__ == "__main__":
    check_even_odd()