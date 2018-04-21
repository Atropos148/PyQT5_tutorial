#!/usr/bin/python3

from PyQt5.QtCore import QDate

xmas1 = QDate(2017, 12, 24)
xmas2 = QDate(2018, 12, 24)

now = QDate.currentDate()

days_passed = xmas1.daysTo(now)
print("{0} days have passed since last Xmas.".format(days_passed))

no_of_days = now.daysTo(xmas2)
print("There are {0} days until newt Xmas.".format(no_of_days))
