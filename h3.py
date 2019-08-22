year = int(input("Enter Year"))


def is_leap(year):
    leap = False
    if 1900 <= year <= 1e5:
        if year % 4 == 0:
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
            else:
                leap = True
    return leap


print(is_leap(year))
