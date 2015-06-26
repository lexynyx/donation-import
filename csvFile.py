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

"""make a function to increment the array """
def information (csvRecords):
   csvFile = open(filename, 'rb')
   # for ( var i = 1 ; i <= csvRecords.length?? ; i ++)
   # csvRecords[i]
F_Name = csvRecords[i].firstName
L_Name = csvRecords[i].lastname
address = csvRecords[i].address
city = csvRecords[i].city
province = csvRecords[i].province
postalC = csvRecords[i].postalCode
amountPaid = csvRecords[i].amountPaid 
datePaid = csvRecords[i].datePaid

 
insertQuery = 'insert into individual vaues ({F_name , L_name , address , city , province , postalC , amountPaid , datePaid})'
cursor = connection.cursor()
cursor.execute(insertQuery, csvFile)

dic = [(i['col1'], i['col2']) for i in openCsvFile()]
 
