import pyautogui

# Function to continuously print the cursor position
def print_cursor_position():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Cursor position: X={x}, Y={y}")
    except KeyboardInterrupt:
        print("Program terminated by user.")

# Start printing the cursor position
print_cursor_position()
