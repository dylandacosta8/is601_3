from typing import List

class Calculator:
    history: List[str] = []

    def __init__(self) -> None:
        pass
    
    def add(self, a: float, b: float) -> float:
        result = a + b
        self._add_to_history(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._add_to_history(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._add_to_history(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._add_to_history(f"Divide: {a} / {b} = {result}")
        return result

    def _add_to_history(self, entry: str) -> None:
        Calculator.history.append(entry)

    @classmethod
    def get_history(cls) -> List[str]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @staticmethod
    def validate_inputs(a: float, b: float) -> bool:
        return isinstance(a, (int, float)) and isinstance(b, (int, float))

