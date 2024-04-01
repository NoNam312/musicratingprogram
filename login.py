from tkinter import *
from subprocess import  call



window = Tk()
window.geometry("1280x720")
window['background'] = '#D7D6FD'



def homePage():
    global window
    window.destroy()
    call(["python", "home.py"])

def listPage():
    global window
    window.destroy()
    call(["python", "list.py"])

def listPage():
    global window
    window.destroy()
    call(["python", "search.py"])

#Header
headFrame = Frame(window, width=1000, bg='#D7D6FD')
headFrame.pack(anchor="w")

logoImage = PhotoImage(file="RTLogo.png")
imgButton= Button(headFrame, height= 70, width=70, image=logoImage, bg="#D7D6FD", bd="0", command=homePage)
imgButton.pack(padx=10, pady=10, anchor="w", side=LEFT)

# Navigation Frame for the Nav Bar
navbar_frame = Frame(window, bg="#6461BB")
navbar_frame.pack(side=TOP, fill=X)

# Create the buttons in the navigation bar
homepageButton = Button(navbar_frame, text="Home", command=homePage, bg="#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
homepageButton.pack(side=LEFT, padx=30, pady=20)

listpageButton = Button(navbar_frame, text="List", command=lambda: navigate_to("List"), bg="#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
listpageButton.pack(side=LEFT, padx=30, pady=20)

recpageButton = Button(navbar_frame, text="Rec", command=lambda: navigate_to("Rec"), bg="#6461BB", bd="0", fg="white", font=("Segoe UI", 12))
recpageButton.pack(side=LEFT, padx=30, pady=20)




loginFrame = Frame(window, padx=50, pady=60, background="white", bd="2")
loginFrame.pack(padx=10, pady=40)

loginLabel = Label(loginFrame, text="Login", font=("Segoe UI", 20), justify="center", background='#8885DD', foreground="white", pady=10)
loginLabel.pack(padx=10, pady=10)

usernameText = Entry(loginFrame, width=40, bd="2", font=("Segoe UI", 10), bg="#F2F2F2")
passwordText = Entry(loginFrame, width=40, bd="2", font=("Segoe UI", 10), bg="#F2F2F2", show="*")

usernameText.pack(padx=5, pady=10)
passwordText.pack(padx=5, pady=10)

loginButton = Button(loginFrame, width=10, height="1", text="Login", bg="#A1C3FF", foreground="white", font=("Segoe UI", 12))
loginButton.pack(padx=10, pady=40)





window.mainloop()
