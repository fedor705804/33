
my_dict = {"Minecraft" : 'люблю',
           "Лето" : 'люблю',
           "Лазертаг" : 'люблю',
           "Роза" : 'люблю',
           "Буся" : 'люблю',
           "Играть" : 'люблю',
           "Stalker" : 'люблю'}

question_1 = 'Угадай, что я люблю: '
result = 0

print(question_1)
if my_dict.get(input()) == 'люблю':
 result += 1  

print(question_1)
if my_dict.get(input()) == 'люблю':
 result += 1  

print(question_1)
if my_dict.get(input()) == 'люблю':
 result += 1  

print('ты угадал ', result , 'раз')
