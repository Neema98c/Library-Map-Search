# This is the file for the backend logic of the program
# It will contain the readers for the CSV files, and will run the search functionality based on the inputs
# from the front end part of the code

# rough breakdown of what I need:

# GUI or CLI will run first, and prompt the user for two inputs: type of search, and then the search term.
# this file will take those search terms, and the search type, 
# open the CSV corresponding to the search type
# search for the item searched for
# if present, use the classmark associated with the search term, and return corresponding information from BOTH CSV files

#eg: 

# What search do you want?

# >>subject
# What subject?
# >>physics
# Subject: ?subject
# Classmark: ?class_mark
# Location: ?library_loc

import csv
    
def searchTypeCheck(searchType, searchTerm):
    match(searchType):
        
        # For subject open the subject csv, find the classmarks and then find the locations from 
        # the classmarks.
        # A subject can contain more than one classmark but only one location.
        
        case "subject" | "1":
            results = []
            with open("subject.csv", newline="") as csvSubject:
                subjectReader = csv.DictReader(csvSubject)
                classmarks = [row["Classmark"] for row in subjectReader 
                              if row["Subject"].lower() == searchTerm.lower()]
            
            if (classmarks == []):
                return []
    
            with open("location.csv", newline="") as csvloc:
                locationReader = csv.DictReader(csvloc)
                locations = list(locationReader)
            for classmark in classmarks:
                for row in locations:
                    if row["Classmark"] == classmark:
                        results.append((searchTerm, classmark, row["Location"]))
            return results
        
        # For class mark, open both CSV files and find the corresponding subjects and locations
        # A classmark can belong to more than one subject, but only one location.
        
        case "classmark" | "2":
            results = []
            with open("subject.csv", newline="") as csvClassmark:
                classmarkReader = csv.DictReader(csvClassmark)
                subjects = [row["Subject"] for row in classmarkReader
                            if row["Classmark"] == searchTerm]
            
            if (subjects == []):
                return []
    
            with open("location.csv", newline="") as csvloc:
                locationReader = csv.DictReader(csvloc)
                location = None
                for row in locationReader:
                    if row["Classmark"] == searchTerm:
                        location = row["Location"]
                        break
            for subject in subjects:
                results.append((subject, searchTerm, location))
            return results
        
        # For location, check location csv file to find classmark, then check the classmark against
        # the subject.
        # A location can contain many classmarks and many subjects
        
        case "location" | "3":
            results = []
            with open("location.csv", newline="") as csvloc:
                locationReader = csv.DictReader(csvloc)
                classmarks = [row["Classmark"] for row in locationReader
                              if row["Location"].lower() == searchTerm.lower()]
            if (classmarks == []):
                return []
            
            with open("subject.csv", newline="") as csvSubject:
                subjectReader = csv.DictReader(csvSubject)
                subjects = list(subjectReader)
            
            for classmark in classmarks:
                for row in subjects:
                    if row["Classmark"] == classmark:
                        results.append((row["Subject"], classmark, searchTerm))
            
            return results
        case _:
            return []