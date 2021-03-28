def update_a_record_for_a_given_telephone_number(telephone_number):
    for x in entries:
        if (entries[x]['telephone_number'] == telephone_number):
            entrie.update({telephone_number: str(input('Такой номер есть! \nВведите новый номер: '))})
            return print('Поздравляем, ввели новый номер: ', telephone_number)
    return 'Такого номера нет'