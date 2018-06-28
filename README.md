### NOTE: All the scripts are compatible only with Python 3.6. To run them on Python 2.7, the modifications will be required.

Python provides with the various data structures, with famous examples of list, dictionary, set and tuple. One of the major aspect of the python data structures is the ease of getting things done. Each data structure provides features that are easy to use. e.g. to search any key inside a dictionary, an operator of "in" is used. However, when we talk about in term of performance, not all data structures prove to be useful. This repository will provide with different scripts, that apply various operations in accordance to different data structres and save the resultant data in csv files.
 
 ---- From This point, each script in the main folder will be explained.
 
 # 1. listTimeComparisonDataGenerator.py
 
## Description: 
Python provides numerous ways to iterate over a list and access its data. By accessing the data, other operations like data modification, data updation etc. can be done. This script focuses on two iteration methods: for loop iteration and list comprehension. In the script, two lists of equal size and same elements in created. The modification done is same in both cases, which is the doubling each element of the list. One list is modified through regular for loop with range function while second is modified through list comprehension.

## Usage: 
On running the script, user is asked with "Data Size". Data size is the upper limit on how many lists should be created. This provides a linear increase in the data and gives a relatively large amount of data. This is the only input and then program runs and generates the csv file in the same folder as script. The csv file will have three columns: first column is the list size, second column in the time taken by for loop and third column is the time taken by the list comprehension. Sample data files for the scripts are present inside the "listTimeData" folder.


# 2. listAndDictionaryLookupComparison.py

## Description:
Data searching is one of the significant requirement when dealing with data. Each data structure provides with different time complexities for looking up data. This script focuses on the dictionaries and list. Three lookups are done: first is inside a list, second one is inside dictionary keys and third one inside the dictionary values. Given a number, all three lookups are done and time for each lookup is calculated. No explict loops are used for the searching. The default search features by the python are used. This aims to find which data structure is time costly for searching.

## Usage:
On running the script, the data size will be required from the user. That data size is used for two purposes:
     a. To create list from 0, data size - 1.
     b. to create dictionary with key=value i.e. 0=0, 1=1 and so on.
After the input, the list and dictionary are created and data is looped from 0 to data size -1. For each entry, it is searched in previously mentioned three ways and the data is stored inside the csv. The csv contains the four columns: first column is entry search, second is the time taken to search inside list, third is lookup time for dictionary key and fourth is the search time for the dictionary value. Sample data file is present inside "DictVsListLookup" folder.


# 3. setListAndDictLookupComparison.py

## Description:
This script is an extension of "listAndDictionaryLookupComparison". This script provides the data for lookup time of list, set and dictionary in python. For dictionary, only the "key" lookup time has been considered.

## Usage:
The usage is also very same to the "listAndDictionaryLookupComparison.py". The difference is in the csv file. From the 4 columns, the first is the searched entry, second is the list lookup time, third is the dictionary key lookup time and fourth is the set lookup time. A sample output file is present inside the "ListVsDictVsSet Lookup Time Data" folder.

# 4. stringConcatenation.py

## Description
String concatenation is one of the commonly used feature. Python provides various ways to concate different string. Most notably are:
   - "+" operator
   - % operator
   - {} with format
  The choice of each method is subjective. But when it comes to time complexity, not all might be efficient.
  
 ## Usage
 On starting the program, user is prompted for Data Size. The data size specifies the max number of concatenations done to a string, starting from 1. From 1 to onwards, the concatenations are done by 3 methods and their time taken is saved to csv file. The csv comprises of 4 columns as:
   1. Concatenations Done
   2. Time with "+" operator
   3. Time with "%" operator
   4. Time with "{} with format" operator
