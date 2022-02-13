price_list = [57.35, 60, 46.79, 0.54, 3.72,
              356.02, 78.55, 1, 29.01, 48.1]


def fix_price(price_list):
    end_world = str(', ')
    for i, num in enumerate(price_list):
        price = str(f'{float(num):.2f}').split('.')
        if i == len(price_list) - 1:
            end_world = '\n'
        print(f'{price[0]} руб {price[1]} коп', end=end_world)


fix_price(price_list)
old_id = id(price_list)
price_list.sort()
fix_price(price_list)
new_id = id(price_list)

if old_id == new_id:
    print(f'id до сортировки: {old_id}\nid после сортировки: {new_id}\nid списка не изменился, список не менялся')

new_price_list = price_list.copy()
new_price_list.reverse()
fix_price(new_price_list)
new_id = id(new_price_list)
print(f'id изменился: {new_id}, список новый!')

five_max_price = new_price_list[0:5:].copy()
fix_price(five_max_price)
