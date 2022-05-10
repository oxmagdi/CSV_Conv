import csv
import re

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def read_CSV_File():

    with open(r"product1652128393.csv", newline='', encoding="utf8") as csvfile:
        data = csv.DictReader(csvfile)
        rows=[]
        for row in data:
            rows.append([
                row['id'],
                row['title'],
                cleanhtml(row['description']),
                row['availability'],
                'new',
                row['price'],
                row['link'],
                row['image_link'],
                row['Manufacturer']
            ])

        return rows
#                 ['id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link', 'brand'],

def create_CSV_file(filename, fields, rows):

    # writing to csv file
    with open(filename, 'w',  newline='', encoding='utf-8') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    rows = read_CSV_File()
    print(rows)
    # name of csv file
    filename = "facebook_catalog.csv"
    # field names
    create_CSV_file(filename,
                    ['id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link', 'brand'],

                    rows)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
