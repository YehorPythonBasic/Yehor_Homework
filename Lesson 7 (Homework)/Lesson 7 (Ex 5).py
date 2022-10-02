import random

# Создаем список с помощью рандома от 1 до 100 с длиной в 5
my_list = [random.randint(1, 100) for i in range(5)]

# Вывод созданного списка
print('Созданный список', my_list)

# Удаление и сохранение элемента из списка под индексом 0
value = my_list.pop(0)

# Добавление удаленного элемента в список
my_list.append(value)

# Вывод
print('Переработанный список', my_list)