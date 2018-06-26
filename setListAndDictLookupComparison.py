import csv
import time
data_size = int(input("data Size ?"))
# Generating list, dictionary and set
data_list = list(range(data_size))
data_dictionary = {}
for count in range(0, data_size):
    data_dictionary[count] = count

data_set = set(data_list)

# output File
output_file = open("list_vs_Dict_vs_Set_csv_" + str(data_size) + ".csv", "a")
csv_writer = csv.writer(output_file, delimiter=',')

# time storage dictionary
time_dict = {}
for each_entry in range(0, data_size):
    # List Search Time
    start_time = time.time()
    if each_entry in data_list:
        time_dict["list_lookup"] = time.time() - start_time

    # Dictionary Key lookup time
    start_time = time.time()
    if each_entry in data_dictionary:
        time_dict["dict_key_lookup"] = time.time() - start_time

    # Set Lookup time
    start_time = time.time()
    if each_entry in data_set:
        time_dict["set_lookup"] = time.time() - start_time

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
