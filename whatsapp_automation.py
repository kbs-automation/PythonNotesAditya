import pywhatkit as kit
import datetime
import time
import pyautogui

# Specify the target phone number (with the country code) and the message
target_number = '+91 8679266863'  # Replace with the recipient's phone number
message = 'Hello, this is an automated message using python programming language'

# Get the current time
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 2  # Send the message 2 minutes from now

# Open WhatsApp Web and type the message
kit.sendwhatmsg(target_number, message, hours, minutes)
time.sleep(10)  # Wait for the WhatsApp Web to load

# Simulate pressing the Enter key to send the message
pyautogui.press('enter')
