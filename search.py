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

# #What search do you want?
# >>subject
# What subject?
# >>physics
# Subject: ?subject
# Classmark: ?class_mark
# Location: ?library_loc

def getCSVData():
    return

def searchTypeCheck(searchTerm, searchType):
    match(searchType):
        case "subject" | 1:
            searchForSubject(searchTerm)
        case "classmark" | 2:
            searchForClassmark(searchTerm)
        case "location" | 3:
            searchForLocation(searchTerm)
        case "exit" | 4:
            return 0

def searchForSubject(searchTerm):
    return

def searchForClassmark(searchTerm):
    return

def searchForLocation(searchTerm):
    return

