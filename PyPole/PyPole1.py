import os
import csv

filename= "poll_data.csv"
totalv= 0
votes= {}

poll_data = os.path.join('..', 'PyPole', 'poll_data.csv')
with open(poll_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    for row in csvreader:    
    
        totalv = totalv + 1
                
    if row[2] in votes:
        votes[row[2]]+=1
                    
    else:
        votes[row[2]] = 1
                    
                    
print("Election Results")
print("Total Votes: " + str(totalv))
print("Winner: " + max(votes, key = votes.get))
