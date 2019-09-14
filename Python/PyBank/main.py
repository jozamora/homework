#******************************************************************
#Jesus Zamora
#This project reads in financial data from a csv and then performs 
#different accounting functions. This prints to terminal and outputs text file.
#******************************************************************
import os
import csv

#Point to the correct file path
budgetCSV = os.path.join("Resources", "budget_data.csv")

countOfMonths = 0
netTotal = 0
dates = []
profitloss = []
sum = 0


#open and read in .csv file 
with open(budgetCSV, newline="") as csvfile:

    csvReader = csv.reader(csvfile,delimiter=',')
    next(csvReader) #Ignore header file and start gathering data at next line
    for row in csvReader:
        dates.append(row[0]) #Creates a list for the dates
        profitloss.append(row[1]) #Creats profit/loss list
        
        countOfMonths = len(dates) #Count thu number of months by getting length of dates
        netTotal += float(row[1]) #The sum of profit/loss column
        averageChange = netTotal/countOfMonths #Average change over the whole year
        maxProf = max(profitloss, key=float) #Find highest profit in list of profit/loss
        maxIndex = profitloss.index(max(profitloss, key=float))#Returns index of max profit
        minLoss = min(profitloss, key= float) #look for lowest loss 
        minIndex = profitloss.index(min(profitloss, key=float))#Return index of lowest loss
        
#Outputs to terminal
print("\nFinancial Analysis")
print("-----------------------------------------")
print(f"Total Months: {countOfMonths}")
print(f"Total: ${netTotal:.2f}")
print(f"Average Change : ${averageChange:.2f}")
print(f"Greatest Increase in Profits: "+ dates[maxIndex] + " " + maxProf)
print(f"Greatest Decrease in Loss: "+ dates[minIndex] + " " + minLoss)

#Outputs to output.txt
outputFile = open("Output.txt", "w")
outputFile.write("\nFinancial Analysis")
outputFile.write("\n-----------------------------------------")
outputFile.write(f"\nTotal Months: {countOfMonths}")
outputFile.write(f"\nTotal: ${netTotal:.2f}")
outputFile.write(f"\nAverage Change : ${averageChange:.2f}")
outputFile.write(f"\nGreatest Increase in Profits: "+ dates[maxIndex] + " " + maxProf)
outputFile.write(f"\nGreatest Decrease in Loss: "+ dates[minIndex] + " " + minLoss)
outputFile.close()