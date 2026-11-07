import numpy as np
import matplotlib.pyplot as plt

temps = np.arange(20, 71, 5)

activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])

# Find optimum temperature
optimum = temps[np.argmax(activity)]

print("Optimum Temperature:", optimum, "°C")

# Plot line graph
fig, ax = plt.subplots()

ax.plot(temps, activity, marker='o', linestyle='-', label='Activity')

# Mark optimum temperature
ax.axvline(optimum, color='red', linestyle='--')

# Annotate peak
ax.annotate(
    'Optimum Temperature = 50°C',
    xy=(optimum, max(activity)),
    xytext=(35, 100),
    arrowprops=dict(arrowstyle='->', color='red')
)

ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Relative Activity")
ax.set_title("Temperature vs Enzyme Activity")

ax.legend()
plt.show()