
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import csv
import os
#google is now my friend <3
import collections
from collections import Counter

#Variables I want to use 
candidates = []
votes_by_candidate = []

#Open the CSV path for the data 
election_data = os.path.join("Resources","election_data.csv")

# Open and read the data csv file we are using 
with open(election_data, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

#Read through your rows 
    for row in csv_reader:

        #add in your candidates!
        candidates.append(row[2])

    # Sort 
    sorting = sorted(candidates)

    # arranging 
    arrange = sorting

    #vote counting and adding them in 
    count_candidate = Counter (arrange) 
    votes_by_candidate.append(count_candidate.most_common())
   
    # percent votes, 3 decimal places (thank you matplotlib tutorial for this! )
    for item in votes_by_candidate:

        firstplace = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        secondplace = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        thirdplace = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourthplace = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')

# Print SO many things using the f'{}

print("The Election Results")
print(f"Total Votes:  {sum(count_candidate.values())}")
print(f"{votes_by_candidate[0][0][0]}: {firstplace}% ({votes_by_candidate[0][0][1]})")
print(f"{votes_by_candidate[0][1][0]}: {secondplace}% ({votes_by_candidate[0][1][1]})")
print(f"{votes_by_candidate[0][2][0]}: {thirdplace}% ({votes_by_candidate[0][2][1]})")
print(f"{votes_by_candidate[0][3][0]}: {fourthplace}% ({votes_by_candidate[0][3][1]})")
print(f"Winner!!:  {votes_by_candidate[0][0][0]}")


# Text
election_file = os.path.join("Resources", "election_data.txt")

with open(election_file, "w") as outfile:

    outfile.write("The Election Results\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write(f"{votes_by_candidate[0][0][0]}: {firstplace}% ({votes_by_candidate[0][0][1]})\n")
    outfile.write(f"{votes_by_candidate[0][1][0]}: {secondplace}% ({votes_by_candidate[0][1][1]})\n")
    outfile.write(f"{votes_by_candidate[0][2][0]}: {thirdplace}% ({votes_by_candidate[0][2][1]})\n")
    outfile.write(f"{votes_by_candidate[0][3][0]}: {fourthplace}% ({votes_by_candidate[0][3][1]})\n")
    outfile.write(f"Winner!!:  {votes_by_candidate[0][0][0]}\n")

   