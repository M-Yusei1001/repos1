import csv

date = []
DATE_COLUMN = 0

#BOM付きCSVも読み込めるように、encodingはutf-8-sigを指定
with open("date_practice.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    
    for row in reader:
        date.append(row[DATE_COLUMN].split("/"))
        

print(date)        


