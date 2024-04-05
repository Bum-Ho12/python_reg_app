'''
file: main.py
function: Main file to run the application
'''
import tkinter as tk
import sqlite3
from registration import RegistrationForm
from login import LoginForm

class ApplicantApp(tk.Tk):
    """
    Class: ApplicantApp
    Function: Main application class for login and registration functionalities
    """
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
        generate_button = tk.Button(self,text="Generate Report", command=self.generate_report)
        generate_button.pack(pady=10)

        # Message label (optional)
        self.message_label = tk.Label(self, text="")
        self.message_label.pack(pady=10)

    def generate_report(self):
        '''
        method: generate_report
        function: Generate a report based on the data in the database
        '''
        # Connect to the database (if needed)
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Fetch data for the report (replace with your specific logic)
        cursor.execute("SELECT * FROM applicants")  # Example query
        applicants = cursor.fetchall()

        # Generate report content (text, HTML, etc.) based on fetched data
        report_content = self.format_report_data(applicants)  # Placeholder for formatting

        # Display the report (different methods based on your choice)
        self.display_report(report_content)
        self.message_label.config(text="Report Generated!")

        # Close the connection
        conn.close()

    # Placeholder function for formatting report data (replace with your logic)
    def format_report_data(self, applicants):
        '''
        method: format_report_data
        function: Format the report data in a specific way
        '''
        report_text = "Applicant Report:\n"
        for applicant in applicants:
            report_text += f"-> Username: {applicant[1]},\n Email: {applicant[2]}\n Attendee 🚩\n\n"
        return report_text

    # Placeholder function for displaying the report (replace with your choice)
    def display_report(self, report_content):
        '''
        method: display_report
        function: Display the report in a message box or a new text widget
        '''
        # # Option 1: Display in a message box
        # tk.messagebox.showinfo(title="Report", message=report_content)

        # Option 2: Display in a new text widget within the main window (example)
        report_window = tk.Toplevel(self)
        report_window.title("Report")
        report_text_widget = tk.Text(report_window)
        report_text_widget.insert(tk.END, report_content)
        report_text_widget.pack()


    # Function to handle login button click
    def handle_login_click(self):
        """
        Function: Create a login form instance within a new window
        """
        login_window = tk.Toplevel(self)  # Use self for parent window
        login_window.title("Login")
        login_form = LoginForm(login_window)
        login_window.wait_window()
        if login_form.success:
            self.message_label.config(text="Login successful!")
        return login_form

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
            self.message_label.config(text="Registration successful!")
        return registration_form

# Run the main loop
if __name__ == "__main__":
    app = ApplicantApp()
    app.mainloop()
