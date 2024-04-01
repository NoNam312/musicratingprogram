from tkinter import *
from subprocess import  call
import csv
from tkinter import messagebox
import os
import webbrowser


window = Tk()
window.geometry("1380x720")
window['background'] = '#D7D6FD'

with open("albumIMGDirectory.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=',')


productionEntry = None
vocalsEntry = None
instrumentalsEntry = None
enjoymentEntry = None
totalEntry = None


# Save the data to a CSV file
def save_ratings_to_csv(album, productionRating, vocalsRating, instrumentalRating, enjoymentRating, averageValue):
    csv_data = [album, productionRating, vocalsRating, instrumentalRating, enjoymentRating, averageValue]

    file_path = 'userList.csv'

    # Check if the file exists, and if not, create a new CSV file with headers
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Album', 'Production', 'Vocals', 'Instrumentals', 'Enjoyment', 'Total'])

    # Append the new rating data to the CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_data)

def load_user_data():
    user_data = []
    with open('userList.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data.append(row)
    return user_data


def submit_rating(album):
    #Declaring Variables
    global productionEntry, vocalsEntry, instrumentalsEntry, enjoymentEntry, totalEntry
    global productionRating, vocalsRating, instrumentalRating, enjoymentRating

    #Setting Ratings Values
    productionRating = None
    vocalsRating = None
    instrumentalRating = None
    enjoymentRating = None


    try:
        productionValue = int(productionEntry.get())
        if 0 <= productionValue <= 10:
            productionRating = productionValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Production.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")
    
    try:
        vocalsValue = int(vocalsEntry.get())
        if 0 <= vocalsValue <= 10:
            vocalsRating = vocalsValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Vocals.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    try:
        instrumentalValue = int(instrumentalsEntry.get())
        if 0 <= instrumentalValue <= 10:
            instrumentalRating = instrumentalValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10. in Instrumentals")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    try:
        enjoymentValue = int(enjoymentEntry.get())
        if 0 <= enjoymentValue <= 10:
            enjoymentRating = enjoymentValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Enjoyment.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    averageValue = (productionRating + vocalsRating + instrumentalRating + enjoymentRating)/4
    totalEntry.delete(0, END)
    totalEntry.insert(0, round(averageValue, 1))


    # Save the data to a CSV file
    csv_data = [album, productionRating, vocalsRating, instrumentalRating, enjoymentRating, round(averageValue, 1)]

    file_path = 'userList.csv'

    # Check if the file exists, and if not, create a new CSV file with headers
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Album', 'Production', 'Vocals', 'Instrumentals', 'Enjoyment', 'Total'])
    
    # Load the existing user data from CSV
    user_data = load_user_data()

    # Update the rating if the album already exists in the user_data
    updated = False
    for album_data in user_data:
        if album_data['Album'] == album:
            album_data['Production'] = productionRating
            album_data['Vocals'] = vocalsRating
            album_data['Instrumentals'] = instrumentalRating
            album_data['Enjoyment'] = enjoymentRating
            album_data['Total'] = round(averageValue, 1)
            updated = True
            break
    
    # If the album doesn't exist in the user_data, add it as a new entry
    if not updated:
        user_data.append({'Album': album, 'Production': productionRating, 'Vocals': vocalsRating,
                          'Instrumentals': instrumentalRating, 'Enjoyment': enjoymentRating,
                          'Total': round(averageValue, 1)})
    
    # Save the updated user_data back to the CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Album', 'Production', 'Vocals', 'Instrumentals', 'Enjoyment', 'Total'])
        writer.writeheader()
        writer.writerows(user_data)
    

def homePage():
    global window
    window.destroy()
    call(["python", "home.py"])

def listPage():
    global window
    window.destroy()
    call(["python", "list.py"])


def SearchAlbum(albumname):
    with open("albumIMGDirectory.csv", 'r') as file:
        csvreader = csv.DictReader(file, delimiter=',')

        for line in file:
            file_line = line.split(',')
            if albumname == (file_line[0]):
                return str(file_line[1])


def ArtistbyAlbum(albumname):
    with open("albumIMGDirectory.csv", 'r') as file:
        csvreader = csv.DictReader(file, delimiter=',')

        for line in file:
            file_line = line.split(',')
            if albumname == (file_line[0]):
                return str(file_line[2])
            
def LabelbyAlbum(albumname):
    with open("albumIMGDirectory.csv", 'r') as file:
        csvreader = csv.DictReader(file, delimiter=',')

        for line in file:
            file_line = line.split(',')
            if albumname == (file_line[0]):
                return str(file_line[4])

def GenrebyAlbum(albumname):
    with open("albumIMGDirectory.csv", 'r') as file:
        csvreader = csv.DictReader(file, delimiter=',')

        for line in file:
            file_line = line.split(',')
            if albumname == (file_line[0]):
                return str(file_line[3])


def ratingWindow(albumname):
    global productionEntry, vocalsEntry, instrumentalsEntry, enjoymentEntry, totalEntry

    newWindow = Toplevel(window)
    newWindow.geometry("1280x720")
    newWindow.title("New Window")
    #Create a Label in New window

    newWindow['background'] = '#D7D6FD'

    topFrame = Frame(window, bg="#6461BB")
    topFrame.pack(side=TOP, fill=X)
    albumText = Label(newWindow, text=f"{albumname}", font=("Segoe UI", 30), fg="white", bg="#6461BB")
    albumText.pack(padx=20, pady=20, side=TOP, fill=X)

    albumIMG = PhotoImage(file=SearchAlbum(albumname))
    zoomIMG = albumIMG.zoom(2, 2)

    albumDisplay = Label(newWindow, image=zoomIMG, height=400, width=400, bd=0)
    albumDisplay.photo = zoomIMG
    albumDisplay.pack(side=LEFT, padx=20, pady=20, anchor="nw")

    #Entry and Labels for Rating
    ratingFrame = Frame(newWindow, bg="#6461BB")
    ratingFrame.pack(side=RIGHT, anchor="ne", padx=5, pady=20)


    #Production Labels and Entry
    productionLabel = Label(ratingFrame, text="Production", font=("Segoe UI", 15), bg="#6461BB", fg="white")
    productionLabel.grid(column=0, row=0, padx=300, pady=22)

    productionEntry = Entry(ratingFrame, width=5, bd="2", font=("Segoe UI", 15), bg="#F2F2F2")
    productionEntry.grid(column=1, row=0, padx=20, pady=22)

    #Vocals Labels and Entry
    vocalsLabel = Label(ratingFrame, text="Vocals", font=("Segoe UI", 15), bg="#6461BB", fg="white")
    vocalsLabel.grid(column=0, row=1, padx=300, pady=22)

    vocalsEntry = Entry(ratingFrame, width=5, bd="2", font=("Segoe UI", 15), bg="#F2F2F2")
    vocalsEntry.grid(column=1, row=1, padx=20, pady=22)

    #Instrumental Labels and Entry
    instrumentalsLabel = Label(ratingFrame, text="Instrumental", font=("Segoe UI", 15), bg="#6461BB", fg="white")
    instrumentalsLabel.grid(column=0, row=2, padx=300, pady=22)

    instrumentalsEntry = Entry(ratingFrame, width=5, bd="2", font=("Segoe UI", 15), bg="#F2F2F2")
    instrumentalsEntry.grid(column=1, row=2, padx=20, pady=22)

    #Enjoyment Labels and Entry
    enjoymentLabel = Label(ratingFrame, text="Enjoyment", font=("Segoe UI", 15), bg="#6461BB", fg="white")
    enjoymentLabel.grid(column=0, row=3, padx=300, pady=22)

    enjoymentEntry = Entry(ratingFrame, width=5, bd="2", font=("Segoe UI", 15), bg="#F2F2F2")
    enjoymentEntry.grid(column=1, row=3, padx=20, pady=22)

    #Total Labels and Entry
    totalLabel = Label(ratingFrame, text="Total", font=("Segoe UI", 15), bg="#6461BB", fg="white")
    totalLabel.grid(column=0, row=4, padx=300, pady=22)

    totalEntry = Entry(ratingFrame, width=5, bd="2", font=("Segoe UI", 15), bg="#F2F2F2")
    totalEntry.grid(column=1, row=4, padx=20, pady=22)


    submit_button = Button(ratingFrame, text="Submit Rating", command=lambda: submit_rating(albumname))
    submit_button.grid(column=1, row=5, pady=10, padx=10)




#Header
headFrame = Frame(window, width=1000, bg='#D7D6FD')
headFrame.pack(anchor="w")

logoImage = PhotoImage(file="RTLogo.png")
imgButton= Button(headFrame, height= 50, width=50, image=logoImage, bg="#D7D6FD", bd="0", command=homePage)
imgButton.pack(padx=10, pady=10, anchor="w", side=LEFT)

searchIMG = PhotoImage(file="searchButton.png")

#Navigation Frame for the Nav Bar
navFrame = Frame(window, bg= "#6461BB")
navFrame.pack(side=TOP, fill=X)

# Create the buttons in the navigation bar
#Home Page Button
homepageButton = Button(navFrame, text="Home", command=homePage, bg= "#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
homepageButton.pack(side=LEFT, padx=30, pady=20)

#List Page Button
listpageButton= Button(navFrame, text="List", command=listPage, bg= "#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
listpageButton.pack(side=LEFT, padx=30, pady=20)

##Recommendation Page Button
recpageButton = Button(navFrame, text="Rec", command="", bg= "#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
recpageButton.pack(side=LEFT, padx=30, pady=20)


searchButton = Button(navFrame, height= 50, width=50, image=searchIMG, bg="#6461BB", bd="0", command=homePage)
searchButton.pack(side=RIGHT, padx=30, pady=20)

all_items = []

with open("albumIMGDirectory.csv", 'r') as file:
    csvreader = csv.DictReader(file, delimiter=',')

    for line in file:
        file_line = line.split(',')
        all_items.append(str(file_line[0]))


all_items.remove("ï»¿Album Name")

def on_search_changed(event):
    search_query = search_var.get().lower()
    canvas.delete("buttons")  # Clear the current canvas contents

    row = 0
    for item in all_items:
        if search_query in item.lower():
            listFrame = Frame(canvas, bg="#6461BB")

            albumIMG = PhotoImage(file=SearchAlbum(item))
            zoomIMG = albumIMG.subsample(3, 3)

            albumDisplay = Label(listFrame, text=item, relief=FLAT, image=zoomIMG, bg="#6461BB")
            albumDisplay.grid(column=0, row=0, padx=20, pady=10)
            albumDisplay.photo = zoomIMG

            albumButton = Button(listFrame, text=item, relief=FLAT, command=lambda t=item: ratingWindow(t), font=("Helvetica", 16), height=2, width=15 ,bg='#8885DD', fg="white")
            albumButton.grid(column=1, row=0, padx=20, pady=10)

            artistDisplay = Label(listFrame, text=ArtistbyAlbum(item), font=("Helvetica", 16), height=2, width=15 ,bg='#8885DD', fg="white", relief=FLAT)
            artistDisplay.grid(column=2, row=0, padx=20, pady=10,)

            genreDisplay = Label(listFrame, text=GenrebyAlbum(item), font=("Helvetica", 16), height=2, width=15 ,bg='#8885DD', fg="white", relief=FLAT)
            genreDisplay.grid(column=3, row=0, padx=20, pady=10,)

            LabelDisplay = Label(listFrame, text=LabelbyAlbum(item), font=("Helvetica", 16), height=2, width=25 ,bg='#8885DD', fg="white", relief=FLAT)
            LabelDisplay.grid(column=4, row=0, padx=20, pady=10,)

            canvas.create_window(10, row, anchor=W, window=listFrame, tags="buttons")
            row += 80  # Increase the row height to create more space between buttons

    # Update the canvas scroll region to include all buttons
    canvas.config(scrollregion=canvas.bbox("all"))


# Create the search bar
search_var = StringVar()
search_entry = Entry(window, textvariable=search_var, font=("Helvetica", 16))
search_entry.pack(pady=10)

# Bind the search function to the Entry widget
search_entry.bind("<KeyRelease>", on_search_changed)

canvas_frame = Frame(window, bg="#D7D6FD")  # Place canvas_frame inside navFrame
canvas_frame.pack(fill=BOTH, expand=True)

# Create the Canvas to hold the button-like widgets
canvas = Canvas(canvas_frame, width=1310, height=400, bg='#AAA8F1')  # Adjust the canvas size to your preference
canvas.pack(side=LEFT, padx=20, pady=20)

# Create the Scrollbar
scrollbar = Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)  # Use pack to place the scrollbar on the right side

# Configure the canvas to control the scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Insert the button-like widgets into the Canvas
on_search_changed(None)
canvas.update_idletasks()  # Update the canvas with the correct button positions

# Update the canvas scroll region to include all buttons
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()
