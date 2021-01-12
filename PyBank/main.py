import csv
import os


# Initialize variables
accounting_data = []
csvpath = os.path.join('Resources', 'budget_data.csv')

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
        accounting_data.append(line)

    # Close file
    csvfile.close()

# Result: Total Profit
total_profit = sum([(lambda x:int(x['Profit/Losses']))(row) for row in accounting_data])  # Total Sum of profit

# Result: Average Monthly Change
#  (PSEUDO CODE for the below):
#  for row in accounting_data:
#      if this is the first row, skip to next, else:
#      difference = this row - previous row
#      add difference to list

for idx, row in enumerate(accounting_data):
    if idx == 0:
        accounting_data[idx]['diff_from_prev_month'] = 0

        continue

    current_pl = int(row['Profit/Losses'])  # === int(accounting_data[idx]['Profit/Losses'])
    prev_pl = int(accounting_data[idx - 1]['Profit/Losses'])
    monthly_difference = current_pl - prev_pl
    accounting_data[idx]['diff_from_prev_month'] = monthly_difference

average_monthly_diff = sum([row['diff_from_prev_month'] for row in accounting_data]) / (len(accounting_data) - 1)

# Result: Greatest increase
#  greatest_increase_amt = max([row['diff_from_prev_month'] for row in accounting_data])
#  greatest_increase_row = get_row_by_key_value(accounting_data, 'diff_from_prev_month', greatest_increase_amt)

# Result: Greatest increase / decrease
greatest_increase_row = None
greatest_decrease_row = None

for row in accounting_data:
    if (not greatest_increase_row) or (row['diff_from_prev_month'] > greatest_increase_row['diff_from_prev_month']):
        greatest_increase_row = row

    if (not greatest_decrease_row) or (row['diff_from_prev_month'] < greatest_decrease_row['diff_from_prev_month']):
        greatest_decrease_row = row

# Output results
print('Financial Analysis')
print('----------------------------')
print('Total Months: %d' % len(accounting_data))
# print('Total Months: {}'.format(len(accounting_data)))
# print('Total Months: {total_months}'.format(total_months=len(accounting_data)))
print('Total: $%.2f' % total_profit)
print('Average  Change: $%0.2f' % average_monthly_diff)
print('Greatest Increase in Profits: {greatest_increase_date} ({profit_loss})'.format(
    greatest_increase_date=greatest_increase_row['Date'],
    profit_loss=greatest_increase_row['diff_from_prev_month']
))
print('Greatest Decrease in Profits: {greatest_decrease_date} ({profit_loss})'.format(
    greatest_decrease_date=greatest_decrease_row['Date'],
    profit_loss=greatest_decrease_row['diff_from_prev_month']
))
