import ast

# Display menu for math operations
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Loop to allow multiple calculations
while True:
    expression = input("Enter a math expression (e.g., 8/4, 6+3, 5-2, 5*5): ")

    # Evaluate the expression
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

    # Ask if the user wants to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
