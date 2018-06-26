import csv
import time
data_size = int(input("data Size ?"))
# Generating list and dictionary
data_list = list(range(data_size))
data_dictionary = {}
for count in range(0, data_size):
    data_dictionary[count] = count

# output File
output_file = open("list_vs_Dict_csv_" + str(data_size) + ".csv", "a")
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

    # Dictionary Value lookup time
    # start_time = time.time()
    # for key, value in data_dictionary.items():
    #     if value == each_entry:
    #         time_dict["dict_value_lookup"] = time.time() - start_time
    #         break

    # Dictionary Key lookup time
    start_time = time.time()
    if data_dictionary[each_entry] in data_dictionary:
        time_dict["dict_value_lookup"] = time.time() - start_time

    csv_writer.writerow((str(each_entry)
                         + ","
                         + str(time_dict["list_lookup"])
                         + ","
                         + str(time_dict["dict_key_lookup"])
                         + ","
                         + str(time_dict["dict_value_lookup"]))
                        .split(","))

    print("Entry : " + str(each_entry) + " Searched")




