import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, length, level, max_level):
    if level > max_level:
        return

    # Calculate the end points of the branch
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Draw the branch
    ax.plot([x, x_end], [y, y_end], color='brown', lw=max_level/level)

    # Calculate new branch length
    new_length = length * np.cos(np.pi / 4)

    # Draw the left branch
    draw_pythagoras_tree(ax, x_end, y_end, angle + np.pi / 4, new_length, level + 1, max_level)
    
    # Draw the right branch
    draw_pythagoras_tree(ax, x_end, y_end, angle - np.pi / 4, new_length, level + 1, max_level)

def plot_pythagoras_tree(max_level):
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    draw_pythagoras_tree(ax, 0, 0, np.pi / 2, 1, 1, max_level)

    plt.show()

recursion_level = int(input("Enter the recursion level: "))
plot_pythagoras_tree(recursion_level)
