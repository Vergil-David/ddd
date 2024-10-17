import random

# Значення дискретної випадкової величини
values = [30, 25, 15, 34]

# Відповідні ймовірності
probabilities = [0.3, 0.25, 0.15, 0.3]

# Кількість симуляцій (наприклад, 1000)
n = int(input("Введіть кількість симуляцій: "))

# Генерація результатів
results = random.choices(values, probabilities, k=n)

# Підрахунок кількості випадків для кожного значення
for value in values:
    count = results.count(value)
    percentage = (count / n) * 100
    print(f"Значення {value} випадало {count} разів ({percentage:.2f}%)")

