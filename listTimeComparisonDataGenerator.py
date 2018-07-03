import csv
import time


def get_for_loop_time(data_list):
    """
    :param data_list: list to be modified through for loop
    :returns: time taken to modify the list
    """
    start_time = time.time()
    for iterator in range(0, len(data_list)):
        data_list[iterator] = data_list[iterator] * 2

    return time.time() - start_time


def get_list_comprehension_time(data_list):
    """
    :param data_list: list to be modified through list comprehension
    :returns: tuple( time taken for modification, modified list)
    """
    start_time = time.time()
    data_list = [x * 2 for x in data_list]

    return (time.time() - start_time), data_list


data_size = int(input("data Size ?"))

# output csv file with time logs
output_file = open("time_csv_" + str(data_size) + ".csv", "w")
csv_writer = csv.writer(output_file, delimiter=',')

# CSV header added
csv_writer.writerow("list_size,for_loop,list_comprehension"
                    .split(","))


for list_size in range(1, data_size+1):
    list_1 = list(range(list_size))
    list_2 = list(range(list_size))

    for_loop_time = get_for_loop_time(list_1)

    comprehension_end_time, list_2 = get_list_comprehension_time(list_2)

    # Output the Time values to csv file
    csv_writer.writerow((str(list_size)
                         + ","
                         + str(for_loop_time)
                         + ","
                         + str(comprehension_end_time))
                        .split(","))
    print("List size : %s done" % list_size)

output_file.close()
