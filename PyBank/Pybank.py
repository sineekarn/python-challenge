# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = ('budget_data.csv')

count = 0
profit_losses = 0
previous_profit_losses = 0
current_profit_losses = 0 
change_profit_losses = 0
total_change_profit_losses = 0
average = 0
current_greatest_increase = 0
current_greatest_increase_month = ""
current_greatest_decrease = 0
current_greatest_decrease_month = ""
out = ""

# Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    out = out + "\n" + ("Financial Analysis")
    out = out + "\n" + ("---------------------------")
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Count the total number of months included in the dataset
    #Calculate the net total amount of "Profit/Losses" over the entire period
    #Calculate the greatest increase in profits (date and amount) over the entire period
    #Calculate the greatest decrease in losses (date and amount) over the entire period
    
    for row in csvreader:
        count = count + 1
        profit_losses = profit_losses +  int(row[1])
        print(row)
        current_profit_losses = int(row[1]) 
        if previous_profit_losses != 0:
            change_profit_losses = current_profit_losses - previous_profit_losses
            total_change_profit_losses = total_change_profit_losses + change_profit_losses
        
        previous_profit_losses = current_profit_losses

        if change_profit_losses > current_greatest_increase:
            current_greatest_increase = change_profit_losses
            current_greatest_increase_month = row[0]
        
        if change_profit_losses < current_greatest_decrease:
            current_greatest_decrease = change_profit_losses
            current_greatest_decrease_month = row[0]

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    # Format for Float Precision
    average = total_change_profit_losses/(count-1)
    formataverage = format(average,'.2f')
       
    out = out + "\n" + ("Total months: " +str(count)) 
    out = out + "\n" + (f"Total: ${profit_losses}") 
    out = out + "\n" + ("Average change: $" + str(formataverage))
    out = out + "\n" + (f"Greatest Increase in Profits: {current_greatest_increase_month} (${current_greatest_increase})")
    out = out + "\n" + (f"Greatest Decrease in Profits: {current_greatest_decrease_month} (${current_greatest_decrease})")

# Print the script 
print(out)

#Export a text file
os.remove("pybank_output.txt")
out_file = open("pybank_output.txt", "a")
out_file.write(out) 
    

