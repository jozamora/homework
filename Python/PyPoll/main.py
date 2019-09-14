#******************************************************************
#Jesus Zamora
#This project reads in a voter data csv files and then counts the number
#of votes for each candidate and find the winner. Outputs to terminal and file.
#******************************************************************
import os
import csv
import collections

#Point to the correct file path
electionCSV = os.path.join("Resources", "election_data.csv")


#setup variables that will be used
candidates = set()
totalVotes = 0
lCounter = 0
kCounter = 0
oCounter = 0
cCounter = 0

#open and read in .csv file 
with open(electionCSV, newline="") as csvfile:

	csvReader = csv.reader(csvfile,delimiter=',') 
	next(csvReader) #Ignore header file and start gathering data at next line
	
	for row in csvReader:
		column = row[2] #Candidate column
		
		totalVotes += 1 #Vote counter
		candidates.add(row[2]) #Create set to see unique candiates for testing purposes
		
		#Go through and count votes for each indivual cnadidate
		if column == 'Li': 
			lCounter += 1
		elif column == 'Khan':
			kCounter += 1
		elif column == 'Correy':
			cCounter += 1
		elif column == 'O\'Tooley':
			oCounter += 1
		
		#Holds values of the counters
		tempList = [lCounter, kCounter, cCounter, oCounter]
	
		#Find highest vote count
		tempWin = max(tempList, key=int)
		
#Go through and see which candidate has higher number of votes
#by comparing the result of the max function		
if tempWin == lCounter:
	winner = 'Li'
elif tempWin == kCounter:
	winner = 'Khan'
elif tempWin == cCounter:
	winner = 'Correy'
elif tempWin == oCounter:
	winner = 'O\'Tooley'

#Calculate percentages	
kPercent = (kCounter/totalVotes)*100
cPercent = (cCounter/totalVotes)*100
lPercent = (lCounter/totalVotes)*100
oPercent = (oCounter/totalVotes)*100

#Print to terminal	
print("\nElection Results")
print("-----------------------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------------------")

print(f"Khan: {kPercent:.2f}" + "% " f"({kCounter})")
print(f"Correy: {cPercent:.2f}" + "% " f"({cCounter})")
print(f"Li: {lPercent:.2f}" + "% " f"({lCounter})")
print(f"O\'Tooley: {oPercent:.2f}" + "% " f"({oCounter})")
print("-----------------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------------")

#Write to output.txt
outputFile = open("Output.txt", "w")
outputFile.write("\nElection Results")
outputFile.write("\n-----------------------------------------")
outputFile.write(f"\nTotal Votes: {totalVotes}")
outputFile.write("\n-----------------------------------------")
outputFile.write(f"\nKhan: {kPercent:.2f}" + "% " f"({kCounter})")
outputFile.write(f"\nCorrey: {cPercent:.2f}" + "% " f"({cCounter})")
outputFile.write(f"\nLi: {lPercent:.2f}" + "% " f"({lCounter})")
outputFile.write(f"\nO\'Tooley: {oPercent:.2f}" + "% " f"({oCounter})")
outputFile.write("\n-----------------------------------------")
outputFile.write(f"\nWinner: {winner}")
outputFile.write("\n-----------------------------------------")
outputFile.close()

