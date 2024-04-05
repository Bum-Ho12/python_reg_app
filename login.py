'''
file name: login.py
function: GUI for login form
'''

import tkinter as tk
import sqlite3

class LoginForm:
    """
    Class: RegistrationForm
    Function: GUI for registration form
    """
    success = False
    def __init__(self,root):
        """
        Initialize the login form elements within the provided root window.
        """
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("400x200")

        # Email label and entry field
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        # Password label and entry field
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")  # Use asterisk for hidden password
        self.password_entry.pack()

        # Register button
        self.register_button = tk.Button(root, text="Login", command=self.login)
        self.register_button.pack()

        # Message label (optional)
        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

    def login(self):
        """
        Method: login
        Function: Display a success message when the user clicks the Register button
        """
        # Get user input from entry fields
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Perform validation or data processing here (optional)
        # ...
        # Connect to the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        try:
            # Fetch user data based on username
            cursor.execute("SELECT * FROM applicants WHERE email = ?", (email,))
            user = cursor.fetchone()  # Get the first row (if any)

            # Validate login credentials (assuming password is stored in the database)
            if user and user[3] == password:  # Check email and password
                self.message_label.config(text="Login successful!")
                self.success = True
                self.root.destroy()
            else:
                self.message_label.config(text="Invalid email or password.")
                self.success = False

        except sqlite3.Error as err:
            # Handle database errors
            self.message_label.config(text="Error: " + str(err))
            self.success = False

        finally:
            # Close the connection
            conn.close()
        return None
