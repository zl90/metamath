# iteration 1: basic times tables.
# iteration 2: add a timer and time limit.
# iteration 4: add ability to choose what times tables I want to include. <-- use random.sample()
# iteration 3: add csv file storage to track times.
# iteration 5: add division too.
# iteration 6: add addition and subtraction.

import random
import time

random.seed()

userInput = ''

while (userInput != 'q'):
    a = random.randint(3, 12)
    b = random.randint(3, 12)

    while (a % 10 == 0):
        a = random.randint(3, 12)

    while (b % 10 == 0):
        b = random.randint(3, 12)

    answer = a * b

    print(f"{a} x {b} = ")

    start = time.time()

    userInput = input()
    if (userInput != 'q'):
        formattedInput = int(userInput)

        end = time.time()

        if (formattedInput != answer):
            print(f'wrong... answer: {answer}\n')

        print(f"time: {end - start}")
