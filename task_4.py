new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for string in new_list:
    name = string.split()[-1]
    print(f'Привет, {name.capitalize()}!')
