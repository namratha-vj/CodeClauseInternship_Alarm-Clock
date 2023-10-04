import threading
import tkinter as tk
from datetime import datetime
import time
import pygame

# Initialize Pygame mixer
pygame.mixer.init()


def play_alarm_sound():
    # Load and play the alarm sound
    pygame.mixer.music.load("alarm_sound.mp3")  # Add your alarm sound here
    pygame.mixer.music.play()


def check_alarm():
    while True:
        # Check if the current time matches the alarm time set by the user
        if alarm_time.get() == datetime.now().strftime("%H:%M"):
            play_alarm_sound()
            break
        time.sleep(1)


def set_alarm():
    # Get the alarm time entered by the user
    alarm_time_value = alarm_time.get()

    # Print a message indicating that the alarm is set for the specified time
    print(f"Alarm set for {alarm_time_value}")

    # Create and start a separate thread for checking the alarm time
    alarm_thread = threading.Thread(target=check_alarm)
    alarm_thread.daemon = True
    alarm_thread.start()


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and place widgets
tk.Label(root, text="Set Alarm (HH:MM)").pack(pady=10)
alarm_time = tk.Entry(root, font=("Arial", 14), justify="center")
alarm_time.pack(padx=20, pady=10)

set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=10)

# Run the application
root.mainloop()
