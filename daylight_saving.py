#!/usr/bin/python3

from PyQt5.QtCore import QDateTime

now = QDateTime.currentDateTime()

print("Time zone: {0}".format(now.timeZoneAbbreviation()))

if now.isDaylightTime():
    print("Current date falls into DST time")
else:
    print("Current date does not fall into DST time")
