import tkinter as tk
from tkinter import messagebox
from calculations import calculate_reflection_refraction
import math

class LightSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Reflection and Refraction Simulator")

        # Angle of incidence input
        tk.Label(root, text="Angle of Incidence (degrees):").grid(row=0, column=0)
        self.angle_entry = tk.Entry(root)
        self.angle_entry.grid(row=0, column=1)

        # Refractive index of medium 1
        tk.Label(root, text="Refractive Index of Medium 1:").grid(row=1, column=0)
        self.n1_entry = tk.Entry(root)
        self.n1_entry.grid(row=1, column=1)

        # Refractive index of medium 2
        tk.Label(root, text="Refractive Index of Medium 2:").grid(row=2, column=0)
        self.n2_entry = tk.Entry(root)
        self.n2_entry.grid(row=2, column=1)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=2)

        # Result display
        self.result_label = tk.Label(root, text="", wraplength=300)
        self.result_label.grid(row=4, columnspan=2)

        # Canvas for graphical representation
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.grid(row=5, columnspan=2)
        self.draw_interface()

        # Color legend
        tk.Label(root, text="Legend:", font=("Arial", 10, "bold")).grid(row=6, columnspan=2)
        tk.Label(root, text="Red: Incident Ray", fg="red").grid(row=7, column=0, sticky="w")
        tk.Label(root, text="Green: Reflected Ray", fg="green").grid(row=8, column=0, sticky="w")
        tk.Label(root, text="Purple: Refracted Ray", fg="purple").grid(row=9, column=0, sticky="w")

    def draw_interface(self):
        # Draws the interface for the incident, reflected, and refracted rays
        #self.canvas.create_line(225, 0, 225, 300, fill="gray", dash=(4, 4))  # Normal line
        self.canvas.create_line(0, 150, 450, 150, fill="#3498db", width=2)  # Boundary line between media

    def calculate(self):
        try:
            # Get user inputs
            angle_of_incidence = float(self.angle_entry.get())
            n1 = float(self.n1_entry.get())
            n2 = float(self.n2_entry.get())

            # Perform calculations
            results = calculate_reflection_refraction(angle_of_incidence, n1, n2)
            self.result_label.config(text=results)

            # Calculate reflection and refraction angles for graphical representation
            angle_of_reflection = angle_of_incidence
            angle_of_refraction = None if "Total internal reflection" in results else float(results.split("\n")[1].split(": ")[1].split(" ")[0])

            # Draw rays on the canvas
            self.draw_rays(angle_of_incidence, angle_of_reflection, angle_of_refraction)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    def draw_rays(self, angle_of_incidence, angle_of_reflection, angle_of_refraction):
        # Clear previous rays
        self.canvas.delete("ray")

        # Calculate coordinates for incident ray
        x_start, y_start = 200, 150
        x_incident = x_start - 100 * math.cos(math.radians(angle_of_incidence))
        y_incident = y_start - 100 * math.sin(math.radians(angle_of_incidence))

        # Draw incident ray
        self.canvas.create_line(x_start, y_start, x_incident, y_incident, fill="red", width=2, tags="ray")

        # Calculate and draw reflected ray
        x_reflected = x_start + 100 * math.cos(math.radians(angle_of_reflection))
        y_reflected = y_start - 100 * math.sin(math.radians(angle_of_reflection))
        self.canvas.create_line(x_start, y_start, x_reflected, y_reflected, fill="green", width=2, tags="ray")

        if angle_of_refraction is not None:
            # Calculate and draw refracted ray
            x_refracted = x_start + 100 * math.cos(math.radians(angle_of_refraction))
            y_refracted = y_start + 100 * math.sin(math.radians(angle_of_refraction))
            self.canvas.create_line(x_start, y_start, x_refracted, y_refracted, fill="purple", width=2, tags="ray")

if __name__ == "__main__":
    root = tk.Tk()
    app = LightSimulatorApp(root)
    root.mainloop()
