import csv
import time
data_size = int(input("data Size ?"))

# output csv file with time logs
output_file = open("time_csv_" + str(data_size) + ".csv", "a")
csv_writer = csv.writer(output_file, delimiter=',')

for list_size in range(1, data_size+1):
    list_1 = list(range(list_size))
    list_2 = list(range(list_size))

    # modify list with for loop and range operator
    start_time = time.time()
    for iterator in range(0, len(list_1)):
        list_1[iterator] = list_1[iterator] * 2

    for_loop_time = time.time() - start_time

    # list Comprehension
    start_time = time.time()
    list_2 = [x * 2 for x in list_2]
    comprehension_end_time = time.time() - start_time

    # Writing the data
    csv_writer.writerow((str(list_size)
                         + ","
                         + str(for_loop_time)
                         + ","
                         + str(comprehension_end_time))
                        .split(","))


