from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass(frozen=True)
class Rectangle:
    x: int
    y: int
    width: int
    height: int

class RectangleChain:
    def init(self):
        self.rectangles = []

    def add_rectangle(self, rect: Rectangle):
        self.rectangles.append(rect)

    def update_coordinates(self, old_rect: Rectangle, new_x: int, new_y: int):
        new_rect = Rectangle(new_x, new_y, old_rect.width, old_rect.height)
        self.add_rectangle(new_rect)

    def draw_rectangles(self):
        for rect in self.rectangles:
            plt.gca().add_patch(plt.Rectangle((rect.x, rect.y), rect.width, rect.height, fill=None, edgecolor='r'))
        plt.axis('scaled')
        plt.show()

# Приклад використання
chain = RectangleChain()
rect1 = Rectangle(10, 10, 100, 50)
chain.add_rectangle(rect1)

# Оновлюємо координати, створюючи новий прямокутник
chain.update_coordinates(rect1, 20, 30)

# Виводимо всі прямокутники на екран
chain.draw_rectangles()