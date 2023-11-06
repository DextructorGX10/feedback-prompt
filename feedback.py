import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time

def save_feedback_count(count):
    with open("feedback_count.txt", "w") as file:
        file.write(str(count))

def load_feedback_count():
    try:
        with open("feedback_count.txt", "r") as file:
            count_str = file.read().strip()
            if count_str:
                return int(count_str)
            else:
                return 0
    except FileNotFoundError:
        return 0

def thumbs_up():
    global feedback_count
    feedback_count += 1
    save_feedback_count(feedback_count)
    feedback_label.config(text="Thanks for the thumbs up!")
    print(f"Feedback received: {feedback_count}")

def thumbs_down():
    global feedback_count
    feedback_count += 1
    save_feedback_count(feedback_count)
    feedback_label.config(text="We appreciate your feedback and will work on improving.")
    print(f"Feedback received: {feedback_count}")

def main():
    global feedback_count, feedback_label # Needs to be defined in order for thumbs up/down to access it

    feedback_count = load_feedback_count()

    # Create the main window
    root = tk.Tk()
    root.title("Feedback")

    # Open and convert thumbs up image
    thumbs_up_image = Image.open("thumbs_up.png")  # Replace with your image path
    thumbs_up_image = thumbs_up_image.resize((100, 100))  # Adjust the size as needed
    thumbs_up_photo = ImageTk.PhotoImage(thumbs_up_image)

    # Open and convert thumbs down image
    thumbs_down_image = Image.open("thumbs_down.png")  # Replace with your image path
    thumbs_down_image = thumbs_down_image.resize((100, 100))  # Adjust the size as needed
    thumbs_down_photo = ImageTk.PhotoImage(thumbs_down_image)

    # Create labels for the images
    thumbs_up_label = tk.Label(root, image=thumbs_up_photo, cursor="hand2")
    thumbs_up_label.bind("<Button-1>", lambda e: thumbs_up())
    thumbs_down_label = tk.Label(root, image=thumbs_down_photo, cursor="hand2")
    thumbs_down_label.bind("<Button-1>", lambda e: thumbs_down())

    # Create a label for feedback message
    feedback_label = tk.Label(root, text="Please provide feedback")

    # Pack the labels
    thumbs_up_label.pack(side="left")
    thumbs_down_label.pack(side="right")
    feedback_label.pack()

    # Start the GUI main loop
    root.mainloop()

if __name__ == "__main__":
    time.sleep(5)  # Add a delay if necessary
    main()
