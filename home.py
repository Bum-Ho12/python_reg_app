import datetime
import tkinter as tk
from tkinter import ttk  # Import ttk for Treeview widget
import sqlite3

class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home")

        # Title 
        title_label = tk.Label(self, text="All Logged In Users")
        title_label.pack(pady=10)

        # Treeview to display users
        self.user_table = ttk.Treeview(self, columns=("username", "email", "login_time"))
        self.user_table.pack()

        self.user_table.heading("#0", text="ID")  # ID column is automatically created
        self.user_table.column("#0", width=50)  

        self.user_table.heading("username", text="Username")
        self.user_table.column("username", width=150)

        self.user_table.heading("email", text="Email")
        self.user_table.column("email", width=200) 

        self.user_table.heading("login_time", text="Login Time")
        self.user_table.column("login_time", width=150) 

        self.populate_table()  # Call when the window is opened

    def populate_table(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, login_time FROM applicants")
        rows = cursor.fetchall()

        for row in rows:
            login_time_str = row[3] 
            if login_time_str:
                # Convert from string (or whatever format it's stored) to a datetime object
                login_time_obj = datetime.datetime.strptime(login_time_str, '%Y-%m-%d %H:%M:%S.%f')  # Adjust format if needed
                formatted_time = login_time_obj.strftime('%d %b %Y, %I:%M %p')  # Nice formatting
            else:
                formatted_time = "Not logged in yet"

            self.user_table.insert("", tk.END, text=row[0], values=(row[1], row[2], formatted_time))  

        conn.close()

if __name__ == "__main__":
    home_window = HomeWindow()
    home_window.mainloop()
