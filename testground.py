line_first = input().split()
line_second = input().split()

def date(M, D, year, month, day):
    if day < D:
        day += 1
    elif day == D:
        day = 1
        month += 1

    if month > M:
        month = 1
        year += 1

    return str(year) + " " + str(month) + " " + str(day)   

M = int(line_first[0])
D = int(line_first[1])
year = int(line_second[0])
month = int(line_second[1])
day = int(line_second[2])

print(date(M, D, year, month, day))                


              



