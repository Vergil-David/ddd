# Modified code to print each step clearly and descriptively

import numpy as np

# Define the functions f12 and f21
def f12(x1, x2):
    return (2 * (x1**2) - 4 * x1 + 18) * (6 * (x2**2) - 26 * x2 + 29)

def f21(x1, x2):
    return (-6 * (x2**2) + 26) * (-3 * (x1**2) + 4 * x1 + 6)

# Define the delta function as the absolute difference between f_i and f*_i
def delta(f_val, f_star):
    return abs(f_val - f_star)

# Set up a grid of values for x1 and x2 (based on your example from the file)
x1_values = np.arange(0, 2.01, 0.5)
x2_values = np.arange(0, 2.01, 0.5)

# Define target (optimal) values f*_12 and f*_21 from the conditions
f_star_12 = 522  # Example value from the data
f_star_21 = 162  # Example value from the data

# Variables to track the optimal values of x1, x2 and minimum delta
min_delta = float('inf')
optimal_x1, optimal_x2 = None, None

print("Починаємо пошук оптимальних значень для x1 і x2...")
print(f"Цільові значення: f*_12 = {f_star_12}, f*_21 = {f_star_21}")

# Iterate over all combinations of x1 and x2 values to find the optimal
for x1 in x1_values:
    for x2 in x2_values:
        # Step 1: Calculate f12 and f21 for the current pair of x1, x2
        f12_val = f12(x1, x2)
        f21_val = f21(x1, x2)
        print(f"\nДля x1 = {x1:.2f}, x2 = {x2:.2f}:")
        print(f"  Обчислено f12(x1, x2) = {f12_val:.2f}")
        print(f"  Обчислено f21(x1, x2) = {f21_val:.2f}")

        # Step 2: Calculate the deltas for f12 and f21
        delta_12 = delta(f12_val, f_star_12)
        delta_21 = delta(f21_val, f_star_21)
        print(f"  Відхилення delta_12 = |f12 - f*_12| = {delta_12:.2f}")
        print(f"  Відхилення delta_21 = |f21 - f*_21| = {delta_21:.2f}")

        # Step 3: Sum the deltas
        total_delta = delta_12 + delta_21
        print(f"  Сума відхилень Δ = delta_12 + delta_21 = {total_delta:.2f}")

        # Step 4: Check if this is the minimum total delta
        if total_delta < min_delta:
            min_delta = total_delta
            optimal_x1, optimal_x2 = x1, x2
            print(f"  Знайдено нові оптимальні значення: x1 = {optimal_x1}, x2 = {optimal_x2}, Δ = {min_delta:.2f}")

# Final result
print("\nПОШУК ЗАВЕРШЕНО")
print(f"Оптимальні значення: x1 = {optimal_x1}, x2 = {optimal_x2}, мінімальна сума відхилень Δ = {min_delta:.2f}")
