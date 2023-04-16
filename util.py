import tkinter as tk

# create a main window
root = tk.Tk()
root.title("TSP using Genetic Algorithm")

# set the size of the window
root.geometry("500x500")

# create a canvas for drawing the cities and the paths
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(side=tk.TOP, padx=10, pady=10)

# create a label for the number of cities
label_cities = tk.Label(root, text="Number of Cities:")
label_cities.pack(side=tk.LEFT, padx=10, pady=10)

# create an entry box for the number of cities
entry_cities = tk.Entry(root)
entry_cities.pack(side=tk.LEFT, padx=10, pady=10)

# create a button for generating the cities
button_generate = tk.Button(root, text="Generate Cities")
button_generate.pack(side=tk.LEFT, padx=10, pady=10)

# create a button for solving the TSP
button_solve = tk.Button(root, text="Solve TSP")
button_solve.pack(side=tk.LEFT, padx=10, pady=10)

# start the main loop
root.mainloop()
