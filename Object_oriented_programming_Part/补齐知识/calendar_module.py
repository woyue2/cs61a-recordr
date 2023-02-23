import calendar

print(calendar.calendar(2023))

f = open('calendar.xlsx','w')
f.write(calendar.calendar(2023))