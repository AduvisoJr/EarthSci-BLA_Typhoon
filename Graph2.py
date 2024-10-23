import pandas as pd 
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Day': ['Mon(L)', 'Mon(H)', 'Tue(L)', 'Tue(H)', 'Wed(L)', 'Wed(H)', 'Thu(L)', 'Thu(H)', 'Fri(L)', 'Fri(H)', 'Sat(L)', 'Sat(H)', 'Sun(L)', 'Sun(H)'],
    'Air Pressure (mb)': [1.006, 1.004, 1.005, 1.004, 1.006, 1.006, 1.007, 1.006, 1.004, 1.006, 0.998, 0.992, 0.999, 1.003],
    'Wind Speed (kph)': [1, 1, 3, 2, 0, 3, 0, 3, 2, 3, 6, 8, 2, 2],
    'Temperature (°C)': [26, 32, 26, 30, 25, 31, 24, 30, 25, 29, 25, 26, 25, 29],
    'Humidity (%)': [94, 76, 94, 72, 98, 82, 98, 76, 96, 80, 98, 99, 100, 99]
}

# Converting to a DataFrame
df = pd.DataFrame(data)

# Plotting Graph 2: Temperature and Humidity
fig, ax1 = plt.subplots()

# Temperature Plot
ax1.set_xlabel('Day', fontweight='bold')
ax1.set_ylabel('Temperature (°C)', color='tab:orange', fontweight='bold')
ax1.plot(df['Day'], df['Temperature (°C)'], color='tab:orange', label='Temperature')
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Adjusting the font size of the day labels
plt.xticks(fontsize=6.5)

# Creating a second y-axis for Humidity
ax2 = ax1.twinx()
ax2.set_ylabel('Humidity (%)', color='tab:green', fontweight='bold')
ax2.plot(df['Day'], df['Humidity (%)'], color='tab:green', label='Humidity')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Adding legends and title
fig.tight_layout()
ax1.legend(loc='upper left', bbox_to_anchor=(0.5, -0.15), ncol=2)
ax2.legend(loc='upper right', bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.title('Temperature and Humidity', fontweight='bold')
plt.show()