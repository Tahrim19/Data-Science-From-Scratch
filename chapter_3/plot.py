import matplotlib.pyplot as plt

# Sample data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.2, 1075.9, 2862.5, 5979.6, 1089.7, 14958.3]

# Plotting
plt.plot(years , gdp, color ='green' , marker = '.')

# Adding Labels and Titles
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.xlabel("Years")

# Display the plot
plt.show()

