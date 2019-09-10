import csv
import urllib.request

book_counter=0
quantity_counter=0

with open('db.sql', 'w') as f_db:
    csv.register_dialect('myDialect', delimiter = ',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('all.csv', 'r') as f_csv:
        reader = csv.reader(f_csv, dialect='myDialect')
        for row in reader:
#            try:
#                urllib.request.urlretrieve(row[5], 'book_cover/{}.jpg'.format(book_counter))
#            except urllib.error.HTTPError:
#                print('{}, {}'.format(book_counter, row[5]))

            row[1] = row[1].replace("'", "''")
            row[2] = row[2].replace("'", "''")
            row[3] = row[3].replace("'", "''")
            row[4] = row[4].replace("'", "''")
            row[5] = row[5].replace("'", "''")

            row[5] = "/static/book_cover/{}.jpg".format(book_counter)
            f_db.write("INSERT INTO book_book VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');\n".format(book_counter, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            for quantity in range(0, int(row[11])):
                f_db.write("INSERT INTO book_bookcopies VALUES({}, '{}', '{}');\n".format(quantity_counter, book_counter, "2019-08-04"))
                quantity_counter += 1
            book_counter += 1
