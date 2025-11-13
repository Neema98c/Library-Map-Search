#this file will use the logic from search.py and add features that
#allow users to type commands to interact with the CSV files

def main():
    vars=""
    print("\n"+"From here you can enter either search parameters.")
    print("1. Subject")
    print("2. Classmark")
    print("3. Subject")
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
