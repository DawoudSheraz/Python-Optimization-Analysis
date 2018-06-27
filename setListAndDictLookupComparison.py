import csv
import time


def datastructurelookuptime(data_structure, entry_searched):
    start_time = time.time()
    if entry_searched in data_structure:
        return time.time() - start_time
    else:
        return 0


data_size = int(input("data Size ?"))

# Data Structures Generation
data_list = list(range(data_size))
data_dictionary = {}
for count in range(0, data_size):
    data_dictionary[count] = count
data_set = set(data_list)

# output File
output_file = open("list_vs_Dict_vs_Set_csv_" + str(data_size) + ".csv", "a")
csv_writer = csv.writer(output_file, delimiter=',')

time_dict = {}

for each_entry in range(0, data_size):

    # List Search Time
    time_dict["list_lookup"] = datastructurelookuptime(data_list, each_entry)

    # Dictionary Key lookup time
    time_dict["dict_key_lookup"] = datastructurelookuptime(data_dictionary, each_entry)

    # Set Lookup time
    time_dict["set_lookup"] = datastructurelookuptime(data_set, each_entry)

    # Saving the Data
    csv_writer.writerow((str(each_entry)
                         + ","
                         + str(time_dict["list_lookup"])
                         + ","
                         + str(time_dict["dict_key_lookup"])
                         + ","
                         + str(time_dict["set_lookup"]))
                        .split(","))

    print("Entry : " + str(each_entry) + " Searched")

output_file.close()
