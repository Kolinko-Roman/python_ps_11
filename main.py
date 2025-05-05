# Завдання 1: Оцінки за тест
grades = [85, 60, 90, 70, 55, 100, 40, 78]
high_grades = [grade for grade in grades if grade > 70]
print("Завдання 1 — Високі оцінки:", high_grades)
print("Кількість високих оцінок:", len(high_grades))
print()

# Завдання 2: Список покупок
shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
long_items = [item for item in shopping_list if len(item) > 4]
print("Завдання 2 — Товари з назвою понад 4 символи:", long_items)
print("Кількість таких товарів:", len(long_items))
print()

# Завдання 3: Пошук дубльованих значень
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Завдання 3 — Числа, що повторюються:", duplicates)
