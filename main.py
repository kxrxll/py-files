cook_book = {}

with open('recipes.txt') as file:
    lines = file.readlines()
    iterator = 0
    while iterator < len(lines):
        dish_name = lines[iterator].strip()
        cook_book[dish_name] = []
        iterator += 1
        number_of_ingredients = int(lines[iterator].strip())
        iterator += 1
        while number_of_ingredients > 0:
            ingredient_list = lines[iterator].strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_list[0],
                'quantity': ingredient_list[1],
                'measure': ingredient_list[2]
            }
            cook_book[dish_name].append(ingredient)
            number_of_ingredients -= 1
            iterator += 1
        iterator += 1


def get_shop_list_by_dishes(book, persons):
    result = {}
    while persons > 0:
        for dish in book:
            for ingredient_to_check in book[dish]:
                ingredient_name = ingredient_to_check['ingredient_name']
                result.setdefault(ingredient_name, {})
                ingredient_from_shop_list = result[ingredient_name]
                ingredient_from_shop_list['measure'] = ingredient_to_check['measure']
                ingredient_from_shop_list.setdefault('quantity', 0)
                ingredient_from_shop_list['quantity'] += int(ingredient_to_check['quantity'])
        persons -= 1
    return result


print(get_shop_list_by_dishes(cook_book, 2))


def file_parser(file_name):
    with open(file_name) as f:
        parsed_lines = f.readlines()
        parsed_result = {
            "text": parsed_lines,
            "rows_number": len(parsed_lines),
            "name": file_name
        }
        return parsed_result


parsed_files = [file_parser("1.txt"), file_parser("2.txt"), file_parser("3.txt")]
max_file = max(parsed_files, key=lambda x: x["rows_number"])
min_file = min(parsed_files, key=lambda x: x["rows_number"])
last_file = parsed_files
for i in range(len(last_file)):
    if last_file[i]['name'] == max_file['name'] or last_file[i]['name'] == min_file['name']:
        del last_file[i]
        break
middle_file = last_file[0]
sorted_files = [min_file, middle_file, max_file]

with open('result.txt', 'w') as result_file:
    for item in sorted_files:
        result_file.write(f'{item["name"]}\n')
        result_file.write(f'{item["rows_number"]}\n')
        for line in item["text"]:
            result_file.write(line)
        result_file.write('\n\n')
