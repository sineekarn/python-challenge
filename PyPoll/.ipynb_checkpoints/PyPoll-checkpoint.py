# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'NU-CHI-DATA-PT-11-2019-U-C', '03-Python', 'Python-HW', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

count = 0
canidate = {}
out = ""

# Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    out = out + "\n" +("Election Results")
    out = out + "\n" + ("----------------------")

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Count the total number of votes cast
    #Find a complete list of candidates who received votes
    for row in csvreader: 
        count = count +1
        name = row[2]

        if name in canidate.keys():
            canidate[name] = canidate[name]+1
        else:
            canidate[name] = 1

    out = out + "\n" + (f"Total Votes: {count}")
    out = out + "\n" + ("----------------------")

    #Calculate the percentage of votes each candidate won
    #Calculate the total number of votes each candidate won
    #Find the winner of the election based on popular vote.
    winner = ""
    winner_cnt = 0
    for key in canidate:
       
        out += "\n" + (f"{key}: {(canidate[key]/count):0.3%} ({canidate[key]})")
        if(canidate[key] > winner_cnt):
            winner_cnt = canidate[key]
            winner = key

out = out + "\n" + ("----------------------")
out += "\n" + (f"Winner: {winner}")
out = out + "\n" + ("----------------------") 

# Print the script 
print(out)


#Export a text file
os.remove("pyPoll_output.txt")
out_file = open("pyPoll_output.txt", "a")
out_file.write(out)     

    

    





















