year = int(input("Enter a year: "))

ly = "Leap year"
cy = "Common year"

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4	!= 0:
    print(cy)
elif year % 100 != 0:
    print(ly)
elif year % 400 != 0:
    print(cy)
else:
    print(ly)

