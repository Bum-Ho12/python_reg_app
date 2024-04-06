'''
file: main.py
function: Main file to run the application
'''
import tkinter as tk
from registration import RegistrationForm
from login import LoginForm
from home import HomeWindow

class ApplicantApp(tk.Tk):
    """
    Class: ApplicantApp
    Function: Main application class for login and registration functionalities
    """
    success = False
    def __init__(self):
        """
        Initialize the main window and buttons for login and registration.
        """
        super().__init__()  # Call the parent class (tk.Tk) constructor
        self.title("Applicant App")
        self.geometry("400x200")

        # Login button
        login_button = tk.Button(self,text="Login", command=self.handle_login_click)
        login_button.pack(pady=10, side='top', anchor='center')

        # Registration button
        register_button = tk.Button(self,text="Register", command=self.handle_register_click)
        register_button.pack(pady=10, side='top', anchor='center')

        # Generate Report button
        generate_button = tk.Button(self,text="Generate Report", command=self.handle_report_click)
        generate_button.pack(pady=10)

        # Message label (optional)
        self.message_label = tk.Label(self, text="")
        self.message_label.pack(pady=10)
        # Function to handle login button click
    def handle_report_click(self):
        """
        Function: Create a login form instance within a new window
        """
        if self.success:
            home_window = HomeWindow()
            home_window.mainloop()
        else:
            self.message_label.config(text="Please login or register first!")

    # Function to handle login button click
    def handle_login_click(self):
        """
        Function: Create a login form instance within a new window
        """
        login_window = tk.Toplevel(self)
        login_window.title("Login")
        login_form = LoginForm(login_window)
        login_window.wait_window()

        # If login is successful, open home.py
        if login_form.success:
            self.success = True
            self.message_label.config(text="Login successful!")
            # self.withdraw()  # Hide the main window
            home_window = HomeWindow()
            home_window.mainloop()

    # Function to handle registration button click
    def handle_register_click(self):
        """
        Function: Create a registration form instance within a new window
        """
        register_window = tk.Toplevel(self)  # Use self for parent window
        register_window.title("Registration")
        registration_form = RegistrationForm(register_window)
        register_window.wait_window()
        if registration_form.success:
            self.success = True
            self.message_label.config(text="Registration successful!")
        return registration_form

# Run the main loop
if __name__ == "__main__":
    app = ApplicantApp()
    app.mainloop()
