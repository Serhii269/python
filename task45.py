class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle(
            self.width + other.width,
            self.height + other.height
        )

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"
    
r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)

r3 = r1 + r2

assert r3.width == 6
assert r3.height == 8
assert r3.get_square() == 48

print(r3)  
print("OK")