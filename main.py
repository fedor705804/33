for i in range(99999999999999999999999999999999999):

 question_1 = 'кто нанял наёмников на уничтожение свободы? Долг или О-сознание'
 question_2 = 'как звали из книги Василия Орехова пьяного умника? Рентген или Хемуль?'
 question_3 = 'сколько удалёных мутантов в S.T.A.L.K.E.R.? 20 или 30'

 answer_1 = 'Долг'
 answer_2 = 'Рентген'
 answer_3 = '30'

 result = 0

 print(question_1)
 user_answer = input()
 if user_answer == answer_1:
  result += 1
  print('ответ верный')

 print(question_2)
 user_answer = input()
 if user_answer == answer_2:
  result += 1
  print('ответ верный')

 print(question_3)
 user_answer = input()
 if user_answer == answer_3:
  result += 1
  print('ответ верный')

 print('хотите пройти игру заново')
 print('0 - да, 1 - нет')
 last_answer = int(input('Введите ответ: '))
 if last_answer == 1:
  break

# print('ты ответил на',result, 'балов'   )
