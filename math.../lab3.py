import numpy as np
import matplotlib.pyplot as plt

# Параметри
alpha = 0.05
time_start = 0
time_end = 40
tau = 4

# Функція математичного сподівання
def m(t):
    return 3 * 10**3 * np.sin(0.2 *t )

# Кореляційна функція
def k(t):
    D_t = 20.5 * t
    return D_t * np.exp(-alpha * tau)

# Моделювання частоти обертання
t_values = np.arange(time_start, time_end + tau, tau)
m_values = m(t_values)
k_values = k(t_values)

# Генерування випадкової функції на основі математичного сподівання та кореляційної функції
random_values = np.random.normal(m_values, np.sqrt(k_values))

# Візуалізація результату
plt.plot(t_values, random_values, label="Частота обертання")
plt.xlabel('Час (с)')
plt.ylabel('Частота обертання')
plt.title('Моделювання частоти обертання валу електродвигуна')
plt.grid(True)
plt.legend()
plt.show()
