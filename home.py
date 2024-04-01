from tkinter import *
from subprocess import  call
import csv
from tkinter import messagebox
import webbrowser


class Album:
    def __init__(self, albumname):
        self.albumname = str(albumname)

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

def submit_rating():
    global productionEntry, vocalsEntry, instrumentalsEntry, enjoymentEntry, totalEntry
    try:
        productionValue = int(productionEntry.get())
        if 1 <= productionValue <= 10:
            productionRating = productionValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Production.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")
    
    try:
        vocalsValue = int(vocalsEntry.get())
        if 1 <= vocalsValue <= 10:
            vocalsRating = vocalsValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Vocals.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    try:
        instrumentalValue = int(instrumentalsEntry.get())
        if 1 <= instrumentalValue <= 10:
            instrumentalRating = instrumentalValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10. in Instrumentals")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    try:
        enjoymentValue = int(enjoymentEntry.get())
        if 1 <= enjoymentValue <= 10:
            enjoymentRating = enjoymentValue
        else:
            messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10 in Enjoyment.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rating.")

    averageValue = (productionRating + vocalsRating + instrumentalRating + enjoymentRating)/4
    totalEntry.delete(0, END)
    totalEntry.insert(0, round(averageValue, 1))

    

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


    submit_button = Button(ratingFrame, text="Submit Rating", command=submit_rating)
    submit_button.grid(column=1, row=5, pady=10, padx=10)



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
newWindow= Frame(myCanvas, bg="#D7D6FD")

#New Frame to the Canvas
myCanvas.create_window((0,0), window=newWindow, anchor="nw")


#Header
headFrame = Frame(newWindow, width=1000, bg='#D7D6FD')
headFrame.pack(anchor="w")

logoImage = PhotoImage(file="RTLogo.png")
imgButton= Button(headFrame, height= 50, width=50, image=logoImage, bg="#D7D6FD", bd="0", command=homePage)
imgButton.pack(padx=10, pady=10, anchor="w", side=LEFT)

searchIMG = PhotoImage(file="searchButton.png")

#Navigation Frame for the Nav Bar
navFrame = Frame(newWindow, bg= "#6461BB")
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


searchButton = Button(navFrame, height= 50, width=50, image=searchIMG, bg="#6461BB", bd="0", command=searchPage)
searchButton.pack(side=RIGHT, padx=30, pady=20)


#Frames for banners
bannersFrame = Frame(newWindow, height=300, width=1000)
bannersFrame.pack()

#URL Links for Banners
URL = "https://stackoverflow.com/questions/49369364/how-do-i-make-python-open-a-youtube-video"

banner1IMG = PhotoImage(file="drakeBanner.png")

#Canvas utilise instead of a banner
bannerC1 = Button(bannersFrame, image=banner1IMG, height=300, width=600, bg="red", command=lambda: webbrowser.open_new("https://soundcloud.com/search?q=baekhyun"))
bannerC2 = Button(bannersFrame, image=banner1IMG, height=300, width=600, bg="red", command=lambda: webbrowser.open_new("https://soundcloud.com/octobersveryown"))

#Mapping Banner
bannerC1.grid(column=0, row=0, padx=40, pady=10)
bannerC2.grid(column=1, row=0, padx=40, pady=10)


#ALBUM MAPPING
#1st Row
musicRow1 = Frame(newWindow, height=400, width=1000, bg="#AAA8F1")
musicRow1.pack(pady=40)

#Label 1st Row
loginLabel = Label(musicRow1, text="Login", font=("Segoe UI", 20), justify="center", background='#AAA8F1', foreground="white", pady=10)
loginLabel.pack( padx=10, pady=10)

#Albums
imageAlbum1 = PhotoImage(file=SearchAlbum("Anniversary"))
imageAlbum2 = PhotoImage(file=SearchAlbum("Trilogy"))
imageAlbum3 = PhotoImage(file=SearchAlbum("130MoodTRBL"))




exampleAlbum1 = Button(musicRow1, image=imageAlbum1, height=200, width=200, bd=0, command=lambda: ratingWindow("Anniversary"))
exampleAlbum1.pack(side=LEFT, padx=12, pady=20)

exampleAlbum2 = Button(musicRow1, image=imageAlbum2, height=200, width=200, bd=0, command=lambda: ratingWindow("Trilogy"))
exampleAlbum2.pack(side=LEFT, padx=12, pady=20)

exampleAlbum3 = Button(musicRow1, image=imageAlbum3, height=200, width=200, bd=0, command=lambda: ratingWindow("130MoodTRBLz"))
exampleAlbum3.pack(side=LEFT, padx=12, pady=20)

exampleAlbum4 = Button(musicRow1, image=banner1IMG, height=200, width=200, bd=0)
exampleAlbum4.pack(side=LEFT, padx=12, pady=20)

exampleAlbum5 = Button(musicRow1, image=banner1IMG, height=200, width=200, bd=0)
exampleAlbum5.pack(side=LEFT, padx=12, pady=20)

exampleAlbum6 = Button(musicRow1, image=banner1IMG, height=200, width=200, bd=0)
exampleAlbum6.pack(side=LEFT, padx=12, pady=20)

#2nd ROw
#1st Row
musicRow2 = Frame(newWindow, height=200, width=1000)
musicRow2.pack(pady=40)

#Albums
exampleAlbum7 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum7.pack(side=LEFT, padx=12)

exampleAlbum8 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum8.pack(side=LEFT, padx=12)

exampleAlbum9 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum9.pack(side=LEFT, padx=12)

exampleAlbum10 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum10.pack(side=LEFT, padx=12)

exampleAlbum11 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum11.pack(side=LEFT, padx=12)

exampleAlbum12 = Button(musicRow2, image=banner1IMG, height=200, width=200)
exampleAlbum12.pack(side=LEFT, padx=12)


#Mainloop and Fullscreen Attribute
window.mainloop()
