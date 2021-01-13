
import csv

 # Initialize Variables with Values
total_months = 0
grt_increase = 0
increase_date=""
grt_decrease = 0
decrease_date = ""
row_count = 0
net_total = 0
sum_of_changes = 0

list_profit_loss = []
list_dates = []
changes = []

csvpath = 'Resources/budget_data.csv'

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Calculate total months in the dataset
    #Create list of profit/loss values
    #Create list of date values that correspond with profit/loss values
    for r in csvreader:
        #value from profit column
        profit_loss = int(r[1])
        #list of profits
        list_profit_loss.append(profit_loss)  
        #list of dates corresonding to profits  
        list_dates.append(r[0])
        #number or rows equals number of month
        row_count = row_count + 1
        #total of values from profit column
        net_total = net_total + profit_loss

#FIRST FOR LOOP       
# Calculate diffs in the list of PNLs
#pnl_count = len(list_profit_loss)  # how many items are in this list?
for i in range(row_count - 1):
    this_row = list_profit_loss[i]
    next_row = list_profit_loss[i + 1]
    #print(list_of_pnls[i])
    changes.append(abs(next_row - this_row))

#SECOND FOR LOOP
#For loop to get greatest increase and decrease plus dates they occur
for i in range(row_count):
    if list_profit_loss[i] > grt_increase:
        grt_increase = list_profit_loss[i]
        increase_date = list_dates[i]
    elif list_profit_loss[i] < grt_decrease:
        grt_decrease = list_profit_loss[i]
        decrease_date = list_dates[i]

for c in changes:
    sum_of_changes = sum_of_changes + c 

# print(sum_of_changes)
average_change = round(sum_of_changes / len(changes))

#Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${grt_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${grt_decrease})")