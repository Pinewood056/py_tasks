import datetime
# check real date in valid DD, MM, YYYY format
inputDate = [14, 10, 1994]
# check yyyy, dd, mm format date
inputDate2 = [1400, 10, 19]
# check mm, yyyy, dd format date
inputDate3 = [12, 1000, 31]
# check for existing 31 June 2021 (No)
inputDate4 = [31, 6, 2021]
# check for existing 31 July 2021 (Yes)
inputDate5 = [31, 7, 2021]


def check_date():
    day, month, year = inputDate
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    if is_valid:
        print(inputDate, "- This date is exist")
    else:
        print(inputDate, "- This date isn`t exist")


def check_date2():
    day, month, year = inputDate2
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    if is_valid:
        print(inputDate2, "- This date is exist")
    else:
        print(inputDate2, "- This date isn`t exist")


def check_date3():
    day, month, year = inputDate3
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    if is_valid:
        print(inputDate3, "- This date is exist")
    else:
        print(inputDate3, "- This date isn`t exist")


def check_date4():
    day, month, year = inputDate4
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    if is_valid:
        print(inputDate4, "- This date is exist")
    else:
        print(inputDate4, "- This date isn`t exist")


def check_date5():
    day, month, year = inputDate5
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    if is_valid:
        print(inputDate5, "- This date is exist")
    else:
        print(inputDate5, "- This date isn`t exist")


check_date()
check_date2()
check_date3()
check_date4()
check_date5()
