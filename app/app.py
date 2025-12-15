def add(a, b):
    """Return the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b


def multiply(a, b):
    """Return the product of two numbers"""
    return a * b


def divide(a, b):
    """Return the division of two numbers"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
