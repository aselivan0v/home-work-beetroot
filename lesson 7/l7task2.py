#Creating a dictionary.

#Create a function called make_country, which takes in a country’s name and capital as parameters.
#Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
#Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(**kwargs):
    for name, capital in kwargs.items():
        print(f'Country: {name} - Her Capital: {capital}')
make_country(Ukraine = 'Kiev', Germany = 'Berlin', Poland ='Warsaw', Portuga = 'Lisbon', Qatar = 'Doha', Romania = 'Bucharest')