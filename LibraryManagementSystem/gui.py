# gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from library import Library
from book import Book
from PIL import Image, ImageTk

# Create the main Library object (with data persistence)
library = Library()

# Function to add a book
def add_book():
    title = simpledialog.askstring("Input", "Enter book title:")
    author = simpledialog.askstring("Input", "Enter book author:")
    if title and author:
        new_book = Book(title, author)
        library.add_book(new_book)
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please provide both title and author.")

# Function to borrow a book
def borrow_book():
    user = simpledialog.askstring("Input", "Enter your name:")
    title = simpledialog.askstring("Input", "Enter book title to borrow:")
    if user and title:
        library.borrow_book(user, title)
        messagebox.showinfo("Success", f"Book '{title}' borrowed by {user}.")
    else:
        messagebox.showwarning("Input Error", "Please provide both name and title.")

# Function to return a book
def return_book():
    user = simpledialog.askstring("Input", "Enter your name:")
    if user:
        library.return_book(user)
        messagebox.showinfo("Success", f"Book returned by {user}.")
    else:
        messagebox.showwarning("Input Error", "Please provide your name.")

# Function to view all books
def view_books():
    books_list = library.books
    if books_list:
        books_info = "\n".join(str(book) for book in books_list)
        messagebox.showinfo("Available Books", books_info)
    else:
        messagebox.showinfo("Available Books", "No books available.")

# Function to view borrowed books
def view_borrowed_books():
    borrowed_list = library.borrowed_books
    if borrowed_list:
        borrowed_info = "\n".join(f"{user}: {book}" for user, book in borrowed_list.items())
        messagebox.showinfo("Borrowed Books", borrowed_info)
    else:
        messagebox.showinfo("Borrowed Books", "No books have been borrowed.")

# Initialize the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x300")
root.resizable(False, False)

# Load icons
try:
    add_icon = ImageTk.PhotoImage(Image.open("icons/add_icon.png").resize((25, 25)))
    borrow_icon = ImageTk.PhotoImage(Image.open("icons/borrow_icon.png").resize((25, 25)))
    return_icon = ImageTk.PhotoImage(Image.open("icons/return_icon.png").resize((25, 25)))
    view_books_icon = ImageTk.PhotoImage(Image.open("icons/view_books_icon.png").resize((25, 25)))
    view_borrowed_icon = ImageTk.PhotoImage(Image.open("icons/view_borrowed_icon.png").resize((25, 25)))
except Exception as e:
    messagebox.showerror("Error", f"Could not load icons: {e}")

# Create buttons for various actions
btn_add = tk.Button(root, text="Add Book", image=add_icon, compound=tk.LEFT, command=add_book)
btn_add.pack(pady=10)

btn_borrow = tk.Button(root, text="Borrow Book", image=borrow_icon, compound=tk.LEFT, command=borrow_book)
btn_borrow.pack(pady=10)

btn_return = tk.Button(root, text="Return Book", image=return_icon, compound=tk.LEFT, command=return_book)
btn_return.pack(pady=10)

btn_view_books = tk.Button(root, text="View Books", image=view_books_icon, compound=tk.LEFT, command=view_books)
btn_view_books.pack(pady=10)

btn_view_borrowed = tk.Button(root, text="View Borrowed Books", image=view_borrowed_icon, compound=tk.LEFT, command=view_borrowed_books)
btn_view_borrowed.pack(pady=10)

# Start the main event loop
root.mainloop()
