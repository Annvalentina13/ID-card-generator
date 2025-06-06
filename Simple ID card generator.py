import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

# Global vars
photo_path = ""

# Load default font
default_font = ImageFont.load_default()

# App window
root = tk.Tk()
root.title("ID Card Generator")
root.geometry("500x600")
root.configure(bg="#2c2f33")

# Input Labels and Fields
tk.Label(root, text="Name", bg="#2c2f33", fg="white").pack(pady=5)
name_entry = tk.Entry(root, font=('Arial', 14))
name_entry.pack()

tk.Label(root, text="ID Number", bg="#2c2f33", fg="white").pack(pady=5)
id_entry = tk.Entry(root, font=('Arial', 14))
id_entry.pack()

tk.Label(root, text="Department", bg="#2c2f33", fg="white").pack(pady=5)
dept_entry = tk.Entry(root, font=('Arial', 14))
dept_entry.pack()

tk.Label(root, text="Role", bg="#2c2f33", fg="white").pack(pady=5)
role_entry = tk.Entry(root, font=('Arial', 14))
role_entry.pack()

# Photo upload
def upload_photo():
    global photo_path
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if path:
        photo_path = path
        messagebox.showinfo("Photo Selected", "Photo successfully uploaded!")

tk.Button(root, text="Upload Photo", command=upload_photo, bg="#7289da", fg="white", font=("Arial", 12)).pack(pady=10)

# Preview Canvas
canvas = tk.Canvas(root, width=300, height=180, bg='white')
canvas.pack(pady=10)

# Generate ID Card Function
def generate_id():
    if not all([name_entry.get(), id_entry.get(), dept_entry.get(), role_entry.get(), photo_path]):
        messagebox.showwarning("Missing Info", "Please fill all fields and upload a photo.")
        return

    # Create ID card
    card = Image.new("RGB", (300, 180), "white")
    draw = ImageDraw.Draw(card)

    # Photo
    img = Image.open(photo_path).resize((80, 100))
    card.paste(img, (10, 40))

    # Text
    font_title = ImageFont.truetype("arial.ttf", 16)
    font_content = ImageFont.truetype("arial.ttf", 12)

    draw.text((100, 20), "EMPLOYEE ID CARD", font=font_title, fill="black")
    draw.text((100, 50), f"Name: {name_entry.get()}", font=font_content, fill="black")
    draw.text((100, 75), f"ID: {id_entry.get()}", font=font_content, fill="black")
    draw.text((100, 100), f"Dept: {dept_entry.get()}", font=font_content, fill="black")
    draw.text((100, 125), f"Role: {role_entry.get()}", font=font_content, fill="black")

    # Preview
    card.thumbnail((300, 180))
    preview = ImageTk.PhotoImage(card)
    canvas.image = preview
    canvas.create_image(0, 0, anchor="nw", image=preview)

    # Save
    card.save("ID_Card_Output.png")
    messagebox.showinfo("Saved", "ID Card saved as ID_Card_Output.png")

tk.Button(root, text="Generate ID Card", command=generate_id, bg="#43b581", fg="white", font=("Arial", 14)).pack(pady=20)

root.mainloop()
