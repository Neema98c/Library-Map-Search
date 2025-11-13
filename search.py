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

i = True

def getCSVData():
    return "error", "no csv"

def searchForSubject(searchTerm):
    if (i == True):
        return searchTerm, "classmark", "location"
    else:
        return "error", searchTerm

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
            



