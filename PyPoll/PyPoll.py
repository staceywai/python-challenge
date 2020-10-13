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
    electiondata = csv.reader(csvfile, delimiter=",")

    # Define the header 
    electiondata_header = next(electiondata)

    # define variables
    total_votes = 0 
    vote = 0
    candidate_list = {}
    listofcandidates = []

   # Read each row of data after the header
    for row in electiondata:
        # read the value in each row
        total_votes += 1
        # grab all candidate list
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.update({candidate:1})
            listofcandidates.append(candidate)
        else: candidate_list[candidate] +=1

print(f'\n',
'Election Results','\n',
'Total Votes: ', total_votes,'\n',
'-------------------------')
#kv = keyvalue count
kvcount = -1
for row in listofcandidates:
    # define number of iterations of for loop
    kvcount += 1
    print(f'',listofcandidates[kvcount],':',
    '{:0.2%}'.format((candidate_list[listofcandidates[kvcount]]/total_votes)),'(',
    candidate_list[listofcandidates[kvcount]],')')
print(f'-------------------------','\n',
'Winner:',max(candidate_list, key=candidate_list.get))

# output to txt file
with open('ElectionResults.txt', 'w') as text_file:
    print(f'\n',
    'Election Results','\n',
    'Total Votes: ', total_votes,'\n',
    '-------------------------',
    file=text_file)
    kvcount = -1
    for row in listofcandidates:
        kvcount += 1
        print(f'',listofcandidates[kvcount],':',
        '{:0.2%}'.format((candidate_list[listofcandidates[kvcount]]/total_votes)),'(',
        candidate_list[listofcandidates[kvcount]],')',
        file=text_file)
    print(f'-------------------------','\n',
    'Winner:',max(candidate_list, key=candidate_list.get),'\n',
    file=text_file)