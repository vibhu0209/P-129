import csv

data = []
with open("E:\WHITEHAT JR\P-129\bright_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

# coneverting all planet name to lower case 
for data_point in planet_data:
    data_point[2] = data_point[2].lower()
    
# sorting planet names in alphabetical order 
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("E:\WHITEHAT JR\P-129\dwarf_stars.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)