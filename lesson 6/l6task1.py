#Make a program that has some sentence (a string)
# on input and returns a dict containing all unique words as keys and the number of occurrences as values.
one_str = 'Ехал Грека через реку, Видит Грека - в реке рак. Сунул Грека руку в реку, Рак за руку Грека - цап!'
print('First str = ', one_str)
print('--------------')
symbol = '!/\,.?!@#$%^&*()[]*-+:;'
clean_one_str = one_str.lower()
# .lower() - прировняли к нижнему регистру
for i in symbol:
    clean_one_str = clean_one_str.replace(i, '')
# .replace(i, '') - убрали лишние символы
words_list = clean_one_str.split()
# .split() разбили строку и создали список
my_dict = {word: words_list.count(word) for word in words_list}
print(my_dict)