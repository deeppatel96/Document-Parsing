# Author: Deep Patel

import csv
import re

def extract_files(files, printToConsole=False):
    result = [['PATH', 'TYPE', 'AMOUNT', 'OTHER']]
    for i in range(0, len(files)):
        result.append(analyze_file(files[i]))

    # Make CSV file using Python list
    with open('results.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)

    # Print to Console if option is set to True
    if printToConsole:
        for i in range(0, len(result)):
            print result[i]

    return


'''

'''

def analyze_file(file):

    PATH = file
    TYPE = ''
    AMOUNT = ''
    OTHER = ''

    # Load all lines of text file into a list variable
    lines = open(file).readlines()

    # Check all lines in file for word "receipt"
    if any("receipt" in substring.lower() for substring in lines):
        TYPE = 'RECEIPT'
    else:
        TYPE = 'BANK'

# For Receipt
    if TYPE == 'RECEIPT':
        # Get total sale amount
        totalLine =  -1
        for index, value in enumerate(lines):
            if "total" in value.lower():
                totalLine = index

        newstr = ''.join((ch if ch in '0123456789,.-' else ' ') for ch in lines[totalLine])
        newstr = newstr.replace(',','')
        totalAmount = [float(i) for i in newstr.split()][-1]
        AMOUNT = str(totalAmount)

        # Get change amount
        changeLine =  -1
        for index, value in enumerate(lines):
            if "change" in  value.lower():
                changeLine = index

        if changeLine == -1:
            OTHER = '0'
        else:
            newstr = ''.join((ch if ch in '0123456789,.-' else ' ') for ch in lines[changeLine])
            newstr = newstr.replace(',','')
            changeAmount = [float(i) for i in newstr.split()][-1]
            if changeAmount == 0:
                OTHER = '0'
            else:
                OTHER = str(changeAmount)

    # For Bank Statement
    else:
         # Get ending bank balance
         balanceLine =  -1
         for index, value in enumerate(lines):
             if "balance" in value.lower() and "previous" not in value.lower() and "opening" not in value.lower():
                 balanceLine = index

         newstr = ''.join((ch if ch in '0123456789,.-' else ' ') for ch in lines[balanceLine])
         newstr = newstr.replace(',','')
         balanceAmount = [float(i) for i in newstr.split()][-1]
         AMOUNT = str(balanceAmount)

         # Get phone number
         for line in lines:
             for match in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", line):
                 if '1-' in line:
                     OTHER = "1-" + match.group()
                 else:
                     OTHER = match.group()

    # Return list of extracted values
    return [PATH, TYPE, AMOUNT, OTHER]


if __name__ == "__main__":

    # Initiate list of document paths
    pathes = ['documents/1.txt', 'documents/2.txt', 'documents/3.txt', 'documents/4.txt', 'documents/5.txt',
            'documents/6.txt', 'documents/7.txt', 'documents/8.txt', 'documents/9.txt']

    # Call function to create csv file and set print to console option to True
    extract_files(pathes, printToConsole=True)
