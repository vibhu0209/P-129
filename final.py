import csv 
dataset_1 = []
dataset_2 = []

with open("E:\WHITEHAT JR\P-129\bright_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open("E:\WHITEHAT JR\P-129\dwarf_stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
planet_data = []

for index, data_row in enumerate(planet_data_1):    
    planet_data.append(planet_data_1[index] + planet_data_2[index])


with open("final_merged.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
