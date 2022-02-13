new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(new_list))


for element in new_list[:]:
    if element.startswith('+'):
        new_list.extend(('"', f'+{int(element):02d}', '"'))
    elif element.isdigit() or element[-1].isdigit():
        new_list.extend(('"', f'{int(element):02d}', '"'))
    else:
        new_list.append(element)
    new_list.pop(0)
print(new_list)
print(id(new_list))

new_line = str()

for elem in new_list:
    if elem == '"' or elem[-1].isdigit():
        new_line += elem
    else:
        new_line += ' ' + str(elem) + ' '

new_line = (" ".join(new_line.split()))
print(new_line)
