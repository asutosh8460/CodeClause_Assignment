import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiation")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
elif choice in ['6']:
    num1 = float(input("Enter a number: "))
elif choice in ['7', '8', '9']:
    num1 = float(input("Enter an angle in degrees: "))
else:
    print("Invalid input")
    exit()

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", power(num1, num2))
elif choice == '6':
    print("Result:", square_root(num1))
elif choice == '7':
    print("Sine:", sin(num1))
elif choice == '8':
    print("Cosine:", cos(num1))
elif choice == '9':
    print("Tangent:", tan(num1))
