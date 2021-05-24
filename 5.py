import datetime

inputDate = input("To check the date, enter the date in format 'dd/mm/yy' : ")

day,month,year = inputDate.split('/')

isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False

if(isValidDate) :
    print ("True")
else :
    print ("False")