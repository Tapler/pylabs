# 1) поиск самого молодго сотрудника в списке
from datetime import datetime

currentYear = datetime.now().year

employees = [['Сотрудник1', 'м', 1985, 'разработчик'],
             ['Сотрудник2', 'ж', 1993, 'аналитик'],
             ['Сотрудник3', 'ж', 1989, 'тестировщик'],
             ['Сотрудник4', 'м', 1979, 'лид']]

year_of_birth = employees[0][2]
for x in range(1, len(employees)):
    if employees[x][2] > year_of_birth:
        year_of_birth = employees[x][2]
        name = employees[x][0]

print('Самый молодой сотрудник:', name, ', в этом году ему исполняется', currentYear - year_of_birth, 'лет')

# 2) поиск самого молодго сотрудника в словаре
employees_dict = {'Сотрудник1': {'пол': 'м', 'г.р.': 1985, 'должность': 'разработчик'},
                  'Сотрудник2': {'пол': 'ж', 'г.р.': 1989, 'должность': 'тестировщик'},
                  'Сотрудник3': {'пол': 'ж', 'г.р.': 1995, 'должность': 'аналитик'},
                  'Сотрудник4': {'пол': 'м', 'г.р.': 1979, 'должность': 'лид'}
                  }
name = 'Сотрудник1'
param = 'г.р.'
year_of_birth = employees_dict[name][param]
for key in employees_dict:
    if employees_dict[key][param] > year_of_birth:
        year_of_birth = employees_dict[key][param]
        name = key
print('Самый молодой сотрудник:', name, ', в этом году ему исполняется', currentYear - year_of_birth, 'лет')

# 3) запрос данных от пользователя
profession = input('Введите должность для поиска:\n')
for key, value in employees_dict.items():
    if value.get('должность') == profession:
        print(key)


