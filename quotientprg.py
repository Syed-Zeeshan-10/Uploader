def main():
    # Input: first number (dividend)
    dividend = float(input("Enter the first number (dividend): "))
    
    # Input: second number (divisor)
    divisor = float(input("Enter the second number (divisor): "))
    
    # Check if the divisor is zero
    if divisor == 0:
        print("Error: Division by zero is not allowed.")
    else:
        # Calculate quotient
        quotient = dividend / divisor
        print("The quotient is:", quotient)

if __name__ == "__main__":
    main()
