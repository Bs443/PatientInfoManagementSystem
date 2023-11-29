from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class DictDatabase:
    def __init__(self) -> None:
        self.database = {'Patient HN': {}, 'First Name': {}, 'Last Name': {}, 'Date of Birth': {}, 'Month of Birth': {},
                         'Year of Birth': {}, 'Gender': {}, 'Home Address': {}, 'Contact Number': {}, 'Blood Type': {},
                         'Medical History': {}, 'Doctor': {}}

    def Insert(self, hn, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber,
               bloodType, history, doctor) -> None:
        # add patient data to the database
        self.database['Patient HN'][hn] = hn
        self.database['First Name'][hn] = firstname
        self.database['Last Name'][hn] = lastname
        self.database['Date of Birth'][hn] = dateOfBirth
        self.database['Month of Birth'][hn] = monthOfBirth
        self.database['Year of Birth'][hn] = yearOfBirth
        self.database['Gender'][hn] = gender
        self.database['Home Address'][hn] = address
        self.database['Contact Number'][hn] = contactNumber
        self.database['Blood Type'][hn] = bloodType
        self.database['Medical History'][hn] = history
        self.database['Doctor'][hn] = doctor

    def Update(self, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber,
               bloodType, history, doctor, hn):
        # update patient data in the database
        self.database['Patient HN'][hn] = hn
        self.database['First Name'][hn] = firstname
        self.database['Last Name'][hn] = lastname
        self.database['Date of Birth'][hn] = dateOfBirth
        self.database['Month of Birth'][hn] = monthOfBirth
        self.database['Year of Birth'][hn] = yearOfBirth
        self.database['Gender'][hn] = gender
        self.database['Home Address'][hn] = address
        self.database['Contact Number'][hn] = contactNumber
        self.database['Blood Type'][hn] = bloodType
        self.database['Medical History'][hn] = history
        self.database['Doctor'][hn] = doctor

    def Search(self, hn) -> list[tuple[str, str, str, str, str, str, str, str, str, str, str, str]]:
        # search for patient data in the database
        try:
            records = []
            index = self.database['Patient HN'][hn]
            as_tuples = (hn, self.database['First Name'][index], self.database['Last Name'][index],
                         self.database['Date of Birth'][index], self.database['Month of Birth'][index],
                         self.database['Year of Birth'][index], self.database['Gender'][index],
                         self.database['Home Address'][index], self.database['Contact Number'][index],
                         self.database['Blood Type'][index], self.database['Medical History'][index],
                         self.database['Doctor'][index])
            records.append(as_tuples)
            return records

        except KeyError:
            messagebox.showerror("The patient does not exist")
            return []

    def Delete(self, hn):
        # delete patient data in the database
        for key in self.database:
            del self.database[key][hn]
        messagebox.showinfo("Deleted data", "Successfully Deleted the Patient data in the database")

    def Display(self) -> list[tuple[str, str, str, str, str, str, str, str, str, str, str, str]]:
        # display all patient data in the database
        records = []
        for hn in self.database['Patient HN']:
            as_tuples = (
            hn, self.database['First Name'][hn], self.database['Last Name'][hn], self.database['Date of Birth'][hn],
            self.database['Month of Birth'][hn], self.database['Year of Birth'][hn], self.database['Gender'][hn],
            self.database['Home Address'][hn], self.database['Contact Number'][hn], self.database['Blood Type'][hn],
            self.database['Medical History'][hn], self.database['Doctor'][hn])
            records.append(as_tuples)

        return records


class Values:
    def Valid(self, hn, firstname, lastname, contactNumber):
        if not (hn.isdigit() and (len(hn) == 3)):
            return "hn"
        elif not (firstname.isalpha()):
            return "firstname"
        elif not (lastname.isalpha()):
            return "lastname"
        elif not (contactNumber.isdigit() and (len(contactNumber) == 10)):
            return "contactNumber"
        else:
            return "SUCCESS"

    def iferror(self, hn, firstname, lastname, contactNumber):
        if not (hn.isdigit() and (len(hn) == 3)):
            raise ValueError
        elif not (firstname.isalpha()):
            raise ValueError
        elif not (lastname.isalpha()):
            raise ValueError
        elif not (contactNumber.isdigit() and (len(contactNumber) == 10)):
            raise ValueError
        else:
            pass


class Color:
    def __init__(self, color='SlateGray3'):
        self.__color = color

    def getColor(self):
        return self.__color


class HomePage(Color):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.bg_color = self.getColor()
        self.home = Tk()
        self.home.title("PATIENT INFO")
        self.home.minsize(width=500, height=350)
        self.home.geometry("500x350")
        self.home.config(bg=self.bg_color)
        # Home Page Header
        Label(self.home, fg='white', bg='black', text="Home Page",
              font='arial 15 bold', width=20).place(x=150, y=10)
        # Home Page Buttons
        Button(self.home, width=20, text="Admit", font='arial 15 bold', command=self.Insert).place(x=135, y=50)
        Button(self.home, width=20, text="Update", font='arial 15 bold', command=self.Update).place(x=135, y=100)
        Button(self.home, width=20, text="Search", font='arial 15 bold', command=self.Search).place(x=135, y=150)
        Button(self.home, width=20, text="Delete", font='arial 15 bold', command=self.Delete).place(x=135, y=200)
        Button(self.home, width=20, text="Display", font='arial 15 bold', command=self.Display).place(x=135, y=250)
        Button(self.home, width=20, text="Exit", font='arial 15 bold', command=self.home.destroy).place(x=135, y=300)

        self.home.mainloop()

    # Insert new patient info
    def Insert(self):
        self.insertWindow = InsertWindow(self.database)

    # Update old patient info
    def Update(self):
        self.updateHNWindow = Tk()
        self.updateHNWindow.title("Update data")
        self.updateHNWindow.config(bg=self.bg_color)
        self.updateHNWindow.geometry("300x150")

        self.hn = StringVar()

        # Label
        Label(self.updateHNWindow, text="Enter the HN to update", bg='SlateGray3', width=20).place(x=60, y=10)

        # Entry
        self.hn = Entry(self.updateHNWindow, width=5, textvariable=self.hn)
        self.hn.place(x=120, y=50)

        # Button
        Button(self.updateHNWindow, width=10, text="Update", command=self.updateHN).place(x=90, y=100)

        self.updateHNWindow.mainloop()

    def updateHN(self):
        self.updateWindow = UpdateWindow(self.hn.get(), self.database)
        self.updateHNWindow.destroy()

    # Search for patient info
    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search", self.database)

    # Delete patient info from db
    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete", self.database)

    # Show all patient info in db
    def Display(self):
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)


class InsertWindow(Color):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.bg_color = self.getColor()
        self.window = Tk()
        self.window.title("Insert Patient Data")
        self.window.minsize(width=500, height=550)
        self.window.geometry("500x550")
        self.window.config(bg=self.bg_color)

        # PATIENT INFO
        self.hn = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.address = StringVar()
        self.contactNumber = StringVar()
        self.history = StringVar()
        self.doctor = StringVar()
        self.genderType = ["Male", "Female"]
        self.dateType = list(range(1, 32))
        self.monthType = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearType = list(range(1900, 2020))
        self.bloodListType = ["A", "B", "O", "AB"]

        # Label
        Label(self.window, text="Patient HN", font='arial 12 bold', width=25).place(x=10, y=10)
        Label(self.window, text="Patient First Name", font='arial 12 bold', width=25).place(x=10, y=50)
        Label(self.window, text="Patient Last Name", font='arial 12 bold', width=25).place(x=10, y=90)
        Label(self.window, text="Date of Birth", font='arial 12 bold', width=25).place(x=10, y=130)
        Label(self.window, text="Month of Birth", font='arial 12 bold', width=25).place(x=10, y=170)
        Label(self.window, text="Year of Birth", font='arial 12 bold', width=25).place(x=10, y=210)
        Label(self.window, text="Patient Gender", font='arial 12 bold', width=25).place(x=10, y=250)
        Label(self.window, text="Patient Address", font='arial 12 bold', width=25).place(x=10, y=290)
        Label(self.window, text="Patient Contact Number", font='arial 12 bold', width=25).place(x=10, y=330)
        Label(self.window, text="Patient Blood Type", font='arial 12 bold', width=25).place(x=10, y=370)
        Label(self.window, text="History of Patient", font='arial 12 bold', width=25).place(x=10, y=410)
        Label(self.window, text="Name of Doctor", font='arial 12 bold', width=25).place(x=10, y=450)

        # Entry
        self.hnEntry = Entry(self.window, width=25, textvariable=self.hn)
        self.firstnameEntry = Entry(self.window, width=25, textvariable=self.firstname)
        self.lastnameEntry = Entry(self.window, width=25, textvariable=self.lastname)
        self.addressEntry = Entry(self.window, width=25, textvariable=self.address)
        self.contactNumberEntry = Entry(self.window, width=25, textvariable=self.contactNumber)
        self.historyEntry = Entry(self.window, width=25, textvariable=self.history)
        self.doctorEntry = Entry(self.window, width=25, textvariable=self.doctor)

        self.hnEntry.place(x=200, y=10)
        self.firstnameEntry.place(x=200, y=50)
        self.lastnameEntry.place(x=200, y=90)
        self.addressEntry.place(x=200, y=290)
        self.contactNumberEntry.place(x=200, y=330)
        self.historyEntry.place(x=200, y=410)
        self.doctorEntry.place(x=200, y=450)

        # Combobox
        self.dateOfBirthBox = ttk.Combobox(self.window, values=self.dateType, width=25)
        self.monthOfBirthBox = ttk.Combobox(self.window, values=self.monthType, width=25)
        self.yearOfBirthBox = ttk.Combobox(self.window, values=self.yearType, width=25)
        self.genderBox = ttk.Combobox(self.window, values=self.genderType, width=25)
        self.bloodListBox = ttk.Combobox(self.window, values=self.bloodListType, width=25)

        self.dateOfBirthBox.place(x=200, y=130)
        self.monthOfBirthBox.place(x=200, y=170)
        self.yearOfBirthBox.place(x=200, y=210)
        self.genderBox.place(x=200, y=250)
        self.bloodListBox.place(x=200, y=370)

        # Button
        Button(self.window, width=10, font='arial 10 bold', text="Insert", command=self.Insert).place(x=10, y=500)
        Button(self.window, width=10, font='arial 10 bold', text="Reset", command=self.Reset).place(x=110, y=500)
        Button(self.window, width=10, font='arial 10 bold', text="Close",
               command=self.window.destroy).place(x=350, y=500)

        self.window.mainloop()

    def Insert(self):
        self.values = Values()

        try:
            self.test = self.values.Valid(self.hnEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                          self.contactNumberEntry.get())
            self.values.iferror(self.hnEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                self.contactNumberEntry.get())
        except ValueError:
            self.valueErrorMessage = "Invalid input in field " + self.test
            messagebox.showwarning("Error", self.valueErrorMessage)
            return None

        if (self.test == "SUCCESS"):
            self.database.Insert(self.hnEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                 self.dateOfBirthBox.get(),
                                 self.monthOfBirthBox.get(), self.yearOfBirthBox.get(), self.genderBox.get(),
                                 self.addressEntry.get(),
                                 self.contactNumberEntry.get(), self.bloodListBox.get(),
                                 self.historyEntry.get(), self.doctorEntry.get())
            messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")

    def Reset(self):
        self.hnEntry.delete(0, END)
        self.firstnameEntry.delete(0, END)
        self.lastnameEntry.delete(0, END)
        self.dateOfBirthBox.set("")
        self.monthOfBirthBox.set("")
        self.yearOfBirthBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, END)
        self.contactNumberEntry.delete(0, END)
        self.bloodListBox.set("")
        self.historyEntry.delete(0, END)
        self.doctorEntry.delete(0, END)


class UpdateWindow(Color):
    def __init__(self, hn, database):
        super().__init__()
        self.database = database
        self.bg_color = self.getColor()
        self.window = Tk()
        self.window.title("Update data")
        self.window.minsize(width=800, height=550)
        self.window.geometry("800x550")
        self.window.config(bg=self.bg_color)

        self.hn = hn
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.address = StringVar()
        self.contactNumber = StringVar()
        self.history = StringVar()
        self.doctor = StringVar()
        self.genderType = ["Male", "Female"]
        self.dateType = list(range(1, 32))
        self.monthType = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearType = list(range(1900, 2020))
        self.bloodListType = ["A", "B", "O", "AB"]

        # Label
        Label(self.window, text="Patient HN", font='arial 12 bold', width=25).place(x=10, y=10)
        Label(self.window, text="Patient First Name", font='arial 12 bold', width=25).place(x=10, y=50)
        Label(self.window, text="Patient Last Name", font='arial 12 bold', width=25).place(x=10, y=90)
        Label(self.window, text="Date of Birth", font='arial 12 bold', width=25).place(x=10, y=130)
        Label(self.window, text="Month of Birth", font='arial 12 bold', width=25).place(x=10, y=170)
        Label(self.window, text="Year of Birth", font='arial 12 bold', width=25).place(x=10, y=210)
        Label(self.window, text="Patient Gender", font='arial 12 bold', width=25).place(x=10, y=250)
        Label(self.window, text="Patient Address", font='arial 12 bold', width=25).place(x=10, y=290)
        Label(self.window, text="Patient Contact Number", font='arial 12 bold', width=25).place(x=10, y=330)
        Label(self.window, text="Patient Blood Type", font='arial 12 bold', width=25).place(x=10, y=370)
        Label(self.window, text="History of Patient", font='arial 12 bold', width=25).place(x=10, y=410)
        Label(self.window, text="Name of Doctor", font='arial 12 bold', width=25).place(x=10, y=450)

        # Set previous values

        self.searchResults = self.database.Search(hn)

        # Show previous values
        Label(self.window, text=self.searchResults[0][1], width=25).place(x=200, y=50)
        Label(self.window, text=self.searchResults[0][2], width=25).place(x=200, y=90)
        Label(self.window, text=self.searchResults[0][3], width=25).place(x=200, y=130)
        Label(self.window, text=self.searchResults[0][4], width=25).place(x=200, y=170)
        Label(self.window, text=self.searchResults[0][5], width=25).place(x=200, y=210)
        Label(self.window, text=self.searchResults[0][6], width=25).place(x=200, y=250)
        Label(self.window, text=self.searchResults[0][7], width=25).place(x=200, y=290)
        Label(self.window, text=self.searchResults[0][8], width=25).place(x=200, y=330)
        Label(self.window, text=self.searchResults[0][9], width=25).place(x=200, y=370)
        Label(self.window, text=self.searchResults[0][10], width=25).place(x=200, y=410)
        Label(self.window, text=self.searchResults[0][11], width=25).place(x=200, y=450)

        # Entry
        self.hnEntry = Entry(self.window, width=25, textvariable=self.hn)
        self.firstnameEntry = Entry(self.window, width=25, textvariable=self.firstname)
        self.lastnameEntry = Entry(self.window, width=25, textvariable=self.lastname)
        self.addressEntry = Entry(self.window, width=25, textvariable=self.address)
        self.contactNumberEntry = Entry(self.window, width=25, textvariable=self.contactNumber)
        self.historyEntry = Entry(self.window, width=25, textvariable=self.history)
        self.doctorEntry = Entry(self.window, width=25, textvariable=self.doctor)

        self.hnEntry.place(x=500, y=10)
        self.firstnameEntry.place(x=500, y=50)
        self.lastnameEntry.place(x=500, y=90)
        self.addressEntry.place(x=500, y=290)
        self.contactNumberEntry.place(x=500, y=330)
        self.historyEntry.place(x=500, y=410)
        self.doctorEntry.place(x=500, y=450)

        # Combobox
        self.dateOfBirthBox = ttk.Combobox(self.window, values=self.dateType, width=20)
        self.monthOfBirthBox = ttk.Combobox(self.window, values=self.monthType, width=20)
        self.yearOfBirthBox = ttk.Combobox(self.window, values=self.yearType, width=20)
        self.genderBox = ttk.Combobox(self.window, values=self.genderType, width=20)
        self.bloodListBox = ttk.Combobox(self.window, values=self.bloodListType, width=20)

        self.dateOfBirthBox.place(x=500, y=130)
        self.monthOfBirthBox.place(x=500, y=170)
        self.yearOfBirthBox.place(x=500, y=210)
        self.genderBox.place(x=500, y=250)
        self.bloodListBox.place(x=500, y=370)

        # Button
        Button(self.window, width=10, font='arial 10 bold',
               text="Update", command=self.Update).place(x=10, y=500)
        Button(self.window, width=10, font='arial 10 bold',
               text="Reset", command=self.Reset).place(x=150, y=500)
        Button(self.window, width=10, font='arial 10 bold',
               text="Close", command=self.window.destroy).place(x=650, y=500)

        self.window.mainloop()

    def Update(self):
        self.database.Update(self.firstnameEntry.get(), self.lastnameEntry.get(), self.dateOfBirthBox.get(),
                             self.monthOfBirthBox.get(),
                             self.yearOfBirthBox.get(), self.genderBox.get(), self.addressEntry.get(),
                             self.contactNumberEntry.get(),
                             self.bloodListBox.get(), self.historyEntry.get(),
                             self.doctorEntry.get(), self.hn)
        messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.hnEntry.delete(0, END)
        self.firstnameEntry.delete(0, END)
        self.lastnameEntry.delete(0, END)
        self.dateOfBirthBox.set("")
        self.monthOfBirthBox.set("")
        self.yearOfBirthBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, END)
        self.contactNumberEntry.delete(0, END)
        self.bloodListBox.set("")
        self.historyEntry.delete(0, END)
        self.doctorEntry.delete(0, END)


class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = Tk()
        self.databaseViewWindow.title("Database View")

        # Label widgets
        Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "id", "firstname", "lastname", "dateOfBirth", "monthOfBirth", "yearOfBirth", "gender", "address",
        "contactNumber", "bloodType", "history", "doctor")

        # Treeview column headings
        self.databaseView.heading("id", text="Patient HN")
        self.databaseView.heading("firstname", text="First Name")
        self.databaseView.heading("lastname", text="Last Name")
        self.databaseView.heading("dateOfBirth", text="Date of Birth")
        self.databaseView.heading("monthOfBirth", text="Month of Birth")
        self.databaseView.heading("yearOfBirth", text="Year of Birth")
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("address", text="Home Address")
        self.databaseView.heading("contactNumber", text="Contact Number")
        self.databaseView.heading("bloodType", text="Blood Type")
        self.databaseView.heading("history", text="History")
        self.databaseView.heading("doctor", text="Doctor")

        # Treeview columns
        self.databaseView.column("id", width=100)
        self.databaseView.column("firstname", width=100)
        self.databaseView.column("lastname", width=100)
        self.databaseView.column("dateOfBirth", width=100)
        self.databaseView.column("monthOfBirth", width=100)
        self.databaseView.column("yearOfBirth", width=100)
        self.databaseView.column("gender", width=100)
        self.databaseView.column("address", width=200)
        self.databaseView.column("contactNumber", width=100)
        self.databaseView.column("bloodType", width=100)
        self.databaseView.column("history", width=100)
        self.databaseView.column("doctor", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow(Color):
    def __init__(self, task, database):
        super().__init__()
        self.database = database
        self.bg_color = self.getColor()
        window = Tk()
        window.title(task + " data")
        window.minsize(width=400, height=150)
        window.geometry("400x150")
        window.config(bg=self.bg_color)

        self.hn = StringVar()
        self.heading = "Please enter Patient HN to " + task

        # Label
        Label(window, text=self.heading, bg='SlateGray3', width=40).place(x=20, y=10)
        Label(window, text="Patient HN", bg='SlateGray3', width=10).place(x=150, y=40)

        # Entry
        self.hnEntry = Entry(window, width=5, textvariable=self.hn)
        self.hnEntry.place(x=165, y=70)

        # Button
        if (task == "Search"):
            Button(window, width=20, text=task, command=self.Search).place(x=90, y=110)
        elif (task == "Delete"):
            Button(window, width=20, text=task, command=self.Delete).place(x=90, y=110)

    def Search(self):
        self.data = self.database.Search(self.hnEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database.Delete(self.hnEntry.get())


if __name__ == '__main__':
    database = DictDatabase()
    HomePage(database)
