# By imanshirani 09-04-2024
import pymxs

# Get the 3ds Max core interface
rt = pymxs.runtime

def arrange_in_grid(objects, rows, cols, spacing=10):
    """
    Arranges the given objects in a grid pattern.

    Parameters:
    - objects: List of objects to arrange.
    - rows: Number of rows in the grid.
    - cols: Number of columns in the grid.
    - spacing: Distance between the objects.
    """
    for i, obj in enumerate(objects):
        row = i // cols
        col = i % cols
        x_position = col * spacing
        y_position = row * spacing
        z_position = 0  # Assuming you want to arrange on the X-Y plane

        # Set the object's position
        obj.position = rt.Point3(x_position, y_position, z_position)

# Main function to execute the arrangement
def main():
    # Get the currently selected objects
    selected_objects = rt.selection

    if not selected_objects:
        print("No objects selected.")
        return

    # Define grid parameters
    rows = 3  # Number of rows
    cols = 3  # Number of columns
    spacing = 20  # Spacing between objects

    # Arrange the selected objects in a grid
    arrange_in_grid(selected_objects, rows, cols, spacing)
    print("Objects arranged in a grid.")

# Execute the main function
main()
