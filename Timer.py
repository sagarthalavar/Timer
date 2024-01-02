import tkinter as tk

def update_timer(seconds):
    label['text'] = f"Time left: {seconds} seconds"

def start_countdown():
    try:
        seconds = int(entry.get())
        countdown(seconds)
    except ValueError:
        label['text'] = "Please enter a valid number for seconds!"

def countdown(seconds):
    if seconds >= 0:
        update_timer(seconds)
        root.after(1000, countdown, seconds - 1)
    else:
        label['text'] = "Time's up!"

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("500x250")

# Create label for timer display
label = tk.Label(root, text="", font=('Arial', 18))
label.pack(pady=20)

# Create entry for user input
entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)

# Create start button
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
