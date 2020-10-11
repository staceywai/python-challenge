# a. total votes cast (count)
# b. unique candidate list (append)
# c. total number of votes each candidate won (create dictionary)
# d. percentage of candidates
# e. the winner of the election based on popular vote (find max of values)


# modules
import os
import csv

# set file path
csvpath = os.path.join("PyPoll","Resources","electiondata.csv")

# read in CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # Define the header 
    csv_header = next(csvreader)
    # print(csv_header)

    # define variables
    total_votes = 0 

   # Read each row of data after the header
    for row in csvreader:
        # read the value in each row
        total_votes += 1


# with open(FILE TO LOAD) as electiondata.csv:
#   reader = csv.reader(electiondata)
#   discard the header row
#   next(reader)

# define variables
# total_votes = 0
# all_candidates_with_duplication = []
# begin looping through and gathering the data
#   for row in reader:
#     total_votes += 1
#     all_candidates_with_duplication.append(row[2])
#     if candidate_totals.get(row[2]):
#         candidate_totas(row[2]) +=1
#     else: candidate_totals[row[2]] = 1

# # Print Summary table
# for cancdidate_name, vote_total in candidate_totals:
#         print(candidate_name.items:())

print('Election Results')
print('-------------------------')
print(f'Total Votes: ', total_votes)
print('-------------------------')
print(f'Khan: 63.000% (2218231)')
print(f'Correy: 20.000% (704200)')
print(f'Li: 14.000% (492940)')
print(f'O Tooley: 3.000% (105630)')
print('-------------------------')
print(f'Winner: ')

