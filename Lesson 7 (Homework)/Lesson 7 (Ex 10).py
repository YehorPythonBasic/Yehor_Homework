# Изначальный список
my_list = [1, 2, 3, "11", "22", 33]

# Новый список
new_list = []

# Цикл for который перебирает элементы изначального списка
for i in my_list:

    # Если тип элемента в списке - строка, тогда он добавляется в новый список
    if type(i) == str:
        new_list.append(i)

# Вывод нового списка
print(new_list)