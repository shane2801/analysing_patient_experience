import csv
# read csv file

filepath = 'C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\hospital-masterfile.csv'
main_file = []
with open(filepath, 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  next(csv_reader)
  for line in csv_reader:
    if line[5]=='' and line[6] == '':
      line[6] = line[4]
    elif line[6] == '':
      line[6] = line[5]   
    main_file.append(line)
    
## saving our file
print("Writing file...")

with open('hospital-masterfile-5.csv', 'w', encoding='utf-8', newline='') as csvfile3:
  # specify field names
  fieldnames = [
    'name', 
    'name2',
    'address',
    'streetAddress',
    'addressLocality',
    'addressRegion',
    'postalCode',
    'href',
    'overview',
    'id',
    'reviews-and-ratings-link',
    'starturl'
    ]
  writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)
  writer.writeheader()

  for text in main_file:
    writer.writerow({
      'name' : text[0], 
      'name2' : text[1],
      'address' : text[2],
      'streetAddress' : text[3],
      'addressLocality' : text[4],
      'addressRegion' : text[5],
      'postalCode' : text[6],
      'href' : text[7],
      'overview' : text[8],
      'id' : text[9],
      'reviews-and-ratings-link' : text[10],
      'starturl' : text[11]
    })

print("Successfully cleaned up hehe")