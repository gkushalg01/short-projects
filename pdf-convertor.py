"""
Created - 07-06-2023
Program by Kushal Ghosh.
Licenced Under GNU 2.0 -  free to use.

This program takes use of the following python libraries to make pdf out of books that are not downloadable, 
make sure to install them using 
$  pip install time pyautogui keyboard PIL fpdf

Work Flow - 
After running, It captures a screenshot every time you press 'right-click',
it crops the screenshot as per size and adds to an image stream
Stops capture when you press 'esc' and then converts the image stream into a pdf file.
It was basically used to convert study books that were non-downloadable into PDFs so I could 
use them as normal notes in my iPad.
"""
import time
import keyboard
import os
import pyautogui
from PIL import Image
from fpdf import FPDF

# Define the folder to save the original screenshots
original_folder = "my_folder_name"

# Create the original folder if it doesn't exist
if not os.path.exists(original_folder):
    os.makedirs(original_folder)

# Define the folder to save the cropped screenshots
cropped_folder = original_folder+"final"

# Create the cropped folder if it doesn't exist
if not os.path.exists(cropped_folder):
    os.makedirs(cropped_folder)

# Initialize the screenshot counter
screenshot_counter = 0

# Initialize the coordinates for cropping (in pixels)
left_crop = 1
top_crop = 1
right_crop = 1079  # Adjust this value based on your screen resolution
bottom_crop = 1399  # Adjust this value based on your screen resolution

# Initialize the PDF object
pdf = FPDF(orientation="P", unit="pt")

# Function to take a screenshot, save it, crop it, save the cropped image, and add it to the PDF
def take_screenshot():
    global screenshot_counter
    time.sleep(0.5)  # Wait for 0.5 seconds
    screenshot_name = f"screenshot_{screenshot_counter}.png"
    screenshot_path = os.path.join(original_folder, screenshot_name)
    pyautogui.screenshot(screenshot_path)
    original_image = Image.open(screenshot_path)
    original_image.save(screenshot_path)
    cropped_image = original_image.crop((left_crop, top_crop, right_crop, bottom_crop))
    cropped_image_path = os.path.join(cropped_folder, screenshot_name)
    cropped_image.save(cropped_image_path)
    screenshot_counter += 1
    print(f"Original screenshot saved: {screenshot_path}")
    print(f"Cropped screenshot saved: {cropped_image_path}")

    # Add the cropped screenshot to the PDF
    pdf.add_page()
    pdf.image(cropped_image_path, 0, 0, pdf.w, pdf.h)

# Function to handle the keyboard events
def on_key_press(event):
    if event.name == "right":
        take_screenshot()

# Register the key press event
keyboard.on_press(on_key_press)

# Main loop to listen for keyboard events
keyboard.wait('esc')  # Press 'esc' to exit the program

# Save the PDF
pdf_output = original_folder+".pdf"
pdf.output(pdf_output)
print(f"PDF created: {pdf_output}")
