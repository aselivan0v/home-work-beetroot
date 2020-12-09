from random import randint
user_number = int(input('Guess the number: '))
generated_number = randint(1, 10)
if generated_number == user_number:
    print(f'Congratulations! You won! Generated number was {generated_number}')
else:
    print('You lose! Try once more!')