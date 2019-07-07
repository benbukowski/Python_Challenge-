import os
import csv


filename= "budget_data.csv"
profit = []
monthly_changes = []
date = []

mcount = 0
total_profit = 0
totalcp = 0
initial_profit = 0


budget_data = os.path.join('..', 'PyBank', 'budget_data.csv')
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        
        mcount = mcount + 1
        date.append(row[0])
        
        total_profit = total_profit + int(row[1])
        profit.append(row[1])
        
   
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
       
        monthly_changes.append(monthly_change_profits)
        
        totalcp = totalcp + monthly_change_profits
        
        initail_profit = final_profit 
        
        totalcp = (totalcp / mcount)
      
   
        
        
        
print("-------------------------------------")
print("Financial Analysis")
print("Total Months:" + str(mcount))
print("Total Profit:" + "$" + str(total_profit))
print("Average Change:" + "$" + str(int(totalcp)))



      
        