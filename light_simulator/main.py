import tkinter as tk
from calculations import calculate_reflection_refraction

# Function to update results on the interface
def update_result():
    try:
        angle_of_incidence = float(entry_angle_of_incidence.get())
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        result_text = calculate_reflection_refraction(angle_of_incidence, n1, n2)
        result.set(result_text)
    except ValueError:
        result.set("Invalid input. Please enter numeric values.")

# Interface setup
root = tk.Tk()
root.title("Light Reflection and Refraction Simulator")

# Labels and input fields
tk.Label(root, text="Angle of Incidence (degrees):").grid(row=0, column=0)
entry_angle_of_incidence = tk.Entry(root)
entry_angle_of_incidence.grid(row=0, column=1)

tk.Label(root, text="Refractive Index of Medium 1:").grid(row=1, column=0)
entry_n1 = tk.Entry(root)
entry_n1.grid(row=1, column=1)

tk.Label(root, text="Refractive Index of Medium 2:").grid(row=2, column=0)
entry_n2 = tk.Entry(root)
entry_n2.grid(row=2, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=update_result)
calculate_button.grid(row=3, column=0, columnspan=2)

# Result display
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=0, columnspan=2)

# Start the GUI loop
root.mainloop()
