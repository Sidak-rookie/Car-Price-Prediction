import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# Load the dataset
dataframe = pd.read_csv("/output.csv")

# Eliminate the index column
dataframe = dataframe.iloc[:, 1:]

#Assign column headers
column_names = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
    "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
    "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"
]
dataframe.columns = column_names

# Identify missing values
missing_info = dataframe.isnull().sum()
print("Columns with missing values:\n", missing_info)

# Remove rows where 'price' has '?', then convert to integer
dataframe = dataframe[dataframe['price'] != '?']
dataframe['price'] = dataframe['price'].astype(int)

# Normalize length, width, and height
dataframe[['length', 'width', 'height']] = dataframe[['length', 'width', 'height']].apply(lambda col: col / col.max())

# Categorizing price into bins
price_intervals = np.linspace(dataframe['price'].min(), dataframe['price'].max(), 4)
category_labels = ['Low', 'Medium', 'High']
dataframe['price-category'] = pd.cut(dataframe['price'], price_intervals, labels=category_labels, include_lowest=True)

# Plot histogram
plt.hist(dataframe['price-category'], bins=3, edgecolor='black')
plt.xlabel("Price Group")
plt.ylabel("Frequency")
plt.title("Distribution of Price Categories")
plt.show()

# Convert categorical 'fuel-type' to numerical
df_dummies = pd.get_dummies(dataframe['fuel-type'])
dataframe = pd.concat([dataframe, df_dummies], axis=1)
dataframe.drop(columns=['fuel-type'], inplace=True)

# Display descriptive statistics
print(dataframe.describe())

# Boxplot for price distribution
sns.boxplot(y=dataframe['price'])
plt.title("Price Box Plot")
plt.show()

# Scatter plot: Engine Size vs Price
plt.scatter(dataframe['engine-size'], dataframe['price'], alpha=0.5)
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.title("Scatter Plot: Engine Size vs Price")
plt.grid()
plt.show()

# Grouping Data
grouped_data = dataframe.groupby(['drive-wheels', 'body-style'])[['price']].mean().reset_index()
print(grouped_data)

# Creating a pivot table for visualization
pivot_chart = grouped_data.pivot(index='drive-wheels', columns='body-style', values='price')
sns.heatmap(pivot_chart, cmap='coolwarm', annot=True)
plt.title("Heatmap of Average Price")
plt.show()

# Regression plot: Engine Size vs Price
sns.regplot(x='engine-size', y='price', data=dataframe)
plt.title("Regression Analysis: Engine Size vs Price")
plt.show()
