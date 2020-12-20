#Task 1
#Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try / except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def func():
    try:
        my_list = [1, 2, 3, 4, 5]
        my_list[5]
    except IndexError:
        print("oops")
    try:
        my_dict = {'Key': 'ags'}
        return my_dict['Ke']
    except KeyError:
        print('oops Key')

func()



