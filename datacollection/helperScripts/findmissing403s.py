import csv

all_gp_links = []
with open('C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\gp-links.csv', 'r') as file_1:
  csv_reader = csv.reader(file_1)
  next(csv_reader)
  for line in csv_reader:
    id = line[1].split('=')[1]
    line.append(id)
    all_gp_links.append(line)

scraped_gp_links = []
with open('C:\\Users\\kmuth\\fyp-tutorial-redo\\datacollection\\myscrapyproject\\myscrapyproject\\gps-links-run-2.csv', 'r') as file_2:
  csv_reader2 = csv.reader(file_2)
  next(csv_reader2)
  for line in csv_reader2:
    id2= line[4].split("X")[1]
    line.append(id2)
    scraped_gp_links.append(line)

for index, line in enumerate(all_gp_links):
  message = "not found"
  if index <= len(scraped_gp_links):
    main_id = line[2]
    for link in scraped_gp_links:
      if int(link[5]) == int(main_id):
        message = "found"
        break
  line.append(message)


print("Writing file...")

with open('corrected-missing-links-gps-mainfile-1.csv', 'w', encoding='utf-8', newline='') as csvfile:
  # specify field names
  fieldnames = ['name', 'overview', 'id', 'status']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  for line in all_gp_links:
    writer.writerow({
      'name': line[0], 
      'overview': line[1],
      'id' : line[2],
      'status' : line[3]
    })

print("Successfully found all the links")


