import datetime

inputDate = input("To check the date, enter the date in format 'dd,mm,yy' : ")

day, month, year = inputDate.split(',')
isValidDate = True

try:
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False

if isValidDate:
    print("This date is exist")
else:
    print("This date isn`t exist")
