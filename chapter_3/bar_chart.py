from matplotlib import pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 35]

# Creating a bar chart
plt.bar(categories, values, color='skyblue')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Display the plot
plt.show()
