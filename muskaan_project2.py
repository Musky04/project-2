import tkinter as tk
from tkinter import ttk

def draw_fractal(canvas, depth):
    canvas.delete("all")  # Clear the canvas
    # Define starting points for the fractal
    points = [(400, 150), (200, 550), (600, 550)]
    draw_sierpinski(canvas, points, depth)

def draw_sierpinski(canvas, points, depth):
    if depth == 0:
        # Draw the triangle
        canvas.create_polygon(points, fill='black', outline='black')
    else:
        # Calculate the mid-points of each side
        p1 = midpoint(points[0], points[1])
        p2 = midpoint(points[1], points[2])
        p3 = midpoint(points[0], points[2])
        # Recursively draw smaller triangles
        draw_sierpinski(canvas, [points[0], p1, p3], depth-1)
        draw_sierpinski(canvas, [points[1], p1, p2], depth-1)
        draw_sierpinski(canvas, [points[2], p2, p3], depth-1)

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Recursive Data Visualization Tool")

    # Add a canvas for drawing fractals
    canvas = tk.Canvas(window, width=800, height=600, background="white")
    canvas.grid(column=0, row=1, columnspan=3)

    # Control for changing the depth of recursion
    depth_label = ttk.Label(window, text="Depth of recursion:")
    depth_label.grid(column=0, row=0, sticky=tk.W)
    depth = tk.IntVar(value=3)
    depth_scale = ttk.Scale(window, from_=1, to=10, variable=depth, orient=tk.HORIZONTAL)
    depth_scale.grid(column=1, row=0, sticky=(tk.W, tk.E))

    # Button to trigger fractal drawing
    draw_button = ttk.Button(window, text="Draw Fractal", command=lambda: draw_fractal(canvas, depth.get()))
    draw_button.grid(column=2, row=0, sticky=tk.E)

    window.mainloop()

if __name__ == "__main__":
    main()
