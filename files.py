def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
        new_ing = dict(ingridient)
        new_ing['quantity'] *= person_count
        if new_ing['ingridient_name'] not in shop_list:
            shop_list[new_ing['ingridient_name']] = new_ing
        else:
            shop_list[new_ing['ingridient_name']]['quantity'] += new_ing['quantity']
  return shop_list

def print_shop_list(shop_list):
    for ingredient in shop_list.values():
        print('{} {} {}'.format(ingredient['ingredient_name'], ingredient['quantity'], ingredient['measure']))

def get_menu_with_quantity(path):
    cook_book = {}
    with open(path, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            line = line.strip()
            cook_book.update({line: []})
            count = int(f.readline().strip())
            for _ in range(count):
                ingredient = f.readline().strip().split(' | ')
                dish_items = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                cook_book[line].append(dish_items)
            f.readline()
    return cook_book

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = get_menu_with_quantity("cook_book.txt")
    shop_list = get_shop_list_by_dishes(cook_book, person_count)
    print_shop_list(shop_list)

create_shop_list()