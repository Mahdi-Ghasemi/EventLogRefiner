

#####################################################################################################################
# This tool gets two CSV files as input and generates a new CSV file as output. One CSV file is a raw event log
# whose rows are the information of events recorded in the database and the second CSV file is the list of the
# name of cases selected through Goal-oriented Process Enhancement and Discovery (GoPED) or any other filtering scheme.
# This tool removes all event information of the cases that are not as selected, and generate a new event log.
######################################################################################################################


import csv
import os
import time
import argparse


#Parser:

myparser=argparse.ArgumentParser(description="This is a line of string that defines all inputs needed to run the code")
# Two main csv files as input:
myparser.add_argument("-Original", "--Original", help="The name of the the input original event log with .csv")
myparser.add_argument("-SelectedCases","--SelectedCases", help="The name of the input file of selected cases with .csv")


myargs=myparser.parse_args()

OriginalFile=myargs.Original
SelectedCasesFile=myargs.SelectedCases

start_time = time.time()#temp

#Reading two csv files:
Original=csv.reader(open(OriginalFile, "r"))
SelectedCases=csv.reader(open(SelectedCasesFile, "r"))

#Converting two csv files to list:
OriginalList=list(Original)
SelectedCasesList=list(SelectedCases)

#Converting the list of selected cases to a set
SelectedCasesSet=set()
for row in SelectedCasesList:
    SelectedCasesSet.add(row[0])


#Keeping the header or original log in a separate list
HeaderOfOriginalLog=OriginalList[0]

#Removing the header of Original log from the list
OriginalList=OriginalList[1:]

# Sorting the original log based on the case name
OriginalList.sort(key=lambda event: event[0])


NumberOfEvents=len(OriginalList)


#MAking the output csv:

RefinedEventLogFileName='NewEventLog'+time.strftime('@%Y-%m-%dT%H-%M-%S', time.localtime())+'.csv'
RefinedEventLogFile = csv.writer(open(RefinedEventLogFileName, 'a', newline=''))

#Adding the header of the original log to the new log as a header
RefinedEventLogFile.writerow(HeaderOfOriginalLog)


NumberOfSelectedCasesInOutput=0 # counting purpose
NumberOfEventsInOutput=0 #counting purpose


#Checking each row of original log and writing it in the new file if it is selected

flag=False #This flag shows that the most recent event (row of original log) was selected or not
if OriginalList[0][0] in SelectedCasesSet: #This IF is handling the first event of the original log before starting the main loop
    RefinedEventLogFile.writerow(OriginalList[0])
    flag=True
    NumberOfSelectedCasesInOutput+=1 # counting purpose
    NumberOfEventsInOutput += 1# counting purpose

index=1 # the index of events in the list of the original log
while index < NumberOfEvents:
    if OriginalList[index][0]==OriginalList[index-1][0]:  #if the Case of the current row is the same as of the previous row, the decision about this row is the same as the previous row
      if flag:
          RefinedEventLogFile.writerow(OriginalList[index])
          NumberOfEventsInOutput += 1
    else: #if the case name of the current row is not the same as of the previous row, then the Case name is checked against the Selected Cases
      if OriginalList[index][0] in SelectedCasesSet:
          RefinedEventLogFile.writerow(OriginalList[index])
          flag=True
          NumberOfSelectedCasesInOutput+=1
          NumberOfEventsInOutput += 1
      else:
          flag = False

    index+=1


#Execution time:
ExecutionTime=time.time() - start_time

print('The output file was successfully made as:',RefinedEventLogFileName,' in ',os.getcwd())
print()
print('Number of events in the original event log:', len(OriginalList))
print('Number of events in the output file:', NumberOfEventsInOutput)
print()
print("Number of selected cases' names in ",SelectedCasesFile,':',len(SelectedCasesSet))
print("Number of selected cases in output:", NumberOfSelectedCasesInOutput)
print()
if len(SelectedCasesSet)!=NumberOfSelectedCasesInOutput:
    print('WARNING! There might be some cases in',SelectedCasesFile ,'that do not exist in', OriginalFile,
          'and/or there are some redundancy in',SelectedCasesFile,'.')


print("\n\nExecution time: %s seconds" % round(ExecutionTime,5))

