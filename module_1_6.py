my_dict = { 'Boris': 33, 'Valera':48,'Petr': 27, 'Roman': 22}
print ('Изначальный словарь:',my_dict)
print('Значение по существующему ключу:',my_dict['Valera'])
print('Значение по отсутствующему ключу:',my_dict.get('Slava'))
my_dict.update({'Nevil': 29, 'Vsevolod': 65}) #можно добавлять в словарь сразу несколько пар
#my_dict['Nevil']= 29    #можно добавлять пары в словарь  по одному
#my_dict['Vsevolod']= 65
ydalil= my_dict.pop('Vsevolod')
print ('Удаленное значение:',ydalil)
print ('Измененный словарь:',my_dict)

print('')
my_set = {2,2,3,3,3,4,5,4,5,'Помидор','Фрукт','Помидор',True}
print('Изначальное множество:',my_set)
my_set.update([8,'Огурец']) # так же можно добавлять по одному через add
my_set.discard(3) #Так же можно было использовать remove, pop, в зависимости от наших задач
print ('Измененное множество:',my_set)