# 3 + 3 = 6
for i in range(5):
    user_answer = int(input(f"3 + 3 = x\n Find an x: "))
    if 3 + 3 == user_answer:
        print("WOW, you are right!")
        print("Next question:")
        break
    else:
        i += 1
        print(f"Try again. {i} attempts from 5")
        continue
else:
    raise Exception("You lose")
# 8 - 4 = 2
for i in range(5):
    user_answer = int(input(f"8 - 4 = x\n Find an x: "))
    if 8 - 4 == user_answer:
        print("WOW, you are right!")
        print("Next question:")
        break
    else:
        i += 1
        print(f"Try again. {i} attempts from 5")
        continue
else:
    raise Exception("You lose")
# 2 + 2 * 2 = 6
for i in range(5):
    user_answer = int(input(f"2 + 2 * 2 = x\n Find an x: "))
    if 2 + 2 * 2 == user_answer:
        print("WOW, you are right!")
        print("Next question:")
        break
    else:
        i += 1
        print(f"Try again. {i} attempts from 5")
        continue
else:
    raise Exception("You lose")
# 12 / 3 = 4
for i in range(5):
    user_answer = int(input(f"12 / 3 = x\n Find an x: "))
    if 12 / 3 == user_answer:
        print("WOW, you are right!")
        print("Congratulations! You won!")
        break
    else:
        i += 1
        print(f"Try again. {i} attempts from 5")
        continue
else:
    raise Exception("You lose")