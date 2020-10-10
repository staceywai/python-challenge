# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# modules
import os
import csv

# set path
csvpath = os.path.join("Resources","budgetdata.csv")

# read in CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # Define the header 
    csv_header = next(csvreader)
    # print(csv_header)
# define variables
    old_month = 0
    new_month = 0
    month_count = 0
    total_value = 0
    PL_change_current = 0
    PL_change_total = 0
 
   # Read each row of data after the header
    for row in csvreader:
        # new_value = old_value + int(row[1])
        # read the value in each row
        month_count = month_count + 1
        total_value += int(row[1])
        # define average change over period of time
        if month_count == 1:
            new_month = int(row[1])
        old_month = new_month   
        print(f"old month", old_month)
        new_month = int(row[1])
        print(f"new month",new_month)
        # PL_change_old = PL_change_current
        # print(f"Profit change old", PL_change_old)
        PL_change_current = new_month - old_month
        print(f"profit change current", PL_change_current)
        PL_change_total = PL_change_total + PL_change_current
        print(f"profit change total", PL_change_total)



# Print table summary
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: ", month_count)
print("Total: $", total_value)
print("Average Change: ",PL_change_total/(month_count-1))
print("Greatest Increase: ")
print("Greatest Decrease in Profits: ")

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# 	•	The total number of months included in the dataset

# 	•	The net total amount of "Profit/Losses" over the entire period

# 	•	The average of the changes in "Profit/Losses" over the entire period
        
# 	•	The greatest increase in profits (date and amount) over the entire period

# 	•	The greatest decrease in losses (date and amount) over the entire period

