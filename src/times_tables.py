# TODO: add ability to interrupt the loop at the exact moment the timer runs out. <-- use the signal module.
# TODO: add csv file storage to track times.
# TODO: add division too.
# TODO: add addition and subtraction.

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

    questionStartTime = time.time()

    userInput = input()
    if (userInput != 'q'):
        total += 1
        formattedInput = int(userInput)

        questionEndTime = time.time()

        if (formattedInput != answer):
            print(f'wrong... answer: {answer}\n')
        else:
            score += 1
            print(f"time: {questionEndTime - questionStartTime}")

print(f"\nTimes up! You scored {score} out of {total}")
