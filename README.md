# 🚗 Car Price Prediction

## 📌 Overview

This project analyzes and visualizes car price data to identify patterns and insights using Python. The dataset includes various car attributes such as engine size, body style, fuel type, and price. The goal is to perform exploratory data analysis (EDA) and statistical analysis to understand key factors affecting car prices.

## ✨ Features

- 🛠️ Data Cleaning and Preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 📈 Data Visualization (Histograms, Scatter Plots, Boxplots, Heatmaps)
- 🔢 Feature Engineering (Categorical to Numerical Conversion, Normalization)
- 📊 ANOVA Statistical Testing
- 📉 Regression Analysis

## 💻 Tech Stack

- 🐍 Python
- 🏷️ Pandas
- 🔢 NumPy
- 🎨 Matplotlib
- 🌊 Seaborn
- 🧪 SciPy

## 🛠️ Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Car-Price-Prediction.git
   cd Car-Price-Prediction
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```sh
   python src/main.py
   ```

## 📂 Project Structure

```
Car-Price-Prediction/
├── 📄 output.csv                        # Dataset used for analysis
├── 📝 main.py                           # Main script for data analysis
├── 📜 README.md                         # Project documentation
│── 🛑 .gitignore                        # Ignore unnecessary files (e.g., __pycache__, .DS_Store)
│── 📜 requirements.txt                  # Dependencies
│── 📜 LICENSE                           # License information
│── 📜 README.md                         # Overview of the project
```

## 🔍 Data Preprocessing

- 🚀 Removed unnecessary index columns.
- 🛠️ Handled missing values.
- 🔄 Converted 'city-mpg' to 'city-L\_per\_100km'.
- 📏 Normalized 'length', 'width', and 'height'.
- 📌 Categorized price into 'Low', 'Medium', and 'High' bins.
- 🔢 Converted categorical values (e.g., 'fuel-type') to numerical.

## 📊 Visualizations

- 📊 Histogram of price categories.
- ⚙️ Scatter plot: Engine Size vs Price.
- 📦 Boxplot: Price Distribution.
- 🔥 Heatmap of Average Price based on Drive Wheels and Body Style.
- 📉 Regression Analysis: Engine Size vs Price.

## 🧪 Statistical Analysis

- 📊 ANOVA test to analyze price variance across different car makes.

## 📈 Results

- 📊 Engine size has a strong correlation with price.
- 🚗 Drive-wheel type and body style significantly influence car pricing.
- ⛽ Fuel type conversion reveals categorical importance in pricing.

## 🤝 Contributing

Feel free to fork this repository and contribute improvements! 🚀

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

