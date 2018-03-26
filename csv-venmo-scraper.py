# csv-venmo-scraper.py

import csv
from collections import namedtuple

if __name__ == "__main__":
    ############################### BUILD ROSTER LIST ###############################
    # read in ski team roster: use namedtuple so can access data like class members
    # First param  - name of "Class"
    # Second param - all fields (keys) that will be supported, space separated
    Member = namedtuple("Member", "Name Phone")
    
    #array to store tuples
    members = []

    #scrape roster file and store in tuple array
    with open("skiTeamRoster_2017-18.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        fNameCell = 0
        phoneCell = 0
        for i, row in enumerate(readCSV):
            # grab column values for first name and phone number
            if (i is 0):
                for j, col in enumerate(row):
                    if ("first" in row[j].lower()): 
                        fNameCell = j
                    if ("phone" in row[j].lower()):
                        phoneCell = j

            # grab name and phone values --> store in Member tuple and append to members array        
            name = row[fNameCell] +  " " + row[fNameCell + 1]
            phone = row[phoneCell]
            member = Member(name, phone)
            members.append(member)
  
    # print(members)

    ############################### BUILD TRANSACTION LIST ###############################
    # read in venmo transaction history: use namedtuple so can access data like class members
    # First param  - name of "Class"
    # Second param - all fields (keys) that will be supported, space separated
    vTransaction = namedtuple("vTransaction", "Datetime Type Status Note From To Amount")
    venmo_transactions = []

    with open("venmoTransactions_2017-18.csv", encoding = "utf-8", errors = 'replace') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(readCSV):
            if i is not 0:
                transaction = vTransaction(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                venmo_transactions.append(transaction)

    # print()
    # print(venmo_transactions)

    