import csv
import os
import requests
from BeautifulSoup import BeautifulSoup

#User input
while(True):
    symb = raw_input("\nEnter a stock symbol!\n")
    type(symb)
    if(len(symb) < 5 and len(symb) != 0):
        break;
print "\nThanks user, generating your report...\n"

#Making a directory to store Excel files
directoryPath = "/Users/sedakpuri/Desktop/" + symb.upper() + "_StockData"
try:
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)
except OSError:
    print ('Error Creating directory! Was this report generated twice from this directory: ' +  directoryPath)
    sys.exit(0)

#Defining the url's to pull from
urlH = 'https://finance.yahoo.com/quote/' + symb + '/history?period1=345452400&period2=1534572000&interval=1d&filter=history&frequency=1d'
urlI = 'https://finance.yahoo.com/quote/' + symb + '/financials?p=F'
urlB = 'https://finance.yahoo.com/quote/'+ symb +'/balance-sheet?p=F'
urlC = 'https://finance.yahoo.com/quote/'+ symb +'/cash-flow?p=F'




#Pulling from Historical Prices Table
response = requests.get(urlH)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('tbody')

listRows = []
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Cells
        listCells.append(cell.text)                              
    listRows.append(listCells)

#Setup/Outputting Historical Prices Table to a csv format!
path = directoryPath + "/" + symb.upper() + "_HistoricalData.csv"
outfile = open(path,"wb")
writer = csv.writer(outfile)

writer.writerow(["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
writer.writerows(listRows)






#Pulling from Financials Table (Income Statement)
response = requests.get(urlI)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('tbody')

listRows = []
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Cells
        listCells.append(cell.text)
    listRows.append(listCells)

#Setup/Outputting Historical Prices Table to a csv format!
path = directoryPath + "/" + symb.upper() + "_IncomeStatement.csv"
outfile = open(path,"wb")
writer = csv.writer(outfile)
writer.writerows(listRows)






#Pulling from Financials Table (Balance Sheet)
response = requests.get(urlB)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('tbody')

listRows = []
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Cells
        listCells.append(cell.text)
    listRows.append(listCells)

#Setup/Outputting Historical Prices Table to a csv format!
path = directoryPath + "/" + symb.upper() + "_BalanceSheet.csv"
outfile = open(path,"wb")
writer = csv.writer(outfile)
writer.writerows(listRows)





#Pulling from Financials Table (Cash Flows)
response = requests.get(urlC)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('tbody')

listRows = []
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Cells
        listCells.append(cell.text)
    listRows.append(listCells)

#Setup/Outputting Historical Prices Table to a csv format!
path = directoryPath + "/" + symb.upper() + "_CashFlows.csv"
outfile = open(path,"wb")
writer = csv.writer(outfile)
writer.writerows(listRows)

print "Sucess! Look on your desktop!\n"

#Asking the user if they want to see the additional immediate statistics
while(True):
    input = raw_input("Would you like to see the immediate stats? (y or n)\n")
    type(input)
    if (input == "y" or input == "Y" or input == "n" or input == "N"):
        break;

if(input == "y" or input == "Y"):
    urlS = 'https://finance.yahoo.com/quote/'+ symb
        
    response = requests.get(urlS)
    html = response.content
    soup = BeautifulSoup(html)
    table = soup.find('tbody')
        
    print("Stats\n")
    for row in table.findAll('tr'):                                 #List of rows
        for cell in row.findAll('td'):                              #Individual Cells
            print (cell.text)
        print ("\n")
