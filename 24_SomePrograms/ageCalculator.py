from datetime import date
# print(date.today())
# print(date.today() - "2025-10-03")
# print(date.today().year)
# print(date.today().month)
# print(date.today().day)
#
# print(date.today().year - 2022)

# take the year of birth and display its age
# byear = int(input("Enter your birth year:"))
# age = date.today().year - byear
# print("Your age is :", age)


# thora advanced
def calulateAge(byear, bmonth, bday):
    year = date.today().year - byear
    if(date.today().month == bmonth and date.today().day == bday):
        year = year + 1
    return year

byear = int(input("Enter a year: "))
bmonth = int(input("Enter a month: "))
bday = int(input("Enter a day: "))
age = calulateAge(byear, bmonth, bday)
print("Your exact age is: ",age)