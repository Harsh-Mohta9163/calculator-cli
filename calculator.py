class Calculator:
    """Simple Calculator with basic operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b"""
        return a ** b

def main():
    """CLI interface for the calculator"""
    calc = Calculator()
    print("=" * 40)
    print("Simple Calculator CLI")
    print("=" * 40)
    print("Operations: add, subtract, multiply, divide, power, quit")
    
    while True:
        operation = input("\nEnter operation: ").lower().strip()
        
        if operation == 'quit':
            print("Goodbye!")
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide', 'power']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if operation == 'add':
                result = calc.add(a, b)
            elif operation == 'subtract':
                result = calc.subtract(a, b)
            elif operation == 'multiply':
                result = calc.multiply(a, b)
            elif operation == 'divide':
                result = calc.divide(a, b)
            elif operation == 'power':
                result = calc.power(a, b)
            
            print(f"Result: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
