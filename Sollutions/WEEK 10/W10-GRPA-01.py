class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    def multiply(self) -> int:
        return self.a * self.b

    def subtract(self) -> int:
        return self.a - self.b

    def quotient(self) -> float:
        return self.a // self.b

    def remainder(self) -> int:
        return self.a % self.b
    