import csv

mainfile_path= "C:\\Users\\kmuth\\OneDrive\\Documents\\hospitals-initial-run-links-removedfaultylinks.csv"
secondfile_path="C:\\Users\\kmuth\\OneDrive\\Documents\\decoded-hospitals-301.csv"

# reading main file
with open(mainfile_path, 'r') as csv_file:
  main_file = []
  csv_reader = csv.reader(csv_file)
  next(csv_reader)
  for line in csv_reader:
    temp = []
    name = line[0]
    name2 = line[1]
    address = line[2]
    streetAddress = line[3]
    addressLocality = line[4]
    addressRegion = line[5]
    postalCode = line[6]
    href = line[7]
    overview = line[8]

    if address == "":
      address = streetAddress + " " + addressLocality + " " + addressRegion + " " + postalCode 
    else:
      address = address.strip()
    
    id = overview.split('=')[1]

    temp.append(name)
    temp.append(name2)
    temp.append(address)
    temp.append(streetAddress)
    temp.append(addressLocality)
    temp.append(addressRegion)
    temp.append(postalCode)
    temp.append(href)
    temp.append(overview)
    temp.append(id)

    main_file.append(temp)
  print("Length of the main file is:", len(main_file))


with open (secondfile_path, 'r') as decoded_urls_csvfile:
  second_file = []
  csv_reader2 = csv.reader(decoded_urls_csvfile)
  next(csv_reader2)
  for line in csv_reader2:
    temp2 = []
    link = line[0]
    starturl = line[1]
    id2 = starturl.split('=')[1]
    temp2.append(link)
    temp2.append(starturl)
    temp2.append(id2)
    second_file.append(temp2)


for i, line in enumerate(main_file):
  main_id = int(line[9])
  link = "missing"
  url = "missing"
  for ss in second_file:
    if int(ss[2]) == main_id:
      link = ss[0]
      url = ss[1]
      break
  line.append(link)
  line.append(url)

## saving our file
print("Writing file...")

with open('hospital-masterfile.csv', 'w', encoding='utf-8', newline='') as csvfile3:
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