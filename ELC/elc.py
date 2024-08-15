import pandas as pd
import matplotlib.pyplot as plt

temprature_data={
    "Date":pd.date_range(start='2023-01-01',end='2023-01-10'),
    "City_A":[25.5,26.2,24.8,23.5,22.9,27.0,26.5,25.8,24.0,23.2],
    "City_B":[22.0,21.5,23.8,25.0,24.5,22.5,21.0,23.2,24.5,25.0]
}

temprature_df=pd.DataFrame(temprature_data)
print(temprature_df)

# 1. Calculate the average temperature for each city
avg_temp = temprature_df[['City_A', 'City_B']].mean()
print("\nAverage Temperatures:")
print(avg_temp)

# 2. Find the date with the highest temperature in City A
max_temp_a = temprature_df.loc[temprature_df['City_A'].idxmax()]['Date']
print("\nDate with the highest temperature in City A:", max_temp_a)

# 3. Visualize the temperature trends for both cities using Matplotlib
# plt.figure(figsize=(10, 6))

# # Plot temperature trends for City A
# plt.plot(temprature_df['Date'], temprature_df['City_A'], label='City A')

# # Plot temperature trends for City B
# plt.plot(temprature_df['Date'], temprature_df['City_B'], label='City B')

temprature_df.plot(kind='bar',ylim=(0,50),x='Date')

plt.title('Temperature Trends')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()