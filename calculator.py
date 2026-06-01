class Calculator:
    """Simple calculator with core arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of two numbers.

        Raises:
            ValueError: If the divisor is zero.
        """
        if b == 0:
            raise ValueError("Divisor cannot be zero.")
        return a / b


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(2, 3))
    print(calculator.subtract(10, 4))
    print(calculator.multiply(5, 6))
    print(calculator.divide(20, 5))
