sum = 0
count = 0

with open("../Common Resources/catalog_full.csv") as catalog_file:
    for line in catalog_file:
        values = line.split(sep=',')
        sum += float(values[-1])
        count += 1

print(sum/count)
