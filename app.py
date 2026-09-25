def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."


def square(a):
    return a * a


result1 = add(5, 3)
result2 = subtract(10, 4)
result3 = multiply(6, 7)
result4 = divide(10, 2)
result5 = square(5)

print("Addition Result:", result1)
print("Subtraction Result:", result2)
print("Multiplication Result:", result3)
print("Division Result:", result4)
print("Square Result:", result5)
