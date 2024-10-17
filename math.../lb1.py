import random

n = int(input("Введіть кількість табуляцій: "))

P = 0.25

count = 0

for _ in range(n):
    rand_num = random.randint(0, 100) 
    if rand_num <= P * 100:  
       count += 1  

percentage = (count / n) * 100

print(f"Процент попадань в інтервал: {percentage}%")
