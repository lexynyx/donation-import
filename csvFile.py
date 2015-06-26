# CSV file related functions

import csv

# CONSTANTS
""" Constants for CSV file """
__CSV_FIRST_NAME__ = 4
__CSV_LAST_NAME__ = 5
__CSV_ADDRESS__ = 7
__CSV_CITY__ = 9
__CSV_PROVINCE__ = 10
__CSV_POSTAL_CODE__ = 11
__CSV_AMOUNT_PAID__ = 17
__CSV_DATE_PAID__ = 18
__CSV_DELIMETER__ = ','

class CSVRecord:
   """ Class for a CSV row in the record """
   def __init__(self,infoRow):
      self.firstName = infoRow[__CSV_FIRST_NAME__]
      self.lastName = infoRow[__CSV_LAST_NAME__]
      self.address = infoRow[__CSV_ADDRESS__]
      self.city = infoRow[__CSV_CITY__]
      self.province = infoRow[__CSV_PROVINCE__]
      self.postalCode = infoRow[__CSV_POSTAL_CODE__]
      self.amountPaid = infoRow[__CSV_AMOUNT_PAID__]
      self.datePaid = infoRow[__CSV_DATE_PAID__]

def openCsvFile(filename):
   """ Return the CSV file as an iterator object """
   csvFile = open(filename, 'rb')
   csvOutput = csv.reader(csvFile, delimiter=__CSV_DELIMETER__)
   return csvOutput

def getRecords(csvObject:)
   """ Return the list of records found inside the CSV file """
   csvRecords = []
   for row in csvObject:
      csvRecords.append(CSVRecord(row))
   del csvRecords[0] #Delete the first row containing the row labels
   return csvRecords
   
# sample program
csvObject = openCsvFile("CharityDataDownload.csv")
csvRecords = getRecords(csvObject)
print csvRecords[1].firstName

"""looping through rows, so that we can read the information, making it an array"""
info = open ('charitydatadownload.csv')
csv_info = csv.reader(info)

for row in csv_info
print row """print row[#]"""

"""create a list of certain attribute of the database SAMPLE"""
csv_CSV_FIRST_NAME = []

for row in csv_info
csv_CSV_FIRST_NAME.append(row[1])
print csv_CSV_FIRST_NAME """this will print a single list of all the donator's name"""

"""
1. read the csv file
2. make every row into an array
3. make a loop so that 
   3.1 it reads the array row 
   3.2 another loop to read all the attribute in the array
   3.3 input the correct array into the correct database column
"""

