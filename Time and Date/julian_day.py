#!/usr/bin/python3

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Gregorian date for today: ", now.toString(Qt.ISODate))
print("Julian date for today: ", now.toJulianDay())
