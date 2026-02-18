import numpy as np #To create the  grid
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation # For the time evolution

# Grid size
N = 100

# States: 0 = OFF, 1 = ON, 2 = REFRACTORY

grid = np.zeros((N, N), dtype=int) # A 2D array with state 0 = OFF


# Random initial firing cells
grid[np.random.rand(N, N) < 0.1] = 1  # 10% True = 1



def count_on_neighbors(x, y, g):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue   # skip the center cell
            nx, ny = (x + dx) % N, (y + dy) % N  # Preiodic boundary conditions
            if g[nx, ny] == 1:
                count += 1
    return count

def update(frame):
    global grid  # make global variable
    new_grid = np.zeros_like(grid)  # make a new grid

    for i in range(N):
        for j in range(N):
            if grid[i, j] == 0:  # OFF
                if count_on_neighbors(i, j, grid) == 2: # If exactly two neighbour is on...
                    new_grid[i, j] = 1                    # The cell is ON (Rule 1) 
            elif grid[i, j] == 1:  # ON
                new_grid[i, j] = 2
            else:  # REFRACTORY
                new_grid[i, j] = 0   # Refractory cells recover (Rule 3)

    grid = new_grid
    img.set_data(grid)
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="viridis")


ani = FuncAnimation(fig, update, frames=300, interval=50)
plt.show()

