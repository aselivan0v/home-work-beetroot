import json

my_dict = {}
my_dict['age'] = 25
my_dict['name'] = 'Carl'
my_dict['data'] = [1, 7, 18]
my_dict['float'] = 1.1
my_dict['name_2'] = 'Карл'
with open('test.json', 'w') as file:
    json.dump(my_dict, file, ensure_ascii= False)

with open('test.json', 'r') as file:
    print(file.read())