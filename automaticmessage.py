import pywhatkit as kit
import datetime
import time
import pyautogui

# Specify the target group name
target_group = 'BCA(AMITY ONLINE SPECIAL [VIP] GROUP)🖥️💫'  # Replace with the name of your group
message = 'Hello, this is an automated message using python now your turn to make this things .'

# Get the current time
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 2  # Send the message 2 minutes from now

# Open WhatsApp Web and type the message
kit.sendwhatmsg_to_group(target_group, message, hours, minutes)
time.sleep(10)  # Wait for the WhatsApp Web to load

# Simulate pressing the Enter key to send the message
pyautogui.press('enter')
