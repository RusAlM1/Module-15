import json

s = {
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'isAlive': True,
    'age': 32,
    'address': {
        'streetAddress': 'Нейбута 32',
        'city': 'Владивосток',
        'state': '',
        'postalcode': ''
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '123-333-4455'
        },
        {
            'type': 'office',
            'number': '123 111-4567'
        }
    ],
    'children': [],
    'spouse': None
}


# with open('1.json', 'w', encoding='utf8') as f:
#     json.dump(s, f, ensure_ascii=False, indent=4)  # dump - помогает записывать данные в фаил целиком как есть
                                                  # dumps - помогает записывать в фаил строку, аналог функции read

# with open('1.json', 'w', encoding='utf8') as f:
#     json_string = json.dumps(s)
#     print(json_string, file=f)

# with open('1.json', encoding='utf8') as f:
#     print(f.read())

# with open('1.json', encoding='utf8') as f:
#     t = json.load(f)
#     print(t)
#
# print(t['firstname'])

# Задание. Подсчитываем сколько раз встречается в файле какое-либо слово:
f = open('1.json', 'r')
lines = f.readlines()
f.close()

s = 'type\n'
count = 0

for i in lines:
    if i == s:
        count += 1
print(s, '=', count)

# второй вариант:

for i in range(len(lines)):
    if lines[i] == s:
        lines[i] = '1'
print(lines)
res_str = ''
for i in lines:
    res_str += 1
# print(res_str)

# добавление в фаил
f = open('2.txt', 'w')
f.write(res_str)
f.close()

f = open('2.txt', 'w')
print(f.read())
f.close()


