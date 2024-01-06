import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nation_combobox.get()
            
            # Course Info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            
            print("First Name: ", firstname, "Last Name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration Status: ", registration_status)
            print("------------------------------------------")
        else:
            tk.messagebox.showwarning(title= "Error", message= "You need to enter your name first!")
    else:
        tk.messagebox.showwarning(title= "Error", message= "You have not accepted the Terms & Conditions!")

# Root window
window = tk.Tk()
window.title("Data Entry From")

frame = tk.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# User Name Labels
first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = ttk.Spinbox(user_info_frame, from_= 18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nation_label= tk.Label(user_info_frame, text="Nationality")
nation_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nation_label.grid(row=2, column=1)
nation_combobox.grid(row=3, column=1)

# Initializing a grid loop for each widget to use a specific padding
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# Saving Course Info
course_frame = tk.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(course_frame, text="Registration Status")

reg_status_var = tk.StringVar(value="Not Registered")
registered_check = tk.Checkbutton(course_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(course_frame, text="# Completed Courses")
numcourses_spinbox = ttk.Spinbox(course_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(course_frame, text="# Completed Semesters")
numsemesters_spinbox = ttk.Spinbox(course_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    

# Accept Terms

terms_frame = tk.LabelFrame(frame, text= "Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var,
                             onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tk.Button(frame, text="Enter Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Run an infinite loop while the application is being executed
window.mainloop()