import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import qrcode
import os
from fpdf import FPDF
import platform
import subprocess

photo_path = ""
template_style = "Classic"

root = tk.Tk()
root.title("ID Card Generator")
root.geometry("520x700")
root.configure(bg="#2c2f33")

# Inputs
tk.Label(root, text="Name", bg="#2c2f33", fg="white").pack()
name_entry = tk.Entry(root, font=('Arial', 14))
name_entry.pack()

tk.Label(root, text="ID Number", bg="#2c2f33", fg="white").pack()
id_entry = tk.Entry(root, font=('Arial', 14))
id_entry.pack()

tk.Label(root, text="Department", bg="#2c2f33", fg="white").pack()
dept_entry = tk.Entry(root, font=('Arial', 14))
dept_entry.pack()

tk.Label(root, text="Role", bg="#2c2f33", fg="white").pack()
role_entry = tk.Entry(root, font=('Arial', 14))
role_entry.pack()

# Template selector
tk.Label(root, text="Select Template", bg="#2c2f33", fg="white").pack(pady=5)
template_var = tk.StringVar(value="Classic")
template_menu = tk.OptionMenu(root, template_var, "Classic", "Modern", "Minimal")
template_menu.pack()

# Photo
def upload_photo():
    global photo_path
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if path:
        photo_path = path
        messagebox.showinfo("Photo Selected", "Photo successfully uploaded!")

tk.Button(root, text="Upload Photo", command=upload_photo, bg="#7289da", fg="white", font=("Arial", 12)).pack(pady=10)

# Preview canvas
canvas = tk.Canvas(root, width=320, height=200, bg='white')
canvas.pack(pady=10)

# QR code generator
def generate_qr(data):
    qr = qrcode.make(data)
    return qr.resize((60, 60))

# Save as PDF
def save_as_pdf(img_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_path, x=30, y=50, w=150)
    pdf.output(pdf_path)

# Print image
def print_card(path):
    if platform.system() == "Windows":
        os.startfile(path, "print")
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", "-a", "Preview", path])
    else:  # Linux
        subprocess.run(["lp", path])

# Generate ID card
def generate_id():
    if not all([name_entry.get(), id_entry.get(), dept_entry.get(), role_entry.get(), photo_path]):
        messagebox.showwarning("Missing Info", "Fill all fields and upload a photo.")
        return

    # Basic setup
    card = Image.new("RGB", (320, 200), "white")
    draw = ImageDraw.Draw(card)
    font_title = ImageFont.truetype("arial.ttf", 16)
    font_text = ImageFont.truetype("arial.ttf", 12)

    # Template color & layout
    style = template_var.get()
    if style == "Classic":
        draw.rectangle([0, 0, 320, 40], fill="#003366")
    elif style == "Modern":
        draw.rectangle([0, 0, 320, 30], fill="#444")
        draw.rectangle([0, 170, 320, 200], fill="#888")
    elif style == "Minimal":
        draw.rectangle([0, 0, 320, 200], fill="#f0f0f0")

    # Photo
    user_img = Image.open(photo_path).resize((70, 90))
    card.paste(user_img, (15, 50))

    # Text
    draw.text((100, 45), f"Name: {name_entry.get()}", font=font_text, fill="black")
    draw.text((100, 70), f"ID: {id_entry.get()}", font=font_text, fill="black")
    draw.text((100, 95), f"Dept: {dept_entry.get()}", font=font_text, fill="black")
    draw.text((100, 120), f"Role: {role_entry.get()}", font=font_text, fill="black")

    # QR Code
    qr_data = f"{name_entry.get()} | {id_entry.get()}"
    qr = generate_qr(qr_data)
    card.paste(qr, (240, 125))

    # Save
    img_path = f"{id_entry.get()}_ID.png"
    pdf_path = f"{id_entry.get()}_ID.pdf"
    card.save(img_path)
    save_as_pdf(img_path, pdf_path)

    # Preview
    preview = ImageTk.PhotoImage(card.resize((320, 200)))
    canvas.image = preview
    canvas.create_image(0, 0, anchor="nw", image=preview)

    messagebox.showinfo("Success", f"Saved as:\n{img_path}\n{pdf_path}")

    # Ask to print
    if messagebox.askyesno("Print?", "Do you want to print the ID card?"):
        print_card(img_path)

tk.Button(root, text="Generate ID Card", command=generate_id,
          bg="#43b581", fg="white", font=("Arial", 14)).pack(pady=15)

root.mainloop()
