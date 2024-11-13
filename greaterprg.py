def main():
    # Input: first number
    num1 = float(input("Enter the first number: "))
    
    # Input: second number
    num2 = float(input("Enter the second number: "))
    
    # Find the greatest number
    if num1 > num2:
        print(f"The greatest number is: {num1}")
    elif num2 > num1:
        print(f"The greatest number is: {num2}")
    else:
        print("Both numbers are equal.")

if __name__ == "__main__":
    main()
