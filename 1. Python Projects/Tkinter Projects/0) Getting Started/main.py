import tkinter as tk
import _sqlite3

#############################################################################################################################
#                                                                                                                           #
#  1) Tkinter is a default library in python and is very easy to work with.                                                 #
#  2) What makes tkinter interesting are widgets.                                                                           #
#  3) Important widgets-- Root, Button, Entry, ComboBox, CheckButton, Radio, ScrolledText, SpinBox, MenuBar, Notebook.      #
#                                                                                                                           #
#############################################################################################################################


###Basics###


                            ##1. define Root widget.

#Tk root widget, which is a window with a title bar and other decoration provided by the window manager. The root widget has to be created before any other widgets and there can only be one root widget.
root = tk.Tk() ##defining a root instance variable.



                            ##2. Title of root widget.

root.title('Student Management System') ##title of the main window.
root.geometry('350x200') ##setting the size of the display window.



                             ##3. Other necessary widgets.

###Widget 1>
##A Label is a Tkinter Widget class, which is used to display text or an image.
# The label is a widget that the user just views but not interact with.
introduction_label = tk.Label(root, text="Hello World !")
introduction_label.pack() #The pack method tells Tk to fit the size of the window to the given text alternatively you could have used the grid widget to place the label at a certain position.

###Widget 2>
##A Button is a Tkinter Widget class, which can be made to perform operations upon click.
# User can interact with it.
def clicked():
    bt.configure(text="Button was clicked !!")
bt=tk.Button(root, text='Click this button', bg='white', fg='black', command=clicked)
bt.pack()



##########################################################################################################


###Databases###
##It can be remembered as simple series of steps including-- connect, cursor, execute,  commit, close


                                ##1. Connect/create a database

##create a database or connect to one.
conn =  _sqlite3.connect('address_book.db')



                                ##2. Create a cursor

##Create cursor. Imagine it like a pointer that can be sent to different location in db and is used to manipulate it.
c = conn.cursor()


                                ##3. Perform Necessary Steps.

#Create table
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer    
        )""")


                                ##4. Commit Changes in DB

##commit the changes made to the database.
conn.commit()


                                ##5. Close the connection to the DB
conn.close()


##########################################################################################################

                                ###Never Forget##

##We call the Tkinter mainloop to process events and keep the display activated.
root.mainloop()