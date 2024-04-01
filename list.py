from tkinter import *
from subprocess import  call
import os
import csv
import tkinter.messagebox as messagebox

def load_album_data():
    albums = []
    with open('albumIMGDirectory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            albums.append(row)
    return albums

def load_user_data():
    user_data = []
    with open('userList.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data.append(row)
    return user_data

def merge_data(albums, user_data):
    merged_data = []
    for album_info in albums:
        album_name = album_info['ï»¿Album Name']
        for user_album in user_data:
            if user_album['Album'] == album_name:
                album_info.update(user_album)
                merged_data.append(album_info)
                break
    return merged_data

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

def searchPage():
    global window
    window.destroy()
    call(["python", "search.py"])


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
                return str(file_line[2])[:-1]


#Widnow for rating music
def ratingWindow(albumname):
    #Declaring Global Variables
    global productionEntry, vocalsEntry, instrumentalsEntry, enjoymentEntry, totalEntry

    newWindow = Toplevel(window)
    newWindow.geometry("1280x720")
    newWindow.title("New Window")
    #Create a Label in New window

    newWindow['background'] = '#D7D6FD'


    #Frame for Music Name
    topFrame = Frame(window, bg="#6461BB")
    topFrame.pack(side=TOP, fill=X)
    albumText = Label(newWindow, text=f"{albumname}", font=("Segoe UI", 30), fg="white", bg="#6461BB")
    albumText.pack(padx=20, pady=20, side=TOP, fill=X)


    #Album Image Path and Zoom
    albumIMG = PhotoImage(file=SearchAlbum(albumname))
    zoomIMG = albumIMG.zoom(2, 2)

    #Displaying Album IMG
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




#Loads the Album Directory/Music Database
def load_album_data():
    albums = []
    with open('albumIMGDirectory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            albums.append(row)
    return albums


#Loads Users Rating List
def load_user_data():
    user_data = []
    with open('userList.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_data.append(row)
    return user_data


#Merging Data for Simpler User
def merge_data(albums, user_data):
    merged_data = []
    for album_info in albums:
        album_name = album_info['ï»¿Album Name']
        for user_album in user_data:
            if user_album['Album'] == album_name:
                album_info.update(user_album)
                merged_data.append(album_info)
                break
    return merged_data

def sort_albums(albums):
    return sorted(albums, key=lambda x: float(x['Total']), reverse=True)

album_data = load_album_data()
user_data = load_user_data()
merged_data = merge_data(album_data, user_data)
sorted_albums = sort_albums(merged_data)




#Window Button
window = Tk()
window.geometry("1280x720")
window['background'] = '#D7D6FD'


#Configuring and Creating the Scrollbar
#Creating a Frame
mainFrame = Frame(window)
mainFrame.pack(fill=BOTH, expand=1)

#Creating a Canvas
myCanvas = Canvas(mainFrame)
myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

#Adding Scrollbar
windowScrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=myCanvas.yview)
windowScrollbar.pack(side=RIGHT, fill=Y)

#Configure the Canvas
myCanvas.configure(yscrollcommand=windowScrollbar.set)
myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))


#Creating Another Frame inside myCanvas
newFrame= Frame(myCanvas, bg="#D7D6FD")

#New Frame to the Canvas
myCanvas.create_window((0,0), window=newFrame, anchor="nw")


#Header
headFrame = Frame(newFrame, width=1000, bg='#D7D6FD')
headFrame.pack(anchor="w")


#Logo Image
logoImage = PhotoImage(file="RTLogo.png")
imgButton= Button(headFrame, height= 50, width=50, image=logoImage, bg="#D7D6FD", bd="0", command=homePage)
imgButton.pack(padx=10, pady=10, anchor="w", side=LEFT)

#Search image photo path
searchIMG = PhotoImage(file="searchButton.png")

#Navigation Frame for the Nav Bar
navFrame = Frame(newFrame, bg= "#6461BB")
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

#Search Button for Searching Music
searchButton = Button(navFrame, height= 50, width=50, image=searchIMG, bg="#6461BB", bd="0", command=searchPage)
searchButton.pack(side=RIGHT, padx=30, pady=20)


imageFrame = Frame(newFrame, bg="#D7D6FD")
imageFrame.pack(side=LEFT, anchor='nw')

def display_albums(albums):
    for widget in imageFrame.winfo_children():
        widget.destroy()

    num_albums_per_row = 4

    for i, album in enumerate(albums, start=1):
        album_name = album['ï»¿Album Name']
        artist = album['Artist']
        total_rating = album['Total']
        image_path = album['Directory']

        photo = PhotoImage(file=image_path)
        label_text = f"{i}. {album_name} - {artist} (Rating: {total_rating})"

        album = Button(imageFrame, text=label_text, image=photo, height=240, width=240, compound='top', bg='black', fg='white', font=("Segoe UI", 10), command=lambda t=album_name: ratingWindow(t))
        album.photo = photo

        # Use grid to place the album in the imageFrame
        album.grid(row=(i-1)//num_albums_per_row, column=(i-1)%num_albums_per_row, padx=5, pady=5)
    




def filter_by_genre_label_format(genre, label, format_):
    filtered_albums = merged_data
    if genre != "All":
        filtered_albums = [album for album in filtered_albums if album['Genre'] == genre]
    if label != "All":
        filtered_albums = [album for album in filtered_albums if album['Label'] == label]
    if format_ != "All":
        filtered_albums = [album for album in filtered_albums if album['Format'] == format_]
    
    # Sort the filtered albums based on total rating in descending order
    sorted_albums = sort_albums(filtered_albums)
    
    # Display the filtered and sorted albums
    display_albums(sorted_albums)

# Add a Filter section for Genre, Label, and Format
filter_frame = Frame(newFrame, bg="#AAA8F1")
filter_frame.pack(side=RIGHT, anchor='ne', fil=Y, expand=False )

#Creating Style for the Filter Button
optionButtonStyle = {'bg': '#6461BB', 'fg': 'white', 'font': ('Segoe UI', 12)}



genre_label = Label(filter_frame, text="Filter by Genre:", font=("Segoe UI", 12), bg="#AAA8F1", fg='white')
genre_label.grid(column=0, row=0, padx=10, pady=10)

genre_options = set(album['Genre'] for album in merged_data)
genre_var = StringVar()
genre_var.set("All")
genre_dropdown = OptionMenu(filter_frame, genre_var, "All", *genre_options)
genre_dropdown.config(**optionButtonStyle)
genre_dropdown.grid(column=0, row=1, padx=10, pady=10)

label_label = Label(filter_frame, text="Filter by Label:", font=("Segoe UI", 12), bg="#AAA8F1", fg='white')
label_label.grid(column=0, row=2, padx=10, pady=10)

label_options = set(album['Label'] for album in merged_data)
label_var = StringVar()
label_var.set("All")
label_dropdown = OptionMenu(filter_frame, label_var, "All", *label_options)
label_dropdown.config(**optionButtonStyle)
label_dropdown.grid(column=0, row=3, padx=10, pady=10)

format_label = Label(filter_frame, text="Filter by Format:", font=("Segoe UI", 12), bg="#AAA8F1", fg='white')
format_label.grid(column=0, row=4, padx=10, pady=10)

format_options = set(album['Format'] for album in merged_data)
format_var = StringVar()
format_var.set("All")
format_dropdown = OptionMenu(filter_frame, format_var, "All", *format_options)
format_dropdown.config(**optionButtonStyle)
format_dropdown.grid(column=0, row=5, padx=10, pady=10)

filter_button = Button(filter_frame, text="Filter", command=lambda: filter_by_genre_label_format(genre_var.get(), label_var.get(), format_var.get()), bg='#6461BB', fg='white', font=("Segoe UI", 12))
filter_button.grid(column=0, row=6, padx=10, pady=10)

# Display all albums initially
display_albums(sorted_albums)

window.resizable(width=False, height=False)
window.mainloop()

    
