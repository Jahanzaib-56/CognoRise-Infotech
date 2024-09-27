import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        # Get the input time from the entry field
        countdown_time = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of seconds")
        return
    
    # Disable the Start button and Entry field during countdown
    start_button.config(state="disabled")
    entry.config(state="disabled")

    # Countdown loop
    while countdown_time >= 0:
        mins, secs = divmod(countdown_time, 60)  # Convert seconds to minutes and seconds
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer_format)  # Update the label with the remaining time
        root.update()
        time.sleep(1)
        countdown_time -= 1

    # Show message when countdown is complete
    messagebox.showinfo("Time's up!", "The countdown has finished!")
    
    # Re-enable the Start button and Entry field after countdown ends
    start_button.config(state="normal")
    entry.config(state="normal")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")  # Set window size
root.config(bg="#D3D3D3")  # Set background color

# Entry widget to input countdown time in seconds
entry = tk.Entry(root, font=("Helvetica", 24), width=5, justify="center", fg="#FFFFFF", bg="#000000", bd=5)
entry.grid(row=0, column=0, padx=10, pady=10)

# Start button to begin the countdown
start_button = tk.Button(root, text="Start", font=("Helvetica", 24), command=start_countdown, bg="#FFFF00", fg="#FF0000", activebackground="#D3D3D3", bd=5)
start_button.grid(row=0, column=1, padx=10, pady=10)

# Label to display the countdown time
label = tk.Label(root, font=("Helvetica", 48), text="00:00", fg="#FFA500", bg="#D3D3D3", pady=20)
label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Footer message
footer_label = tk.Label(root, text="Time in Seconds", font=("Helvetica", 12), fg="#000000", bg="#D3D3D3")
footer_label.grid(row=2, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
