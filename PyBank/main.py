
# modules
import os
import csv

# set file path
csvpath = os.path.join("Resources","budgetdata.csv")

# read in CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # Define the header 
    csv_header = next(csvreader)
    # print(csv_header)
# define variables
    PL_old = 0
    PL_new = 0
    month_count = 0
    total_value = 0
    PLchange_current = 0
    PLchange_total = 0
    Greatest_Increase = -9999999999
    Greatest_Decrease = 99999999999
    Greatest_Increase_month = 0
    Greatest_Decrease_month = 0
   # Read each row of data after the header
    for row in csvreader:
    
        # read the value in each row
        month_count = month_count + 1
        total_value += int(row[1])
        # define average change over period of time
        if month_count == 1:
            PL_new = int(row[1])
        PL_old = PL_new   
        print(f"PL old", PL_old)
        PL_new = int(row[1])
        print(f"PL new",PL_new)
        # PL_change_old = PL_change_current
        # print(f"Profit change old", PL_change_old)
        PLchange_current = PL_new - PL_old
        print(f"profit change current", PLchange_current)
        PLchange_total = PLchange_total + PLchange_current
        print(f"profit change total", PLchange_total)

        # Find greatest increase and decrease
        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = int(row[1])
            print(f'GreatestIncrease',Greatest_Increase)
            Greatest_Increase_month = row
        if int(row[1]) < Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_month = row
            print(f'GreatestIncrease',Greatest_Decrease)



# Print table summary
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: ", month_count)
print("Total: $", total_value)
print("Average Change: ",PLchange_total/(month_count-1))
print("Greatest Increase: ",Greatest_Increase_month, Greatest_Increase)
print("Greatest Decrease in Profits: ", Greatest_Decrease_month, Greatest_Decrease)

        
# 	•	The greatest increase in profits (date and amount) over the entire period

# 	•	The greatest decrease in losses (date and amount) over the entire period

