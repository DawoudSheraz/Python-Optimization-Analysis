import csv
import time


def get_lookup_time(data_structure, entry_searched):
    """
    :param data_structure: in which entry will be searched using "in"
    :param entry_searched : value to be searched
    :returns: time taken to search, 0 if not found
    """
    start_time = time.time()
    if entry_searched in data_structure:
        return time.time() - start_time
    else:
        return 0


def get_dictionary_value_lookup_time(dictionary, entry_searched):
    """
    :param dictionary: dictionary whose values will ne searched
    :param entry_searched : value to be searched
    :returns: time taken to search, 0 if not found
    """
    start_time = time.time()
    if dictionary[entry_searched] in dictionary:
        return time.time() - start_time
    return 0


data_size = int(input("data Size ?"))

# Data Generation
data_list = list(range(data_size))
data_dictionary = {}
for count in range(0, data_size):
    data_dictionary[count] = count

output_file = open("list_vs_Dict_csv_" + str(data_size) + ".csv", "w")
csv_writer = csv.writer(output_file, delimiter=',')

# CSV header added
csv_writer.writerow(("searched_entry,list_lookup,"
                    "dict_key_lookup,dict_value_lookup")
                    .split(","))

time_dict = {}

for each_entry in range(0, data_size):

    # List Search Time
    time_dict["list_lookup"] = get_lookup_time(data_list, each_entry)

    # Dictionary Key lookup time
    time_dict["dict_key_lookup"] = get_lookup_time(data_dictionary, each_entry)

    # Dictionary value lookup time
    time_dict["dict_value_lookup"] = get_dictionary_value_lookup_time(data_dictionary, each_entry)

    csv_writer.writerow((str(each_entry)
                         + ","
                         + str(time_dict["list_lookup"])
                         + ","
                         + str(time_dict["dict_key_lookup"])
                         + ","
                         + str(time_dict["dict_value_lookup"]))
                        .split(","))

    print("Entry : " + str(each_entry) + " Searched")

output_file.close()


