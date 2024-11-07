import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Define circle parameters: (x, y) coordinates and radius
circles = [
    Circle((0.4, 0.5), 0.3, color='pink', alpha=0.4, label="RAVDESS"),
    Circle((0.6, 0.5), 0.3, color='lightblue', alpha=0.4, label="CREMA-D"),
    Circle((0.5, 0.7), 0.3, color='lightgreen', alpha=0.4, label="SAVEE"),
    Circle((0.5, 0.3), 0.3, color='orange', alpha=0.4, label="TESS")
]

# Add circles to plot
for circle in circles:
    ax.add_patch(circle)

# Add text labels for each dataset
ax.text(0.25, 0.5, "RAVDESS", fontsize=12, ha='center', va='center', color='black')
ax.text(0.75, 0.5, "CREMA-D", fontsize=12, ha='center', va='center', color='black')
ax.text(0.5, 0.8, "SAVEE", fontsize=12, ha='center', va='center', color='black')
ax.text(0.5, 0.2, "TESS", fontsize=12, ha='center', va='center', color='black')

# Add text label for the central overlap
ax.text(0.5, 0.5, "Angry, Happy, Sad, Neutral,\nFearful, Disgusted, Surprised", 
        fontsize=10, ha='center', va='center', color='black')

# Set title and remove axes for cleaner look
ax.set_title("Emotions Across RAVDESS, CREMA-D, SAVEE, and TESS")
ax.axis("off")

# Show plot
plt.show()
