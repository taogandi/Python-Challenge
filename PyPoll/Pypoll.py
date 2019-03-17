import os
import csv

# Source Path

pypoll_file = os.path.join("Resources","election_data.csv")

# Set Initil values

count = 0
list_candidates = []
unique_candidate = []
vote_count = []
Percent_of_vote = []

# Open file with csv reader

with open(pypoll_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
       
        count = count + 1
        # Create dictionary
        list_candidates.append(row[2])
        
  #counting votes 
    for x in set(list_candidates):
        unique_candidate.append(x)
  
        # # of votes for each of the candidates 
        y = list_candidates.count(x)
        vote_count.append(y)

        # total votes
        z = (y/count)*100
        Percent_of_vote.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
# printing results
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(Percent_of_vote[i],2)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Export to txt
with open('election_results.txt', 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write("Total Vote: " + str(count) + "\n")
    txt_file.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
            txt_file.write(unique_candidate[i] + ": " + str(round(Percent_of_vote[i],2)) +"% (" + str(vote_count[i]) + ")\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write("The winner is: " + winner + "\n")
    txt_file.write("---------------------------------------\n")