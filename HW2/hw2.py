"""
Si Kai Lee sl3950
Columbia W4111 Introduction to Databases
Homework 2
"""

import sys
from collections import *


def load_data(file_path):
    """
    This method reads the dataset, and returns a list of rows.
    Each row is a list containing the values in each column.
    """
    import csv
    with file(file_path) as f:
        dialect = csv.Sniffer().sniff(f.read(2048))
        f.seek(0)
        reader = csv.reader(f, dialect)
        return [l for l in reader]


def q1(data):
    """
    @param data the output of load_data()
    @return the number of  distinct types of items (by `description` attribute) in this dataset
    """
    # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
    # 826
    items = []

    for i in range(1, len(data)):
        items.append(data[i][15])
    return len(set(items))


def q2(data):
    """
    @param data the output of load_data()
    @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
    """
    # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
    # 54

    vendors = []

    for i in range(1, len(data)):
        vendors.append(data[i][-9])
    return len(set(vendors))


def q3(data):
    """
    @param data the output of load_data()
    @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
    """
    # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
    # https://docs.python.org/2/tutorial/datastructures.html
    # 2633

    store_sales = {}

    for i in range(1, len(data)):
        if data[i][2] not in store_sales:
            store_sales[data[i][2]] = int(data[i][-2])
        else:
            store_sales[data[i][2]] += int(data[i][-2])

    return sorted(store_sales, key=store_sales.__getitem__)[-1]


def q4(data):
    """
    @param data the output of load_data()
    @return The value of the `description` attribute of the most sold item from the store from q3()
    """
    # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
    # https://docs.python.org/2/tutorial/datastructures.html
    # Captain Morgan Spiced Rum, Juarez Tequila Gold

    s_id = q3(data)

    most_sold, description = 0, ''

    for i in range(1, len(data)):
        if data[i][2] == s_id and int(data[i][-2]) >= most_sold:
            most_sold = int(data[i][-2])
            description = data[i][15]
            print most_sold, description

    # for i in range(1, len(data)):
    #     if data[i][2] == s_id:
    #         print data[i][-2], data[i][15]

    return description


def q5(data):
    """
    Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
    @param data the output of load_data()
    @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
    """
    # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
    # https://docs.python.org/2/tutorial/datastructures.html
    # 50320

    zipcode_qty = {}

    for i in range(1, len(data)):
        if data[i][6] not in zipcode_qty and data[i][11] == 'TEQUILA':
            zipcode_qty[data[i][6]] = int(data[i][-2])
        elif data[i][11] == 'TEQUILA':
            zipcode_qty[data[i][6]] += int(data[i][-2])

    return sorted(zipcode_qty, key=zipcode_qty.__getitem__)[-1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
      sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
      sys.exit(1)
    file_path = sys.argv[1]

    data = load_data(file_path)
    print q1(data)
    print q2(data)
    print q3(data)
    print q4(data)
    print q5(data)
