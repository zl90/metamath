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

timeLimitInSeconds = 60
startTime = time.time()
endTime = startTime + timeLimitInSeconds

timesTables = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
score = 0
total = 0

while (userInput != 'q' and time.time() < endTime):
    a = random.sample(timesTables, 1)[0]
    b = random.sample(timesTables, 1)[0]

    answer = a * b

    print(f"{a} x {b} = ")

    start = time.time()

    userInput = input()
    if (userInput != 'q'):
        total += 1
        formattedInput = int(userInput)

        end = time.time()

        if (formattedInput != answer):
            print(f'wrong... answer: {answer}\n')
        else:
            score += 1
            print(f"time: {end - start}")

print(f"\nTimes up! You scored {score} out of {total}")
