#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import csv
import os

#set variables - very similar to the VBA assignment?
months = []
profit_loss_changes = []
count_months = 0
net_amount_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

# file path for your data set that you are using 
pybank_csv=os.path.join("Resources","budget_data.csv")

# Open CSV/read it
with open(pybank_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    #header row 
    csv_header = next(csvfile)

    for row in csv_reader:

        # month count 
        count_months += 1

        # profit/losses
        current_profit_loss = int(row[1])
        net_amount_profit_loss += current_profit_loss

        if (count_months == 1):

            # values need to be equal 
            previous_profit_loss = current_profit_loss

        else:

            #what is the change between current and previous???
            profit_loss_change = current_profit_loss - previous_profit_loss

           #add in the months 
            months.append(row[0])

            # next we want to add in p/l 
            profit_loss_changes.append(profit_loss_change)

            # loop it! 
            previous_profit_loss = current_profit_loss

    #Sum (add together) 
    sum_profit_loss = sum(profit_loss_changes)

    # average it out and divide your sum by the months 
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    #MAX aka high amount of change and MIN aka low amount of change  
    high_change = max(profit_loss_changes)
    low_change = min(profit_loss_changes)

    # Locate the high and low amounts over time 
    high_month = profit_loss_changes.index(high_change)
    low_month = profit_loss_changes.index(low_change)

    # months 
    best = months[high_month]
    worst = months[low_month]

print(f"Total Months:  {count_months}")
print(f"Total:  ${net_amount_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best} (${high_change})")
print(f"Greatest Decrease in Losses:  {worst} (${low_change})")

#text files 
budget_file = os.path.join("Resources", "budget_data.txt")

#google helped with this 
with open(budget_file, "w") as outfile:

    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_amount_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best} (${high_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst} (${low_change})\n")