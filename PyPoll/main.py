import csv

#  * The total number of votes cast
total_votes = 0
#  * A complete list of candidates who received votes
candidate_list=[]
#  * The total number of votes each candidate won
voter_results = []
#  * The percentage of votes each candidate won
percent_vote = []
# Track the winner of the election based on popular vote.
#  * win_value tracks highes number of votes
#  * winner tracks name of candidate with most votes
win_value = 0
winner = ""
#  * This counter keeps track of how many candidates we have
can_counter = 0
#  * pointer used to map by index results for each candidate to voter_results.
#initialize pointer for relative index of candidate
pointer = 0

#  * value is use to pull candidate's vote tally out of voter_results list and iterate the tally for that candidate
value = 0

#  * Set relative path to csv data set
csvpath = 'Resources/election_data.csv'

#Open CSV file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        #Track total votes in dataset
        total_votes = total_votes + 1
        #create list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2]) 
    # Set counter to number of candidates being tallied
    can_counter = len(candidate_list)
    #put correct number of indexed values in voter result list so that voter result of each candidate can be stored.
    for i in range(can_counter):
        voter_results.insert(i, 0)

#Open CSV file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Calculate total months in the dataset
    # print(f"This is voter results {voter_results}")###TEST CODE
    test_var = 0
    #Count Votes for each candidate
    for row in csvreader:
        #index of current candidate in candidate_list
        pointer = candidate_list.index(row[2])
        value = voter_results[pointer]
        value += 1
        voter_results[pointer]= value
        test_var += 1

#Match candidate_list with voter_results
#Iterate value for corrosponding candidate
for i in range(can_counter):
    candidate = candidate_list[i] 
    if voter_results[i] > win_value:
        win_value = voter_results[i]
        winner = candidate
        
print(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''')

# pThis for loop will calcuate percentage of total votes per candidate
for i in range(can_counter):
    candidate = candidate_list[i] 
    percent_vote = voter_results[i] / total_votes * 100
    print(f"{candidate_list[i]}: {round(percent_vote, 3)}% ({voter_results[i]})")

print(f'''-------------------------
Winner: {winner} with {win_value}
------------------------- ''')