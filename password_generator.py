import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())  # Get password length from entry field
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)  # Update result label with generated password

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Label for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

# Entry field for password length
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Label to display generated password
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

