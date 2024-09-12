
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import plot_handler as ph

map_type = None
#Git-specifick-change: here

# Function to plot graph
def update_plot():

    #set R-value
    ph.r = float(entry.get())

    #Type of map
    map_type = text_var.get()
    # Generate random data for demonstration
    if map_type == "Logistic map" or map_type == "Tent map":
        x, y = ph.get_x_y(map_type)
    else:
        x = np.linspace(0, 10, 100)
        y = np.sin(x) + np.random.random(100) * 0.5  # Sine wave with noise

    # Clear the current figures
    ax1.clear()
    ax2.clear()
    
    # Plot on the first subplot
    ax1.plot(x, y, label="Return map")
    ax1.plot(x, x, label="y=x")
    ax1.set_title(map_type)
    ax1.set_xlabel("x(j)")
    ax1.set_ylabel("x(j+1)")
    ax1.legend(loc='upper right')

    if map_type == "Logistic map":
        x, y = ph.logistic_map(200)
    else:
        y = np.sin(x)
    ax2.plot(x, y, label=map_type)  # Example plot for second subplot
    ax2.set_title("After some timesteps")
    ax2.set_xlabel("j")
    ax2.set_ylabel("x(j)")

    '''
    # Plot on the second subplot (for demonstration purposes)
    ax2.plot(x, np.cos(x), label="Cosine wave")  # Example plot for second subplot
    ax2.set_title("Second Plot")
    ax2.set_xlabel("x")
    ax2.set_ylabel("cos(x)")
    ax2.legend(loc='upper right')
    '''
    
    # Redraw the canvas
    canvas.draw()

# Function to handle window close event
# Function to handle window close event
def on_closing():
    # Quit tkinter main loop and destroy the window
    root.quit()
    root.destroy()

# Create the main tkinter window
root = tk.Tk()
root.title("Tkinter with Matplotlib")

# Create a frame for the plot and button
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

#fig, ax = plt.subplots(figsize=(5, 4))
# Create a matplotlib figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

# Create a Tkinter variable to hold the selected text
text_var = tk.StringVar(value="Logistic map")

# Create a canvas to embed the plot
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a button to update the plot
button = ttk.Button(frame, text="Show Plot", command=update_plot)
button.pack(side=tk.BOTTOM)

# Create and pack the radio buttons
radio_button_a = ttk.Radiobutton(root, text="Logistic map", value="Logistic map", variable=text_var)
#radio_button_a.pack(anchor=tk.W)
radio_button_a.pack(anchor=tk.W, padx=10, pady=10, side=tk.LEFT)

radio_button_b = ttk.Radiobutton(root, text="Tent map", value="Tent map", variable=text_var)
#radio_button_b.pack(anchor=tk.W)
radio_button_b.pack(anchor=tk.W, padx=10, pady=10, side=tk.LEFT)

# Create a label
label = tk.Label(root, text="R:")
#label.pack(padx=10, pady=10)
label.pack(side=tk.LEFT, padx=10, pady=10)

# Create a StringVar with default value
default_value = tk.StringVar(value="2")

entry = tk.Entry(root, width=5, textvariable=default_value)
#entry.pack(padx=10, pady=10)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create and pack the activation button
#activation_button = ttk.Button(root, text="Print Selected Text", command=print_selected_text)
#activation_button.pack(pady=10)
#button = ttk.Button(frame, text="set", command=update_plot)
#button.pack(side=tk.BOTTOM)

# Initialize the plot
update_plot()

# Bind the window close button to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the tkinter main loop
root.mainloop()