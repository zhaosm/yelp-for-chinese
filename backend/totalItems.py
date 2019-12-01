import csv

data=set()
with open('restaurants.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        if line[1]=='business_id':
            continue
        data.add(line[1])
print("img,rank,rating,numReviews,cost,name,type,address,business_id,categories")
with open('totalItems.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        if line[8] in data:
            print(line)