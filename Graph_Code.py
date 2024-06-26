"""
Author: Suryanarayana Ravi
Description: This Python script generates a scatter plot from data stored in an Excel sheet and overlays a reference line. It is designed to visualize relationships between two variables and compare them against a predetermined threshold.

Instructions:
1. Replace the file path with the location of your Excel sheet containing the data.
2. Customize plot parameters such as title, axis labels, and reference line as necessary.
3. Run the script to generate the plot.

MIT License
Copyright (c) 2024 Suryanarayana 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Importing necessary libraries
import pandas as pd # Importing pandas library for data manipulation
import matplotlib.pyplot as plt # Importing matplotlib library for plotting

# Step 1: Read data from the Excel sheet
data = pd.read_excel("C:\\Users\\Surya\\Example.xlsx") # Reading data from Excel sheet and storing it in a DataFrame

# Step 2: Create the plot
plt.figure(figsize=(18, 8)) # Creating a figure object with specific size

# Step 3: Plot the data
plt.scatter(data['X axis'], data['Y axis'], label='Data', s=1) # Plotting scatter plot for X and Y axis
plt.axhline(y=20, color='r', linestyle='--', label='Reference line') # Adding a reference line

# Step 4: Add title and labels
plt.title('Title') # Adding title to the plot
plt.xlabel('X axis', fontsize=14) # Adding label to X axis with specific font size
plt.ylabel('Y axis', fontsize=14) # Adding label to Y axis with specific font size

# Step 5: Customize tick labels
plt.xticks(fontsize=18) # Setting font size for X axis tick labels
plt.yticks(fontsize=18) # Setting font size for Y axis tick labels

# Step 6: Add legend and grid
plt.legend(fontsize=12) # Adding legend with specific font size
plt.grid(True) # Adding grid to the plot

# Step 7: Show the plot
plt.show() # Displaying the plot