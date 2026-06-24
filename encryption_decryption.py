
import tkinter as tk
from tkinter import ttk, messagebox

# Caesar Cipher Encryption
def encrypt():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text!")
        return

    shift = 3
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Caesar Cipher Decryption
def decrypt():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text!")
        return

    shift = 3
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Clear Function
def clear_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("Encryption & Decryption System")
root.geometry("700x500")
root.resizable(False, False)

# Background
root.configure(bg="#0f172a")

# Heading
title = tk.Label(
    root,
    text="🔐 Encryption & Decryption System",
    font=("Segoe UI", 20, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=15)

# Frame
frame = tk.Frame(root, bg="#1e293b", bd=2)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Input Label
input_label = tk.Label(
    frame,
    text="Enter Text",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="white"
)
input_label.pack(pady=(15,5))

# Input Box
input_text = tk.Text(
    frame,
    height=6,
    width=70,
    font=("Consolas", 11)
)
input_text.pack()

# Buttons
button_frame = tk.Frame(frame, bg="#1e293b")
button_frame.pack(pady=15)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    font=("Segoe UI", 11, "bold"),
    bg="#22c55e",
    fg="white",
    width=15,
    command=encrypt
)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    font=("Segoe UI", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    width=15,
    command=decrypt
)
decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    font=("Segoe UI", 11, "bold"),
    bg="#ef4444",
    fg="white",
    width=15,
    command=clear_fields
)
clear_btn.grid(row=0, column=2, padx=10)

# Output Label
output_label = tk.Label(
    frame,
    text="Output",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="white"
)
output_label.pack(pady=(10,5))

# Output Box
output_text = tk.Text(
    frame,
    height=6,
    width=70,
    font=("Consolas", 11)
)
output_text.pack()

# Footer

footer = tk.Label(
    root,
    text="Cyber Security Internship Project | DecodeLabs",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="lightgray"
)
footer.pack(pady=10)

root.mainloop()


