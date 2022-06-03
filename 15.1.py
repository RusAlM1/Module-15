# f = open('filename.txt', 'w')  # создание файла
# f.write('''Дайте мне белые крылья
# Я утопаю в омуте
# Через тернии, провода
# В небо, только б не мучаться
# Тучкой маленькой обернусь
# И над твоим крохотным домиком
# Разрыдаюсь косым дождем
# Знаешь, я так соскучился
# Знаешь, я так соскучился
# Знаешь, я так соскучился
# Знаешь, я так соскучился''')
# f.close()


# myFile = open ('namefile.txt', 'w')
# myFile.write('tttt')
# print('zzzz', file=myFile)

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char)+number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char)+number) % len(alphaUp)]
    else:
        return  char

with open("filename.txt") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w') as myFile:
    myFile.write(summary)
