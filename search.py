#This is the file for the backend logic of the program
#It will contain the readers for the CSV files, and will run the search functionality based on the inputs
#from the front end part of the code

#rough breakdown of what I need:

#GUI or CLI will run first, and prompt the user for two inputs: type of search, and then the search term.
#this file will take those search terms, and the search type, 
#open the CSV corresponding to the search type
#search for the item searched for
#if present, use the classmark associated with the search term, and return corresponding information from BOTH CSV files

#eg: 

# What search do you want?

# >>subject
# What subject?
# >>physics
# Subject: ?subject
# Classmark: ?class_mark
# Location: ?library_loc

import csv

i = True

def getCSVData():
    with open("subject.csv", newline="") as csvfile:
        subjectReader = csv.reader(csvfile,delimiter=" ", quotechar="|")

def searchForSubject(searchTerm):
        
    with open("subject.csv", newline="") as csvSubject:
        subjectReader = csv.DictReader(csvSubject)
        subjectRow = None
        for row in subjectReader:
            if row["Subject"].lower() == searchTerm.lower():
                subjectRow = row
                break
            
    if subjectRow is None:
        return None
            
    classmark = subjectRow["Classmark"]
    
    with open("location.csv", newline="") as csvloc:
        locationReader = csv.DictReader(csvloc)
        for row in locationReader:
            if row["Classmark"] == classmark:
                return subjectRow["Subject"], classmark, row["Location"]
        return "error"

def searchForClassmark(searchTerm):
    if (i == True):
        return "subject", searchTerm, "location"
    else:
        return "error", searchTerm

def searchForLocation(searchTerm):
    if (i == True):
        return "subject", "classmark", searchTerm
    else:
        return "error", searchTerm
    
def searchTypeCheck(searchType):
    match(searchType):
        case "subject" | "1":
            searchTerm = input("Enter a subject to search for: ")
            return searchForSubject(searchTerm)
        case "classmark" | "2":
            searchTerm = input("Enter a classmark to search for: ")
            return searchForClassmark(searchTerm)
        case "location" | "3":
            searchTerm = input("Enter a location to search for: ")
            return searchForLocation(searchTerm)
        case "exit" | "4":
            exit()
        case _:#if none of these options, make the user do it again.
            return "error", searchType
            

def main():
    vars=""
    print("\n"+"From here you can enter either search parameters.")
    print("1. Subject")
    print("2. Classmark")
    print("3. Location")
    print("4. Exit")
    searchTest2 = input("Enter a search term: ")   

    vars = searchTypeCheck(searchTest2)
    error_message1 = "There was an error with your input"
    error_message2 = ""

    if(vars[0]=="error"):
        error_message2 = "The input '"+vars[1]+"' confounded the machine"
        print(error_message1)
        print(error_message2)
        main()
    else:
        print("\nSubject is: "+vars[0])
        print("Classmark is: "+vars[1])
        print("Location is: "+vars[2])
        print("\nWould you like to search for more?")
        againCheck = input("Please type Yes or No: ").lower()
        if (againCheck=="yes" or againCheck=="1" or againCheck=="y"):
            main()
        else:
            exit()
        
main()


