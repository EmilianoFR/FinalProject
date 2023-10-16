from breezypythongui import EasyFrame
import tkinter as tk
from tkinter import Entry
from tkinter import *
from tkinter import PhotoImage


#Main class for application
class ShelterApp(EasyFrame):
    def __init__(self, root):
        self.root = root
        self.root.title("Izzy's Shelter")
        self.create_main_window()

    # Creates the GUI's main window which includes buttons to navigate to available cats
    def create_main_window(self):
        main_window = self.root
        main_window.title("Izzy's Shelter")

        window_width = 800  # Change to your desired width
        window_height = 600  # Change to your desired height

        # Set the window dimensions
        main_window.geometry(f"{window_width}x{window_height}")

        # Set the background color using hexadecimal color code
        main_window.configure(bg="#2ABBF6")

        header = tk.Label(main_window, text="Izzy's Shelter", foreground="black", background="#2ABBF6", font=("Helvetica", 24))
        header.pack()

        # Load and display your image
        image_path = "C:/Users/emife/Desktop/Final Project/Photos/IzzysShelter.png"
        img = PhotoImage(file=image_path)
        img_label = tk.Label(main_window, image=img)
        img_label.image = img  # Store the PhotoImage
        img_label.pack()


        # Create a frame to contain the "Inquiry Form" and "Available Cats" buttons
        buttons_frame = tk.Frame(main_window, bg="#2ABBF6")
        buttons_frame.pack()

        # Inquiry button will open a form in a new window for the user to fill out with their contact information
        # so that they can reach out in regards to a listed pet.
        inquiry_button = tk.Button(buttons_frame, text="Inquiry form", width=25, height=5, bg="#237EDA", fg="black", command=self.open_inquiry_form)
        inquiry_button.grid(row=0, column=0, padx=10)  # Add horizontal padding

        cats_button = tk.Button(buttons_frame, text="View Cats", width=25, height=5, bg="#237EDA", fg="black", command=self.open_cat_window)
        cats_button.grid(row=0, column=1, padx=10)  # Add horizontal padding


    # Method for the cat button on the main window. Button opens a new window called "Cat Window" which shows the user all available cats.
    #And buttons for corresponding cats that provides their information
    def open_cat_window(self):
        cat_window = tk.Toplevel(self.root)
        cat_window.title("Available Cats")
        cat_label = tk.Label(cat_window, text="Available Cats", bg="#2ABBF6", font=("Helvetica", 24))
        cat_label.pack()
        cat_window.configure(bg="#2ABBF6")

        # Load and display your images
        image1 = "C:/Users/emife/Desktop/Final Project/Photos/Cat1.png"
        render1 = PhotoImage(file=image1)
        img_label1 = tk.Label(cat_window, image=render1)
        img_label1.pack(side=tk.LEFT)

        image2 = "C:/Users/emife/Desktop/Final Project/Photos/Cat2.png"
        render2 = PhotoImage(file=image2)
        img_label2 = tk.Label(cat_window, image=render2)
        img_label2.pack(side=tk.LEFT)

        image3 = "C:/Users/emife/Desktop/Final Project/Photos/Cat3.png"
        render3 = PhotoImage(file=image3)
        img_label3 = tk.Label(cat_window, image=render3)
        img_label3.pack(side=tk.LEFT)

        # Update the labels with the modified PhotoImage objects
        img_label1.configure(image=render1)
        img_label2.configure(image=render2)
        img_label3.configure(image=render3)

        # Store the PhotoImage as instance variables to prevent garbage collection
        cat_window.image1 = render1
        cat_window.image2 = render2
        cat_window.image3 = render3

        # Add buttons to display cat information in a new "Info Window"
        cat1_button = tk.Button(cat_window, text="Cat 1 Info", command=lambda: self.display_cat_info(Cat1, "Cat 1 Info"))
        cat2_button = tk.Button(cat_window, text="Cat 2 Info", command=lambda: self.display_cat_info(Cat2, "Cat 2 Info"))
        cat3_button = tk.Button(cat_window, text="Cat 3 Info", command=lambda: self.display_cat_info(Cat3, "Cat 3 Info"))

        cat1_button.pack()
        cat2_button.pack()
        cat3_button.pack()

    # Display cat information in the same cat window
    # Display cat information in a new "Info Window"
    def display_cat_info(self, cat, title):
        info_window = tk.Toplevel(self.root)
        info_window.title(title)

        name_label = tk.Label(info_window, text=f"Name: {cat.name}")
        name_label.pack()

        age_label = tk.Label(info_window, text=f"Age: {cat.age}")
        age_label.pack()

        fixed_label = tk.Label(info_window, text=f"Fixed: {cat.fixed}")
        fixed_label.pack()

        gender_label = tk.Label(info_window, text=f"Gender: {cat.gender}")
        gender_label.pack()


    #Method for the Inquiry Form, provides text boxes that are labeled with the desired information for the user to fill out and submit 

    def open_inquiry_form(self):
        inquiry_window = tk.Toplevel(self.root)
        inquiry_window.title("Inquiry Form")

        def validate_text(text):
            # Validation function to allow only letters (no numbers)
            return text.isalpha() or text == ""

        def validate_phone(text):
            # Validation function to allow only numbers (no letters)
            return text.isdigit() or text == ""

        
        validate_text_cmd = (inquiry_window.register(validate_text), '%P')
        validate_phone_cmd = (inquiry_window.register(validate_phone), '%P')


        #Labels for text entry 
        name_label = tk.Label(inquiry_window, text="Enter Full Name")
        user_name = Entry(inquiry_window, fg="black", bg="white", width=50, validate="key", validatecommand=validate_text_cmd)
        name_label.pack()
        user_name.pack()

        phone_label = tk.Label(inquiry_window, text="Enter Phone Number")
        user_phone = Entry(inquiry_window, fg="black", bg="white", width=50, validate="key", validatecommand=validate_phone_cmd)
        phone_label.pack()
        user_phone.pack()

        email_label = tk.Label(inquiry_window, text="Enter Email")
        user_email = Entry(inquiry_window, fg="black", bg="white", width=50)
        email_label.pack()
        user_email.pack()

        pet_label = tk.Label(inquiry_window, text="Enter Pet Name")
        user_pet = Entry(inquiry_window, fg="black", bg="white", width=50, validate="key", validatecommand=validate_text_cmd)
        pet_label.pack()
        user_pet.pack()

        #Submit form button method closes the window
        def submit_form():
            inquiry_window.destroy()

        submit_button = tk.Button(inquiry_window, text="Submit form", command=submit_form)
        submit_button.pack()

#Used to store pets information and also contains the method to return the info which is called on by the pets button
class Pet_Info(ShelterApp):
    def __init__(self, name, age, fixed, gender):
        self.name = name
        self.age = age
        self.fixed = fixed
        self.gender = gender

#Variables used to fill out a pets information using the Pet_Info class
Cat1 = Pet_Info("Robin", "4 years", "Yes", "Female")
Cat2 = Pet_Info("Vivi", "2 year", "No", "Female")
Cat3 = Pet_Info("Zoro", "3 year", "Yes", "Male")


if __name__ == "__main__":

    IzzysShelter = tk.Tk()
    app = ShelterApp(IzzysShelter)
    IzzysShelter.mainloop()

