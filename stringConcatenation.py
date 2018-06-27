import csv
import time


# Addition specifies the concatenations to the current value
def concatethroughplus(current_value, addition):

    start_time = time.time()
    for counter in range(0, addition):
        current_value = current_value + str(counter)

    return current_value, time.time() - start_time


def concatepercentage(current_value, addition):

    start_time = time.time()
    for counter in range(0, addition):
        current_value = "%s%s" % (current_value, counter)

    return current_value, time.time() - start_time


def concateformat(current_value, addition):
    start_time = time.time()
    for counter in range(0, addition):
        current_value = "{}{}".format(current_value, counter)

    return current_value, time.time() - start_time


data_size = int(input("data Size ?"))

output_file = open("concat_" + str(data_size) + ".csv", "a")
csv_writer = csv.writer(output_file, delimiter=',')

time_dict = {}

for count in range(0, data_size):
    string_1 = ""
    string_2 = ""
    string_3 = ""

    # "+" concat time
    string_1, time_dict["plus_concat"] = concatethroughplus(string_1, count)

    # "%" concat time
    string_2, time_dict["percentage_concat"] = concatepercentage(string_2, count)

    # "format" concat time
    string_3, time_dict["format_concat"] = concateformat(string_3, count)

    csv_writer.writerow((str(count + 1)
                         + ","
                         + str(time_dict["plus_concat"])
                         + ","
                         + str(time_dict["percentage_concat"])
                         + ","
                         + str(time_dict["format_concat"]))
                        .split(","))

    print(str(count + 1) + " concatenations done")

output_file.close()


