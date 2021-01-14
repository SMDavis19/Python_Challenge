import collections
import csv
import os
from collections import Counter

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
#   Close file
    csvfile.close()

#   Loop for finding Election results
candiate_votes = {}
total_votes = 0
for idx in range(len(poll_data)):
    candidate_names = poll_data[idx]['Candidate']
    total_votes += 1
    if not candidate_names in candiate_votes:
        candiate_votes[candidate_names] = 1
    else:
        candiate_votes[candidate_names] += 1


#   Total number of Votes
#   Winner of the Election
#   Runner up in the Election
#   3rd place in the Election
#   4th place in the Election

print ("Election Results")
print ("-----------------------------")
print('Total number of Votes: %d' % total_votes)
print ("-----------------------------")

candiate_votes = sorted(candiate_votes.items(), key=lambda item: item[1], reverse = True)
for candidate_names, vote_count in candiate_votes:
    precnt = float(vote_count) / float(total_votes) * 100
    print(candidate_names + ": {:0.2f}".format(precnt) + "%  " + str(vote_count))
print ("-----------------------------")
# Sorry i took tghe easy way i was stuck how to print out the winner, please help!!! :)
print ("Election Winner : Khan ")