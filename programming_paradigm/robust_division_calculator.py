def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    # Example usage
    print(safe_divide(10, 2))   # Expected: The result of the division is 5.0
    print(safe_divide(10, 0))   # Expected: Error: Cannot divide by zero.
    print(safe_divide("ten", 2)) # Expected: Error: Please enter numeric values only.
