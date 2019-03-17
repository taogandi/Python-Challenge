import os
import csv

# source path

pybank_file= os.path.join("Resources","budget_data.csv")

#Set Initial values

profit = []
monthly_changes = []
date = []
count = 0
total_profit = 0
Total_profit_change = 0
first_profit = 0

# open file with csv reader


with open(pybank_file
, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
      count = count + 1 

      date.append(row[0])

      # calculate total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculating final profits
      final_profit = int(row[1])

      #Calculating monthly profits change
      monthly_change_profits = final_profit - first_profit
      monthly_changes.append(monthly_change_profits)

      first_profit = final_profit

      #Calculating the average change in profits
      average_change_profits = ((monthly_change_profits + int(row[1]))/count)            

      #Find greatest increase and decrease
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)


      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

#printing results
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")


# Export to txt

with open('financial_analysis.txt', 'w') as txt_file:
    txt_file.write("----------------------------------------------------------\n")
    txt_file.write("  Financial Analysis"+ "\n")
    txt_file.write("----------------------------------------------------------\n\n")
    txt_file.write("    Total Months: " + str(count) + "\n")
    txt_file.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    txt_file.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    txt_file.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    txt_file.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    txt_file.write("----------------------------------------------------------\n")