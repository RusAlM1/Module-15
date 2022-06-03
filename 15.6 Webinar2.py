# myfile = open('helo.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()

# раюота с файлами и исключениями
# try:
#     somefile = open('hello1.txt', 'w')
#     try:
#         somefile.write('hello world')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)

# with open('helo2.txt', 'w') as somefile:
#     somefile.write('goodbye world!')

# with open('test.txt', 'a') as file:
#     file.write('\nbye world!')

# with open('test1.txt', 'w') as file:
#     file.write('''1758
# 1863
# 1367
# 1452
# 1986
# 1593
# 1846
# 2486
# 8462''')

# with open('test1.txt') as f: #не указали функцию, т.к. по умолчанию идет 'r' - чтение
#     a = f.readlines()
#     # b = list(map(int, a))
#     # print(b[5])
#     c = [int(x) for x in a]
#     print(c)

# Задача 1
# with open('test1.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     # print(a)
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0:
#             res.append(i)
# print(max(res), len(res)) # выдает ошибку "ValueError: max() arg is an empty sequence"

# Задача 2
# with open('test2.txt', 'w') as file:
#     file.write('''1758
# 1863
# 1367
# 1452
# -1986
# 1593
# 1846
# -2486
# 8462
# 1758
# -1863
# 1367
# 1452
# 1986
# 1593
# -1846
# 2486
# 8462
# -9058
# 7005
# -6048
# 6872
# 9685
# -4120
# 9010
# 2856
# 7777''')

# with open('test2.txt') as f:
#     s = [int(x) for x in f]
#     res = []
#     for i in range(1, len(s)):
#         # print(s[i], '    ', s[i-1])
#         if (abs(s[i]) % 10 == 7 or abs(s[i - 1]) % 10 == 7) and (s[i] + s[i - 1]) % 12 == 0:
#             res.append(s[i] + s[i - 1])
# print(len(res), max(res)) # выдает ошибку "ValueError: max() arg is an empty sequence"

# Задача 3
# with open('test3.txt', 'w') as file:
#     file.write('''XXXYZYYYZYYYZZXXYXYYYYZZXYYYZYYXYYYXYYYYZZZZXXXXZYYXYYZZZXYYZZXYYZZXYYZ
# YYYXZXZZZXXYYZZZXXXYZXYZYYYZYYYYXXXYYYYZZZZXYXYYYXXXXXZZZZYYYXXYYZZ''')

# with open('test3.txt') as f:
#     s = f.readline()
#     # print(s)
#     m = 1
#     k = 1
#     for i in range(1, len(s)):
#         # print(s[i], '    ', s[i-1])
#         if s[i] != s[i - 1]:
#             k += 1
#             m = max(k, m)
#         else:
#             k = 1
# print(m)

# Подсчет кол-ва слов
# myfile = open('textsong.txt', 'w')
# file = myfile.write('''I spoke to God today and She said that She's ashamed
# What have I become?
# What have I done?
# I spoke to the devil today and he swears he's not to blame
# And I understood 'cause I feel the same
# Arms wide open
# I stand alone
# I'm no hero and I'm not made of stone
# Right or wrong
# I can hardly tell
# I'm on the wrong side of Heaven and the righteous side of hell
# The wrong side of Heaven and the righteous side
# The righteous side of hell''')
# print(file)
# myfile.close()

# myfile = open('textsong.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()

# file = open('textsong.txt')
# data = file.read()
# words = data.split()
# print(words)
# print(len(words))
# file.close()

# JSON

import json # импорт всегда указывается в самом начале кода

# data = {
#     "name": "Ivan",
#     "age": 26,
#     "city": "Saratov"
# }
#
# with open('data_file.json', 'w') as f:
#     data = json.dump(data, f)

with open('data_file.json', 'r') as f:
    data1 = json.load(f)
    print(data1)
    print(type(data1))