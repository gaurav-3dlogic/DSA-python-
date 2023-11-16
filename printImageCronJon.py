import os
import random
import subprocess
from datetime import datetime
import pytz
import schedule
import time
from PIL import Image

# Directory containing the images
image_dir = r"C:\Users\cyno_\OneDrive\Desktop\quotes"

# List all files in the directory
image_files = os.listdir(image_dir)

def print_random_image():
    # Choose a random image from the list
    random_image = random.choice(image_files)

    # Full path to the selected image
    image_path = os.path.join(image_dir, random_image)

    # Open the image and resize it to A4 size (8.27x11.69 inches)
    a4_width = 8.27 * 300  # 1 inch = 300 pixels
    a4_height = 11.69 * 300
    image = Image.open(image_path)
    image = image.resize((int(a4_width), int(a4_height)))

    # Save the resized image to a temporary file
    temp_image_path = os.path.join(image_dir, "temp_image.png")
    image.save(temp_image_path)

    # Printer name
    printer_name = "EPSON47AA44 (L15150 Series)"

    # Check if the printer is valid in Windows environment
    printer_found = False
    printers = subprocess.run(["wmic", "printer", "get", "name"], capture_output=True, text=True)
    if printer_name in printers.stdout:
        printer_found = True

    # Convert image path to double backslashes for Windows paths
    temp_image_path = temp_image_path.replace("\\", "\\\\")

    if printer_found:
        # Print the A4 size image
        subprocess.run(["mspaint.exe", "/pt", temp_image_path, printer_name], check=True)
    else:
        print(f"Invalid printer name: {printer_name}")

    # Delete the temporary image file
    os.remove(temp_image_path)

    # Log the execution time
    current_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Script executed at {current_time}, Printed image: {random_image}"
    with open("script_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

# Schedule the function to run daily at 18:02 IST
schedule.every().day.at("16:50").do(print_random_image)

while True:
    schedule.run_pending()
    time.sleep(1)
