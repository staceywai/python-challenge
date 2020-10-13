# modules
import os
import csv

# set file path
csvpath = os.path.join("PyBank","Resources","budgetdata.csv")

# read in CSV
with open(csvpath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")

    # Define the header 
    budgetdata_header = next(budgetdata)

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
    Greatest_Increase_PL = 0
    Greatest_Decrease_month = 0
    Greatest_Decrease_PL = 0

   # Read each row of data after the header
    for row in budgetdata:
    
        # read the value in each row
        month_count = month_count + 1
        total_value += int(row[1])
        # define average change over period of time
        if month_count == 1:
            PL_new = int(row[1])
        PL_old = PL_new   
        PL_new = int(row[1])
        PLchange_current = PL_new - PL_old
        PLchange_total = PLchange_total + PLchange_current

        # Find greatest increase and decrease
        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = int(row[1])
            Greatest_Increase_month = row[0]
            Greatest_Increase_PL = PLchange_current
        if int(row[1]) < Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_month = row[0]
            Greatest_Decrease_PL = PLchange_current

# Print table summary
# print("Financial Analysis")
# print("------------------------------")
# print(f"Total Months: ", month_count)
# print(f"Total: $", total_value)
# print(f"Average Change: $",round(PLchange_total/(month_count-1),2))
# print(f"Greatest Increase: ", Greatest_Increase_month, "($",Greatest_Increase_PL,")")
# print(f"Greatest Decrease in Profits: ", Greatest_Decrease_month, "($",Greatest_Decrease_PL,")")


print(f'\n',
'Financial Analysis','\n',
'------------------------------','\n',
'Total Months:', month_count,'\n',
'Total: $', total_value,'\n',
'Average Change: $',round(PLchange_total/(month_count-1),2),'\n',
'Greatest Increase: ', Greatest_Increase_month, '($',Greatest_Increase_PL,')','\n',
'Greatest Decrease in Profits: ', Greatest_Decrease_month, '($',Greatest_Decrease_PL,')')

# output to txt file
with open('FinancialAnalysis.txt', 'w') as text_file:
    print(f'\n',
    'Financial Analysis','\n',
    '------------------------------','\n',
    'Total Months:', month_count,'\n',
    'Total: $', total_value,'\n',
    'Average Change: $',round(PLchange_total/(month_count-1),2),'\n',
    'Greatest Increase: ', Greatest_Increase_month, '($',Greatest_Increase_PL,')','\n',
    'Greatest Decrease in Profits: ', Greatest_Decrease_month, '($',Greatest_Decrease_PL,')','\n',
    file=text_file)

    


