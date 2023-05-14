import tkinter as tk
import random

# List of boids
boids = []

class Boid:
    def __init__(self, x, y, size, speed, canvas):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.canvas = canvas
        # Top left corner of the oval at (x - size, y - size), bottom right corner at (x + size, y + size)
        self.circle = canvas.create_oval(x - size, y - size, x + size, y + size, fill='white')

    # Movement function for the boid
    def move(self):
        self.x += self.speed
        self.y += self.speed
        self.canvas.move(self.circle, self.speed, self.speed)

def update():
    for boid in boids:
        boid.move()
    canvas.after(10, update)

# Creating the canvas
root = tk.Tk()
# Canvas is 800 x 600
canvas = tk.Canvas(root, width = 800, height = 600, bg='black')
canvas.pack()

# Creating a number of boids
for i in range(10):
    # Spawns boids in random places on the canvas
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    # Determining the size of the boid
    boid = Boid(x, y, 10, 1, canvas)
    boids.append(boid)

update()
root.mainloop()
