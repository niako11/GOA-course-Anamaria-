year = int(input("enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is coming to an end.")
else:
    print("The year is not over.")
