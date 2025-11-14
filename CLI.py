#this file will use the logic from search.py and add features that
#allow users to type commands to interact with the CSV files
from search import searchTypeCheck

def main():
    results=[]
    print("\n"+"From here you can enter either search parameters.")
    print("1. Subject")
    print("2. Classmark")
    print("3. Location")
    print("4. Exit")
    
    searchType = input("Choose a search area: ").lower()
    
    if (searchType == "4" or searchType == "exit"):
        exit()
    
    if (searchType == "3" or searchType == "location"):
        print("----- MAP -----")
        print("Top Floor")
        print("\n---------------")
        print("| TFTL | TFTR |")
        print("---------------")
        print("| TFBL | TFBR |")
        print("---------------")
        print("Middle Floor")
        print("\n---------------")
        print("| ____ | MFTR |")
        print("---------------")
        print("| ____ | ____ |")
        print("---------------")
        print("Ground Floor")
        print("\n---------------")
        print("| ____ | ____ |")
        print("---------------")
        print("| ____ | LAW  |")
        print("---------------")
        print("\n Use these location codes when searching.")
    
    searchTerm = input("Enter your search: ")   

    results = searchTypeCheck(searchType, searchTerm)

    if (results == []):
        print("Search term '"+searchTerm + "' not found with search type: '" + searchType+"'")
        print("The result may not exist or spelling may be incorrect")
        main()
        
    print("\nResults:")
    for subject, classmark, location in results:
        print(" Subject: " + subject.upper() + "  Classmark: "+classmark+"  location: "+location.upper())
    
    print("\nWould you like to search for anything else?")
    againCheck = input("Please type Yes or No: ").lower()
    if (againCheck=="yes" or againCheck=="1" or againCheck=="y"):
        main()
    else:
        exit()
main()