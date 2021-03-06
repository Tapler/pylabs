# описание себя списком
description = ['Иванов', 'Иван', 'Иванович', 1990, 'male', 180, 80, 'developer']
print(description)

# описание себя при помощи словаря
description = {
    ('Иванов', 'Иван', 'Иванович'):
        {'birthday': 1990,
         'sex': 'male',
         'height': 180,
         'weight': 80,
         'profession': 'developer'}
}
print(description)

# Список занимает меньше памяти, требует меньше времени на обработку, меньше информативности
# Словарь более гибкий вариант - проще изменять, более информативен, но занимает больше памяти
# В данном случае лучше словарь
