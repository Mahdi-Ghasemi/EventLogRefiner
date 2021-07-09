# EventLogRefiner
This tool gets two CSV files as input and generates a new CSV file as output. One CSV file is a raw event log whose rows are the information of events recorded in the database and the second CSV file is the list of the name of cases selected through Goal-oriented Process Enhancement and Discovery (GoPED) or any other filtering scheme. This tool removes all event information of the cases that are not as selected, and generate a new event log. Such a new event log file will be in a format ready to be fed to process mining tools (such as ProM).

## **Inputs:**
1. _CSV file of Original Event Log_:

The format of this input file is like the event logs that are typically used in process mining projects. The format of the output will be the same as this input file. The rows related to the absent cases in the CSV file of Selected Cases won't be present in the output file.

The original CSV file MUST

- have a **header** containing column names. (The tool assumes the first row of this file as a header and will use that as a header for the output file as well.)
- use the **first** column as a Case identifier (case name, ID,…).

2. _CSV file of selected cases_:

This CSV file is the output of GoPED containing the name of all selected cases.

This CSV file MUST:

- have only one column (the first column of the CSV).
- not have any header.
- have the Case identifier (Name, ID,…) of a case in each row.

## **Output:**
The output is a CSV file in the same format as the original CSV file.

The name of the output file will be as _NewEventLog@{date and time}.csv_. This file will be made in the same folder as the tool.


## **How to run the tool:**
The tool works via command-line arguments in CMD where Python 3 is running. The format of the string must be as follows:

…> python EventLogRefiner.py -Original {the name of CSV file with .csv} -SelectedCases { the name of CSV file with .csv }

- It is strongly suggested not to use any special character in the CSV files name, such as space.
- If there is any space character in the names of CSV files, the name must be between double quotations (").

Examples:   
> _...> python EventLogRefiner.py -Original myevent.csv -SelectedCases myselection.csv_

> The csv arguments can also be mentioned as abbreviated or shorter names:  
> _...> python EventLogRefiner.py -O myevent.csv -S myselection.csv_   
> _..> python EventLogRefiner.py -Orig myevent.csv -Sel myselection.csv_

> The CSV arguments position in the command line is flexible:  
> _...> python EventLogRefiner.py -S myselection.csv -O myevent.csv_
