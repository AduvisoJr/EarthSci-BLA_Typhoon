import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Day': ['Mon(L)', 'Mon(H)', 'Tue(L)', 'Tue(H)', 'Wed(L)', 'Wed(H)', 'Thu(L)', 'Thu(H)', 'Fri(L)', 'Fri(H)', 'Sat(L)', 'Sat(H)', 'Sun(L)', 'Sun(H)'],
    'Air Pressure (mb)': [6, 4, 5, 4, 6, 6, 7, 6, 4, 6, 0.998, 0.992, 0.999, 1.003],
    'Wind Speed (kph)': [1, 1, 3, 2, 0, 3, 0, 3, 2, 3, 6, 8, 2, 2],
    'Temperature (°C)': [26, 32, 26, 30, 25, 31, 24, 30, 25, 29, 25, 26, 25, 29],
    'Humidity (%)': [94, 76, 94, 72, 98, 82, 98, 76, 96, 80, 98, 99, 100, 99]
}

# Converting to a DataFrame
df = pd.DataFrame(data)

# Plotting Graph 4: Temperature, Air Pressure, Humidity, and Wind Speed
fig, ax1 = plt.subplots()

# Temperature Plot
ax1.set_xlabel('Day', fontsize=10, fontweight='bold')
ax1.set_ylabel('Temperature (°C) and Air Pressure (mb)', color='tab:orange', fontsize=10, fontweight='bold')
ax1.plot(df['Day'], df['Temperature (°C)'], color='tab:orange', label='Temperature')
ax1.tick_params(axis='y', labelcolor='tab:orange', labelsize=9)

# Adjusting the font size of the day labels
plt.xticks(fontsize=6.5)

# Air Pressure Plot (added to ax1 to overlay)
ax1.plot(df['Day'], df['Air Pressure (mb)'], color='tab:blue', label='Air Pressure')
ax1.legend(loc='upper left', bbox_to_anchor=(0.5, -0.15), ncol=2)

# Creating a second y-axis for Humidity and Wind Speed
ax2 = ax1.twinx()
ax2.set_ylabel('Humidity (%) & Wind Speed (kph)', color='tab:green', fontsize=10, fontweight='bold')

# Humidity Plot
ax2.plot(df['Day'], df['Humidity (%)'], color='tab:green', label='Humidity')

# Wind Speed Plot
ax2.plot(df['Day'], df['Wind Speed (kph)'], color='tab:red', label='Wind Speed')

ax2.tick_params(axis='y', labelcolor='tab:green', labelsize=9)

# Adding legends and title
fig.tight_layout()
ax2.legend(loc='upper right', bbox_to_anchor=(0.5, -0.15), ncol=2)

# Title with bold text
plt.title('Temperature, Air Pressure, Humidity, and Wind Speed', fontsize=12, fontweight='bold')
plt.show()