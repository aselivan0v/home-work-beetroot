import random

sample_letters = input('Enter your world: ')
for _ in range(5):
    result = ''.join(random.sample(sample_letters, 5))
    print(result)