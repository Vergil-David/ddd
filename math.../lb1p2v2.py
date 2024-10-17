import random


n = int(input("Введіть кількість ітерацій: "))

events = ['x1', 'x2', 'x3', 'x4']

results = []

for _ in range(n):
    random_number = random.randint(1, 100)
    
    if 0 <= random_number <= 30:
        results.append('x1')
    elif  random_number <= 55:
        results.append('x2')
    elif  random_number <= 70:
        results.append('x3')
    else:
        results.append('x4')

for event in events:
    count = results.count(event)
    percentage = (count / n) * 100
    print(f"Подія {event} траплялась {count} разів ({percentage:.2f}%)")
