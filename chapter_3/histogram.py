import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
y_values = [3, 0, 2, 10, 0, 30, 22, 15, 10, 6, 4]

# Creating a histogram
plt.bar(x_values, y_values, width=5 ,color='blue', edgecolor='black')
 
# Adding labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Bar Chart Example with Different X and Y Values')

# Display the plot
plt.show()
