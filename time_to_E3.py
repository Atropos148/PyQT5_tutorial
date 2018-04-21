#!/usr/bin/python3

from PyQt5.QtCore import QDate


def ask_about_E3_date():
    print("When is the next E3?")
    E3_date_input = input('Put in date(numbers): year, month, day\n')
    E3_date_fixed = E3_date_input.split(',')

    for number in E3_date_fixed:
        number.strip(' ')

    return E3_date_fixed


now = QDate.currentDate()
print("Do you want E3 2018?")
answer = input('1. Yes\n2. No\n')
if int(answer) == 1:
    next_E3 = QDate(2018, 6, 12)
else:
    E3_date = ask_about_E3_date()
    next_E3 = QDate(int(E3_date[0]), int(E3_date[1]), int(E3_date[2]))

print("Days until E3: {0}".format(now.daysTo(next_E3)))
