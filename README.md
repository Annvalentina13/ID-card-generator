# ID Card Generator Application

## Overview

This Python application allows users to create customized employee ID cards with the following features:

- Input fields for Name, ID Number, Department, and Role.
- Upload a user photo to be included on the ID card.
- Select from multiple ID card design templates (Classic, Modern, Minimal).
- Generate a QR code containing user details on the card.
- Preview the generated ID card within the app.
- Save the ID card as a PNG image and export as a PDF.
- Optionally print the ID card directly from the application.

---

## Features

- **User-friendly GUI** using Tkinter.
- **Image processing** with Pillow (PIL) to create and customize ID cards.
- **QR code generation** using the `qrcode` library.
- **PDF generation** using `fpdf`.
- **Print support** for Windows, macOS, and Linux.
- Multiple design templates for card styles.

---

## Requirements

- Python 3.x
- Packages (install via pip):
  - `pillow`
  - `qrcode`
  - `fpdf`

## Usage Instructions
- Run the Python script id_card_generator.py.
- Enter the employee details in the respective fields:
- Name
- ID Number
- Department
- Role
- Upload a photo of the employee.
- Select a design template from the dropdown menu.
- Click Generate ID Card to create and preview the card.
- The card is saved automatically as <ID_Number>_ID.png and <ID_Number>_ID.pdf.
- You will be prompted to print the card — choose yes/no.
- The generated card image and PDF will be saved in the script's directory.
- File Structure
- id_card_generator.py — Main application script.
- Generated files:
- <ID_Number>_ID.png — PNG image of the generated ID card.
- <ID_Number>_ID.pdf — PDF file containing the ID card.
