#! /usr/bin/env python3
# This is game of guessing numbers

import random
guessTaken = 0

print("Привет! Как тебя зовут?")
myName = input()

number = random.randint(1,20)
print("Что ж, {}, я загадываю число от 1 до 20.".format(myName))

for guessTaken in range(6):
    print("Попробуй угадать.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Твоё число слишком маленькое.")

    if guess > number:
        print("Твоё число слишком большое.")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print("Отлично, {}! Ты справился за {} попытки!".format(myName, guessTaken))

if guess != number:
    number = str(number)
    print("Увы! Я загадала число {}".format(number))
