def leap_year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return 1
    else:
        return 0

def number_of_days(m, y):
    if m == 2:
        if leap_year(y) == 1:
            return 29 
        else:
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31
        
def days_left(d, m, y):
    c = number_of_days(m,y) - d
    for x in range(m + 1, 13):
        c += number_of_days(x, y)
    return(c)
    
    
#main
print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

print("Menu: ")
print("1) Calculate the number of days in the given month")
print("2) Calculate the number of days in the given year")
menu_choice = int(input(""))

if menu_choice == 1:
    print(number_of_days(month, year))
else:
    print(days_left(day, month, year))