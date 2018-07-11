"""
This script provides time data about insertion into csv and txt file
"""

import os
import csv
import time


def get_txt_file_insertion_time(insertions, column=1):
    """
    get time to insert n rows with k column size in a txt file.

    :param insertions: number of rows
    :param column: number of entries separated by ,
    :return: time taken
    """
    out_str = "data," * column
    out_file = open('temp.txt', 'w')
    start_time = time.time()

    for counter in range(0, insertions):
        out_file.write("%s\n" % out_str)

    return time.time() - start_time


def get_csv_file_insertion_time(insertions, column=1):
    """
    get time to insert n rows with k column size in csv file.

    :param insertions: number of rows
    :param column: number of columns
    :return: time taken
    """
    out_str = "data," * column
    out_file = csv.writer(open('temp.csv', 'w'))
    start_time = time.time()

    for counter in range(0, insertions):
        out_file.writerow(out_str.split(','))

    return time.time() - start_time


if __name__ == '__main__':
    # Max Insertion and column Size
    max_write_size = int(input("Max Data Write Size : "))
    no_of_columns = int(input("Number of Columns : "))

    time_dictionary = {}

    time_data_csv = csv.writer(open('txt_csv_%s.csv' % max_write_size, 'w'))
    time_data_csv.writerow('Insertions,Txt file time, csv file time'.split(','))

    for count in range(1, max_write_size + 1):
        time_dictionary['txt_file_time'] = get_txt_file_insertion_time(
            count, no_of_columns)

        time_dictionary['csv_file_time'] = get_csv_file_insertion_time(
            count, no_of_columns)

        time_data_csv.writerow(('%s,%s,%s'
                                % (count
                                   , time_dictionary['txt_file_time']
                                   , time_dictionary['csv_file_time'])
                                ).split(','))

        print("%s Insertions" % count)

    os.remove('temp.txt')
    os.remove('temp.csv')
    print("Completed")


