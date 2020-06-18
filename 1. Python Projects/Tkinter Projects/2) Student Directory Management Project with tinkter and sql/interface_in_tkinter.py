from tkinter import *
import SQLimplement as SQL

root=Tk()
root.title("Student Management System.")##title of the main window




####Entering the details of the Student.##############
heading_label=Label(root, text="Student Management system") ##Showing first message on the screen
heading_label.grid(row=1, column=1) ##Printing the message on the screen, can be done by pack or grid

Name=Label(root, text="Enter Name:") ##will display the name field in the interface.
Name.grid(row=2, column=0)

College=Label(root, text="Enter College:")
College.grid(row=3, column=0)

PhoneNumber=Label(root, text="Enter Phone Number:")
PhoneNumber.grid(row=4, column=0)




####Taking entry from the user.##################
Name_Entry=Entry(root, width="50", bg="#cbf542", fg="#060308")
Name_Entry.grid(row=2, column=1)

College_Entry=Entry(root, width="50", bg="#cbf542", fg="#060308")
College_Entry.grid(row=3, column=1)

PhoneNumber=Entry(root, width="50", bg="#cbf542", fg="#060308")
PhoneNumber.grid(row=4, column=1)



###Funtion to submit values entered from the user.###
def takeValues():
    try:
        name = Name_Entry.get()   ###getting the value of name.
        if name=="":
            raise EXCEPTION

        college=College_Entry.get() ###getting the value of collge.
        if college=="":
            raise EXCEPTION

        phone=PhoneNumber.get()  ###getting the value of phonenumber.
        if phone=="":
            raise EXCEPTION

    except Exception:
        print("Reenter all fields.")
    else:
        if type(phone)!=int:
            print("Please enter a valid phone number.")

    SQL.EnterDetails(name, college, int(phone) ) ###calling the function in SQLimplement file.



###Displaying the previously enterd values.
def ViewDetails():
    SQL.ViewDetails()




###Making Button to sumbit student details.#############
submit_button=Button(root, text="Submit Details", command=lambda : takeValues())
submit_button.grid(row=5, column=1)




###Making Button to view student details.##############
view_button=Button(root, text="View Details", command=lambda : ViewDetails())
view_button.grid(row=5, column=2)



###START THE LOOP.
root.mainloop()