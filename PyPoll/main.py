import csv
import os

# Initialize variables
poll_data = []
csvpath = os.path.join('Resources', 'election_data.csv')

# Utilities
# def get_row_by_key_value(iterable_data, key, value):
#     """
#     Returns a row from an iterable where key=value
#
#     :param iterable_data: The iterable data (list, dict, etc.) to lookup
#     :param key: The key of the row we want to test
#     :param value: The value of iterable_data[key] that must match to return the row
#     :return: one iteration (a row) of an iterable (list, dict, etc.) where iterable_data[value] == key
#     """

#     for item in iterable_data:
#         if item[key] == value:
#             return item

# Read data in from CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile)

    # Read each row of data after the header
    for line in csvreader:
        poll_data.append(line)

    # Close file
    csvfile.close()

total_votes = sum([(lambda x:int(x['Voter ID']))(row) for row in poll_data])


print ("Election Results")
print ("-----------------------------")
print('Total number of Votes: %d' % len(poll_data))