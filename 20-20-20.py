from tkinter import *
from vision import *


#function for starting session, start session if true
def start_session():
    l3 = Label(root, text = activation_instruction, wraplength = 490, justify = LEFT)
    l3.grid(row = 3, column = 0)
    start_button.configure(state = "disabled")
    if seek_and_detect() == False:
        l4 = Label(root, text = "Unable to connect to camera. Session Failed.", wraplength = 490, justify = LEFT)
        l4.grid(row = 4, column = 0)




# Text 

intro = ("The 20-20-20 rule dictates that for every 20 minutes that you look at a screen, you should take at least 20 seconds "
        "to look away from the screen at a target that is at least 50 feet away. This helps in preventing eye strain and promotes "
        "good visual hygiene.\n")

explanation = ("This program uses computer vision to moniter whether you are at your desk or not. It will determine whether or not to "
        "notify you to take a vision break depending on if you are at your computer or not. If you are away for more than a minute, a " 
        "vision break will not be needed. If not, a new prompt telling you to take a break will pop up. A report will be generated at "
        "the end of the session ")

activation_instruction = ("You are currently in session. To exit, close this window. The results of your session will be recorded in "
        "a file called session_results in the program folder.")
    
root = Tk()

# prevent window from being maximized 
root.resizable(width = False, height = False)

# set size (500 x 500) and title
root.geometry("500x500")
root.title("20-20-20: Eye Strain Prevention")



# text
l1= Label(root, text = intro ,wraplength = 490, justify = LEFT)
l1.grid(row = 0, column = 0)

l2= Label(root, text = explanation ,wraplength = 490, justify = LEFT)
l2.grid(row = 1, column = 0)

# button
start_button = Button(root, text = "Start", command = start_session)

start_button.grid(row = 2, column = 0)


root.mainloop()


