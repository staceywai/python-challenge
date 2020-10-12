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
    print(f'candidate:',candidate_list[candidate])
    print(listofcandidates)
    print(listofcandidates[0])
    candidate_count = len(listofcandidates)
    print(len(listofcandidates))


#calculate values
    # for candidate in candidate_list:
    #     candidate_vote_total = candidate_list[candidate]
    # print(f'candidate votes:', candidate_vote_total)
    # candidate_percentage = candidate_vote_total/total_votes
    # print(f'candidate percentage:', candidate_percentage)


print('Election Results')
print(f'Total Votes: ', total_votes)
print('-------------------------')

print_count = -1
for x in listofcandidates:
    # define number of iterations of for loop
    print_count += 1
    print(f'',listofcandidates[print_count],":","{:0.2%}".format((candidate_list[listofcandidates[print_count]]/total_votes)),"(", candidate_list[listofcandidates[print_count]],")")
    # listofcandidates[row],"{:0.2%}".format((candidate_list[listofcandidates[row]]/total_votes)), candidate_list[listofcandidates[row]])
print('-------------------------')
# print(f'Khan',"{:0.2%}".format((candidate_list['Khan']/total_votes)), candidate_list['Khan'])
# print(f'Correy:', "{:0.2%}".format((candidate_list['Correy']/total_votes)), candidate_list['Correy'])
# print(f'Li:', "{:0.2%}".format((candidate_list['Li']/total_votes)), candidate_list['Li'])
# print(f'O Tooley:', "{:0.2%}".format((candidate_list["O'Tooley"]/total_votes)), candidate_list["O'Tooley"])
# print('-------------------------')
print(f'Winner:',max(candidate_list, key=candidate_list.get))
