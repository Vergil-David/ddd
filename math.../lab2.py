import random
import math
import matplotlib.pyplot as plt

def generate_exponential_random_values(lmbda, n):
    """Generates n exponentially distributed random values with parameter lmbda."""
    if lmbda <= 0:
        raise ValueError("Lambda must be greater than 0")
    if n <= 0:
        raise ValueError("Number of values must be greater than 0")
    
    results = []
    for _ in range(n):
        u = random.random()
        x = -math.log(1 - u) / lmbda
        results.append(x)
    return results

# Parameters
lmbda = 0.2
n = 1000

# Generate exponentially distributed random values
random_values = generate_exponential_random_values(lmbda, n)

# Plotting the histogram
plt.hist(random_values, bins=30, density=True, alpha=0.6, color='b')
plt.title('Exponential Distribution with λ=0.2')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show()