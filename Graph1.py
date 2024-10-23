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

# Plotting Graph 1: Air Pressure and Wind Speed
fig, ax1 = plt.subplots()

# Air Pressure Plot
ax1.set_xlabel('Day', fontweight='bold')
ax1.set_ylabel('Air Pressure (mb)', color='tab:blue', fontweight='bold')
ax1.plot(df['Day'], df['Air Pressure (mb)'], color='tab:blue', label='Air Pressure')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Adjusting the font size of the day labels
plt.xticks(fontsize=6.5)

# Creating a second y-axis for Wind Speed
ax2 = ax1.twinx()
ax2.set_ylabel('Wind Speed (kph)', color='tab:red', fontweight='bold')
ax2.plot(df['Day'], df['Wind Speed (kph)'], color='tab:red', label='Wind Speed')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Adding legends and title
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Air Pressure and Wind Speed', fontweight='bold')
plt.show()