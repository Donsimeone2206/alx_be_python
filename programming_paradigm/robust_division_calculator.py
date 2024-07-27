# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling for division by zero and non-numeric inputs."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division and return the result
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

