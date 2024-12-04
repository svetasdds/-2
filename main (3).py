import math

# Функція для знаходження середнього числа
def find_middle(a, b, c):
    if (a < b < c) or (c < b < a):
        return b
    elif (b < a < c) or (c < a < b):
        return a
    else:
        return c

# Функція перевірки належності точки до нижнього лівого сектора (29 варіант)
def is_in_black_area(x, y, r):
    return x**2 + y**2 <= r**2 and y <= 0 and x <= 0

# Функція для обчислення суми
def calculate_sum(x, max_terms=100, tolerance=1e-6):
    total_sum = 0  # Початкова сума
    for n in range(1, max_terms + 1):
        term = math.factorial(2 + n) / (x**n * 2**(2 * n + 1))  # Обчислення члена ряду
        total_sum += term
        # Перевірка на збіжність
        if abs(term) < tolerance:
            break
    return total_sum

# Частина 1: Знаходження середнього числа
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

middle = find_middle(a, b, c)
print(f"Середнє число: {middle}")

# Частина 2: Перевірка точок
r = float(input("Введіть радіус кола r: "))
n = int(input("Введіть кількість точок: "))

points = []
for i in range(n):
    x, y = map(float, input(f"Введіть координати точки {i+1} (x, y): ").split())
    points.append((x, y))

count = 0
for x, y in points:
    if is_in_black_area(x, y, r):
        count += 1

print(f"Кількість точок, що потрапляють у нижній лівий сектор: {count}")

# Частина 3: Обчислення суми ряду
x = float(input("Введіть значення x для обчислення суми ряду: "))
max_terms = int(input("Введіть максимальну кількість членів ряду: "))
tolerance = float(input("Введіть точність (tolerance): "))

result = calculate_sum(x, max_terms, tolerance)
print(f"Сума ряду: {result}")
