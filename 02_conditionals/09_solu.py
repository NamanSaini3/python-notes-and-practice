year = 2026 

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,   " not this year  last leap year was 2024. So 2028 will be our next leap year" )
else:
    print(year, "is NOT a leap year")
