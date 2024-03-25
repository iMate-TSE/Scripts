import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = [
    ((1.0, 1.0, 1.0), "Excited"),
    ((1.0, 0.5, 1.0), "Happy"),
    ((0.9, 0.2, 0.8), "Loved/Grateful"),
    ((0.9, 0.2, 0.2), "Relaxed"),
    ((0.1, 0.9, 1.0), "Angry"),
    ((0.2, 0.9, 0.7), "Stressed"),
    ((0.1, 0.6, 0.4), "Anxious"),
    ((0.0, 0.7, 0.45), "Disgust"),
    ((0.1, 0.1, 0.1), "Sad"),
    ((0.2, 0.1, 0.3), "Bored"),
    ((0.4, 0.4, 0.4), "Sleepy"),
    ((0.1, 0.3, 0.0), "Lonely"),
    ((0.0, 0.0, 0.0), "Depressed")
]

# Extract coordinates and labels
coordinates, labels = zip(*data)
x, y, z = zip(*coordinates)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each point
for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i], c='b', marker='o')
    ax.text(x[i], y[i], z[i], labels[i])

# Set labels and title
ax.set_xlabel('Pleasure')
ax.set_ylabel('Arousal')
ax.set_zlabel('Dominance')
ax.set_title('PAD Emotional Scale')

plt.show()
