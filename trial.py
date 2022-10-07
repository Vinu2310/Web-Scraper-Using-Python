import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html")
bsObj = BeautifulSoup(html,"lxml")
table = bsObj.findAll("table", {"class":"tbldata14 bdrtpg"})[0]
rows = table.findAll("tr")
csvFile = open("editors.csv","wt",newline='')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()