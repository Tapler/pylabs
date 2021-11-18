# заменить все буквы x на y
source_string = "sdgasx xxx fsdga"
newString = ""

for x in source_string:
    if x == "x":
        newString += "y"
    else:
        newString += x

print('Исходная строка:', source_string)
print('Новая строка:', newString)

# сосчитать произведение числе, кратных 3 и 5
numbers = [1, 2, 3, 15, 5, 6, 7, 45, 4, 3]
multiplication = 1

for x in numbers:
    if x // 3 == x / 3 and x // 5 == x / 5:
        multiplication *= x

print('multiplication=', multiplication)

source_string = "sdgasx xxx fsdga"
print('Исходная строка:', str, '\nНовая строка:', source_string.replace("x", "y"))
