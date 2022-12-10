path = r"C:\Users\Vidyashree M C\Desktop\data.csv"
#
# with open(path) as csv_file:
#
#     for line in csv_file:
#         print(line)
#         print(type(line))

import csv


"""
1. open csv file.
2. read/write
3. close file

reading operations:
1. reader()     - list
2. DictReader() - dictionary

"""
# with open(path) as file:
#     reader_obj = csv.reader(file)
#     print(reader_obj)       # typecasting, traverse, next()
#
#     for row in reader_obj:
#         print(row)          # list of rows
#
# print()
# with open(path) as file:
#     reader_obj = csv.DictReader(file)
#     print(reader_obj)
#
#     for row in reader_obj:
#         print(row)

#################################################################################
with open(path) as csv_:
    reader_obj = csv.reader(csv_)

    # skipping the header
    header = next(reader_obj)

    count = 0
    for row in reader_obj:
        count += 1

    # print(count)

#####################################################################################

path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\csv_files\employees.csv"

# reader()
# with open(path) as csv_file:
#     reader_obj = csv.reader(csv_file)
#     header = next(reader_obj)
#
#     for row in reader_obj:  # [douglas, male, testing, 70000]
#         if row[1] == "female":
#             print(row)
#
#
# # DictReader()
# with open(path) as csv_file:
#     reader_obj = csv.DictReader(csv_file)
#
#     for row in reader_obj:  # {name: douglas, gender: male, team: testing, pay: 70000}
#         if row["gender"] == "female":
#             print(row)

#############################################################################
path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\csv_files\example.csv"


"""
writing operation:
1. writer()     --> list/tuple
2. DictWriter() --> dictionaries

to write the data
1. writerow -> single data
2. writerows -> multiple data

"""

with open(path, "w") as file:
    writer_obj = csv.writer(file)
    # writer_obj.writerow("hello")
    # writer_obj.writerow([1, 2, 3, 4])
    # writer_obj.writerow((10, 20, 30, "hai"))
    # writer_obj.writerow({1, 2, 3, 4})
    # writer_obj.writerow({"a": 1, "b": 2})

    # writer_obj.writerows(["hello", [1, 2, 3, 4], (10, 20, 30, "hai"), {1, 2, 3, 4}])

path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\csv_files\example1.csv"

with open(path, "w") as csv_file:
    writer_obj = csv.DictWriter(csv_file, ["name", "pay"])
    writer_obj.writeheader()
    writer_obj.writerow({"name": "ram", "pay": 12000})
    writer_obj.writerow({"name": "shyam", "pay": 20000})
    writer_obj.writeheader()

    writer_obj.writerows([{"name": "steve", "pay": 1000},
                          {"name": "john", "pay": 2000},
                          {"name": "bill", "pay": 3000},
                          {"name": "bob", "pay": 4000}])


















