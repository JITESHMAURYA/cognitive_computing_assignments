try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("The result of division is:",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
finally:
    print("This block always executes, whether there was an exception or not.")


try:
    number = float(input("Enter a number: "))
    print("You entered:",number)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
