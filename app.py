def login(username, password):
    """Validate user login"""
    if username == "admin" and password == "secret":
        return {"status": "success", "message": "Login successful"}
    return {"status": "failed", "message": "Invalid credentials"}

def calculate_sum(numbers):
    """Calculate sum of numbers"""
    if not numbers:
        return 0
    return sum(numbers)

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0
def multiply(a, b):
    return a * b
