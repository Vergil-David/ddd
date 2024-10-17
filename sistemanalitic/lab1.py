import math

def f1(x):
    return 2 + 0.5 * math.exp(x)

def f2(x):
    return 8 + x**3

def main():
    try:
        # Введення меж для x
        x1 = float(input("Крок 1: Введіть початкове значення x1: "))
        x2 = float(input("Крок 1: Введіть кінцеве значення x2: "))
        # Обмеження
        F1 = float(input("Крок 1: Введіть порогове значення F1: "))
        F2 = float(input("Крок 1: Введіть порогове значення F2: "))
        step = 0.1

        print("\nКрок 2: Створення вектора значень x та таблиці функцій f1(x) та f2(x)")
        # Створення вектора значень x
        x_values = [x1 + i * step for i in range(int((x2 - x1) / step) + 1)]
        # Створення таблиці значень
        table = [(x, f1(x), f2(x)) for x in x_values]
        
        print("x\t\tf1(x)\t\tf2(x)")
        for x, y1, y2 in table:
            print(f"{x:.2f}\t\t{y1:.2f}\t\t{y2:.2f}")

        print("\nКрок 3: Фільтрація значень за умовами f1(x) <= F1 та f2(x) >= F2")
        # Фільтрація значень
        filtered_values = [(x, f1(x), f2(x)) for x, y1, y2 in table if y1 <= F1 and y2 >= F2]

        if not filtered_values:
            print("Крок 4: За заданими умовами немає паретто-множин.")
            return 1  # Код помилки для відсутності рішень

        print("x\t\tf1(x)\t\tf2(x)\t\tf1/F1\t\tf2/F2\t\tmin\t\tmax")
        # Обчислення та виведення min(f1(x)/F1, f2(x)/F2) та max(f1(x)/F1, f2(x)/F2)
        min_max_values = []
        max_min_values = []

        for x, y1, y2 in filtered_values:
            f1_ratio = y1 / F1
            f2_ratio = y2 / F2
            min_value = min(f1_ratio, f2_ratio)
            max_value = max(f1_ratio, f2_ratio)
            
            min_max_values.append((x, min_value))
            max_min_values.append((x, max_value))

            print("{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(
                x, y1, y2, f1_ratio, f2_ratio, min_value, max_value))

        print("\nКрок 5: Пошук оптимальних значень")
        optimal_minmax = max(min_max_values, key=lambda item: item[1], default=(None, float('-inf')))
        optimal_maxmin = min(max_min_values, key=lambda item: item[1], default=(None, float('inf')))

        if optimal_minmax[0] is not None:
            print("MinMax (максимум мінімумів): x = {:.2f}, значення = {:.2f}".format(optimal_minmax[0], optimal_minmax[1]))
        else:
            print("Не знайдено MinMax значення.")

        if optimal_maxmin[0] is not None:
            print("MaxMin (мінімум максимумів): x = {:.2f}, значення = {:.2f}".format(optimal_maxmin[0], optimal_maxmin[1]))
        else:
            print("Не знайдено MaxMin значення.")

        print("\nКрок 6: Перевірка на збіг значень для MinMax і MaxMin")
        if optimal_minmax[0] == optimal_maxmin[0]:
            print("\nОптимальне рішення знайдено: x = {:.2f}".format(optimal_minmax[0]))
        else:
            print("\nРаціонального компромісу немає, оскільки MinMax і MaxMin не збігаються.")
        
        return 0  # Код успішного виконання

    except ValueError:
        print("Помилка: Некоректне введення числових значень.")
        return 2  # Код помилки для некоректних значень

# Запуск програми
if __name__ == "__main__":
    main()
