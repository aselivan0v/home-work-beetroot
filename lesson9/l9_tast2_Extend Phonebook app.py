# Task 2
# Extend Phonebook application
#
# Functionality of Phonebook application:
#
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook. Application should load JSON data,
# if it is present in the folder with application, else raise an error. After the user exits, all data should be saved
# to loaded JSON.
import json

FILENAME = 'Phonebook.json'


def add_new_entries(entries, first_name, last_name, telephone_number, city):
    new_entrie = {}
    new_entrie['first_name'] = first_name
    new_entrie['last_name'] = last_name
    new_entrie['telephone_number'] = telephone_number
    new_entrie['city'] = city
    new_entrie['id'] = int(max(entries)) + 1
    entries[new_entrie['id']] = new_entrie

    write_file(entries)



def search_by_first_name(entries, first_name):
    resalt = []
    for a in entries:
        if (entries[a]['first_name'] == first_name):
            resalt.append([first_name, entries[a]['last_name'], entries[a]['telephone_number'], entries[a]['city']])
    if not resalt:
        return 'Такого имени нет'
    return resalt

def search_by_last_name(last_name):
    for x in entries:
        if (entries[x]['last_name'] == last_name):
            return 'Такая фамилия есть'
    return 'Такой фамилии нет'


def search_by_full_name(first_name, last_name):
    for x in entries:
        for q in entries:
            if (entries[x]['first_name'] == first_name and entries[q]['last_name'] == last_name):
                return 'Такое ФИО есть'
    return 'Такого ФИО нет'


def search_by_telephone_number(telephone_number):
    for x in entries:
        if (entries[x]['telephone_number'] == telephone_number):
            return 'Такой номер есть'
    return 'Такого номера нет'


def search_by_city_or_state(city):
    for x in entries:
        if (entries[x]['city'] == city):
            return 'Такой город есть'
    return 'Такого города нет'


def delete_a_record_for_a_given_telephone_number():
    pass

def update_a_record_for_a_given_telephone_number(entries, telephone_number):
    new_entries = {}
    for x in entries:
        print(x, type(x), entries[x]['telephone_number'], type( entries[x]['telephone_number'] ))
        new_number = {}
        if entries[str(x)]['telephone_number'] == telephone_number:
            new_number['telephone_number'] = input('Такой номер есть! \nВведите новый номер: ')
            new_entries.update(new_number)
            write_file(new_entries)
        else:
            new_entries[x] = entries[x]
            # return print('Поздравляем, ввели новый номер: ', new_number)
    return 'Такого номера нет'

def an_option_to_exit_the_program():
    pass

def read_file():
    with open(FILENAME) as file:
        x = json.load(file)
    return x

def write_file(dict):
    with open(FILENAME, 'w') as file:
        json.dump(dict, file)


def main():
    entries = read_file()
    while True:
        print( '''1. Add new entries
2. Search by first name
3. Search by last name
4. Search by full name
5. Search by telephone number
6. Search by city or state
7. Delete a record for a given telephone number
8. Update a record for a given telephone number
9. An option to exit the program''')

        choice = input()
        if choice == '1': add_new_entries(entries,
                                          input('first name '),
                                          input('last name '),
                                          input('telephone_number '),
                                          input('city'))
        if choice == '2': print(search_by_first_name(entries, input('Введите имя ')))
        if choice == '8': print(update_a_record_for_a_given_telephone_number(entries, input('Введите номер: ')))




# print(entries)
#add_new_entries(24, 'Dima', 'Savchuk', '98745661', 'Kyiv')
# print(entries)
#
# print(search_by_first_name('Sacha'))
# print(search_by_last_name('Selivanov'))
# print(search_by_telephone_number('98745661'))
# print(search_by_city_or_state('Kyiv'))
# print(search_by_full_name('Artem', 'Savchuk'))
# print(update_a_record_for_a_given_telephone_number('98745661'))
# print(entries)
# write_file(entries)
# print(read_file(), type(read_file()))

main()
