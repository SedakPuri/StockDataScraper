# StockDataScraper
A python program that scrapes off stock data stored in HTML tables from Yahoo Finance (https://finance.yahoo.com/) and makes a folder on your desktop that contains seperate xls (Excel files) of the:

1. Historical Stock Data 
2. Balance Sheet
3. Income Statement
4. Statement of Cash Flows

Note:

**-Program still contains some bugs but works for the most part**

**-Program creates file on desktop relative to my computer path to desktop (/Users/sedakpuri/Desktop/). This is only temporary and will be fixed in later adaptations but you can fix this by altering the value of the directoryPath variable**

Dependencies:
**BeautifulSoup**, **Resources**

Update 2.0:
Project also includes an Apple Automator program that runs a shell script and creates a clean user interface to prompt the user to input in a stock ticker and fetches data (more improvements to come :P). 
