
import csv


def read_CSV_File():

    with open(r"C:\\Users\\Nemo\\Desktop\\CSV_Conv\\catalog_products.csv", newline='') as csvfile:
        data = csv.DictReader(csvfile)
        print("ID Department Name")
        print("---------------------------------")
        for row in data:
            print(row['id'])

def create_CSV_file(filename, fields, rows):

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    columns, rows = read_CSV_File()

    # name of csv file
    filename = "my.csv"
    # field names
    # create_CSV_file(filename,
    #                 ['Name', 'Branch', 'Year', 'CGPA'],
    #                 [['Nikhil', 'COE', '2', '9.0'],
    #                 ['Sanchit', 'COE', '2', '9.1'],
    #                 ['Aditya', 'IT', '2', '9.3'],
    #                 ['Sagar', 'SE', '1', '9.5'],
    #                 ['Prateek', 'MCE', '3', '7.8'],
    #                 ['Sahil', 'EP', '2', '9.1']])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
