import json

my_dict = {}
my_dict['age'] = 25
my_dict['name'] = 'Carl'
my_dict['data'] = [1, 2, 3, 4]
my_dict['float'] = 1.1
my_dict['bool'] = [True, False]
my_dict['NoneType'] = None


print(my_dict)
#with open('hello.json', 'w') as file:
#    file.write(str(my_dict))
#    json.dump(my_dict, file)

my_json_obj = {}
with open('hello.json', 'r') as file:
    my_json_obj = json.load(file)

with open('hello.json', 'r') as file:
    print(file.read())

print(my_json_obj, type(my_json_obj))