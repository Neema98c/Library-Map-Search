from tkinter import *
from tkinter import ttk
from search import searchTypeCheck

root = Tk()

def doSearch():

    searchType = searchTypeVar.get()
    searchTerm = searchBar.get()
    
    results = searchTypeCheck(searchType, searchTerm)
    
    if not results:
        resultsLabel.config(text="No results found.")
        return

    # Build a text block
    output = ""
    for subject, classmark, location in results:
        output += f"Subject: {subject.upper()}\nClassmark: {classmark.upper()}\nLocation: {location.upper()}\n\n"

    resultsLabel.config(text=output)
    

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
searchTitle = ttk.Label(content, text="Search Bar")
searchBar = ttk.Entry(content)

searchTypeVar = StringVar(value="1")

subject = ttk.Radiobutton(content, text="Subject", variable=searchTypeVar, value="1")
classmark = ttk.Radiobutton(content, text="Classmark", variable=searchTypeVar, value="2")
location = ttk.Radiobutton(content, text="Location", variable=searchTypeVar, value="3")
    
search = ttk.Button(content, text="Search", command=doSearch)
exit = ttk.Button(content, text="Exit", command=exit)

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
resultsLabel = ttk.Label(frame, text="", justify="left")
resultsLabel.grid(row=0, column=0, sticky="nw")
searchTitle.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
searchBar.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
subject.grid(column=0, row=5)
classmark.grid(column=1, row=5)
location.grid(column=2, row=5)
search.grid(column=3, row=5)
exit.grid(column=4, row=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

        
root.mainloop()
