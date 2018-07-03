import csv
import time


def get_concate_through_plus_time(current_value, addition):
    """
    :param current_value: string on which concats will be done
    :param addition : specifies number of concats to be done
    :returns: time taken to do the concats through + operator
    """
    start_time = time.time()
    for counter in range(0, addition):
        current_value = current_value + str(counter)

    return current_value, time.time() - start_time


def get_concate_percentage_time(current_value, addition):
    """
    :param current_value: string on which concats will be done
    :param addition : specifies number of concats to be done
    :returns: time taken to do the concats through % operator
    """
    start_time = time.time()
    for counter in range(0, addition):
        current_value = "%s%s" % (current_value, counter)

    return current_value, time.time() - start_time


def get_concate_format_time(current_value, addition):
    """
    :param current_value: string to be concated through format operator
    :param addition : specifies number of concats to be done
    :returns: time taken to do the concats through format operator
    """
    start_time = time.time()
    for counter in range(0, addition):
        current_value = "{}{}".format(current_value, counter)

    return current_value, time.time() - start_time


data_size = int(input("data Size ?"))

output_file = open("concat_" + str(data_size) + ".csv", "w")
csv_writer = csv.writer(output_file, delimiter=',')

# CSV header added
csv_writer.writerow("number_of_concats"
                    ","
                    "+ concat"
                    ","
                    "% concat"
                    ","
                    "format_concat"
                    .split(","))

time_dict = {}

for count in range(0, data_size):
    string_1 = ""
    string_2 = ""
    string_3 = ""

    # "+" concat time
    string_1, time_dict["plus_concat"] = get_concate_through_plus_time(
                                                        string_1, count)

    # "%" concat time
    string_2, time_dict["percentage_concat"] = get_concate_percentage_time(
                                                        string_2, count)

    # "format" concat time
    string_3, time_dict["format_concat"] = get_concate_format_time(
                                            string_3, count)

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


