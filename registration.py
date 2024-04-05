'''
file name: registration.py
function: GUI for registration form
'''

import tkinter as tk
import sqlite3

class RegistrationForm:
    """
    Class: RegistrationForm
    Function: GUI for registration form
    """
    success = False
    def __init__(self,root):
        """
        Initialize the registration form elements within the provided root window.
        """
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("400x300")

        # Username label and entry field
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=2)

        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Email label and entry field
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack(pady=2)

        self.email_entry = tk.Entry(root)
        self.email_entry.pack(pady=5)

        # Password label and entry field
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=2)

        self.password_entry = tk.Entry(root, show="*")  # Use asterisk for hidden password
        self.password_entry.pack(pady=5)

        # Register button
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack(pady=10)

        # Message label (optional)
        self.message_label = tk.Label(root, text="")
        self.message_label.pack()
        if self.success:
            self.root.destroy()

    def register(self):
        """
        Method: register
        Function: Display a success message when the user clicks the Register button
        """
        # Get user input from entry fields
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Connect to the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # Create table 'applicants' if it doesn't exist
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )'''
        )

        try:
            # Insert data into the applicants table
            cursor.execute(
                "INSERT INTO applicants (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            conn.commit()  # Save changes to the database
            self.message_label.config(text="Registration successful!")
            self.success = True
            self.root.destroy()
        except sqlite3.Error as err:
            # Handle database errors (e.g., duplicate username or email)
            self.message_label.config(text="Error: " + str(err))
            print(
                f"Error: {err}"
            )
            self.success = False

        finally:
            # Close the connection
            conn.close()
        return None
