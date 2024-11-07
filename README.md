# 🚀 Layoffs Dataset 2024: Data Cleaning, Preparation, and Visualization 📊

This project involves cleaning and preparing the **2024 layoffs dataset** for analysis using **Python**, **SQL**, and **Power BI**. After cleaning the raw data, various visualizations were created in Power BI to analyze trends in layoffs by year, industry, location, and more.

##  📖Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Technologies Used](#technologies-used)
- [Dataset Description](#dataset-description)
- [Data Cleaning Process](#data-cleaning-process)
- [Power BI Visualizations](#power-bi-visualizations)
- [Code Explanation](#code-explanation)
- [Results](#results)
- [How to Run the Project](#how-to-run-the-project)
- [Credits](#credits)
- [License](#license)

##  Project Overview📁
This project focuses on preparing and visualizing the **2024 layoffs dataset**. After cleaning the raw data by addressing issues like missing values, duplicates, and inconsistent formats, I used **Power BI** to create various visualizations that uncover insights from the data. This includes a line chart to show layoffs by year and industry, a map chart for layoffs by country, and a summary card to visualize the total number of layoffs.

## 🎯 Objective
The goal of this project is to:
- Clean and prepare the **2024 layoffs dataset** for analysis.
- Create meaningful **visualizations** to help stakeholders understand trends and patterns in mass layoffs.

## 🛠 Technologies Used
- **🐍Python** (Pandas, NumPy)
- **🛢️SQL** (SQLite)
- **📊Power BI** (for visualizations)
- **📅Excel** (for initial inspection and analysis)

## 📊 Dataset Description
The dataset contains information about layoffs from 2020 to 2024, scraped from **Layoffs.fyi**. The purpose of the dataset is to enable the analysis of recent mass layoffs and discover patterns in the layoffs across industries and countries.

- **Data Source**: [Layoffs.fyi](https://layoffs.fyi/)
- **Credits**: Roger Lee

## 🧹 Data Cleaning Process
The data cleaning process involved several key steps:

1. **Removing Duplicates**: Duplicate rows were removed to ensure data integrity.
2. **Imputing Missing Values**: 
   - Numeric columns: Missing values were replaced with the **rounded mean** of the respective columns.
   - Categorical columns: Missing values were filled with the **mode** (most frequent value) of each column.
3. **Normalizing Data Formats**: 
   - **Text columns** were converted to **lowercase** for consistency.
   - **Date columns** were standardized to the 'YYYY-MM-DD' format.
4. **Data Type Standardization**: Ensured that all columns had the correct data types for analysis.

## 📊 Power BI Visualizations

After cleaning the data, I used **Power BI** to create a set of insightful visualizations:

1. **📈 Line Chart: Company Layoffs by Year and Industry**  
   - This line chart visualizes the number of layoffs across the years (2020-2024) and the industries most affected by layoffs.
   - It helps to identify trends in layoffs by industry and across different years.
![Line Chart](https://github.com/Willie-Conway/Data-Cleaning-and-Preparation/blob/7fd5f2473935251c79069134102d24aeee4d484b/Project/Screenshot%202024-11-04%20024517.png)

2. **🌍 Map Chart: Layoffs by Country**  
   - A map chart displays the total layoffs by country, enabling a geographic view of mass layoffs.
   - This helps identify regions with the highest concentration of layoffs and visualize global trends.
![Map Chart](https://github.com/Willie-Conway/Data-Cleaning-and-Preparation/blob/223d58b3c5e76d8cd6e5161e343ec185cc202db6/Project/Screenshot%202024-11-07%20004618.png)

3. **📊 Summary Card: Total Layoffs (1.03M)**  
   - A **card visual** was used to display the total number of layoffs across all years and industries, which came to **1.03 million**.
   - This provides a quick summary of the data for stakeholders.

4. **📊 Dashboard: Considated View** 
   - A consolidated view of all three visualizations in the **Power BI Dashboard**. This dashboard combines the **line 
     chart** 📈, **map chart** 🌍, and **summary card** 🗂 into a comprehensive, interactive interface for stakeholders to 
     explore layoffs trends, geographic distribution, and overall totals.

![Interactive Chart](https://github.com/Willie-Conway/Data-Cleaning-and-Preparation/blob/223d58b3c5e76d8cd6e5161e343ec185cc202db6/Project/Screenshot%202024-11-04%20024536.png)

  ## 📹 Demo Video

<div>
    <a href="https://www.loom.com/share/ef49067b43da4e19ba14152b7a50e69a">
      <p>Layoffs Dataset 2024: Data Cleaning, Preparation, and Visualization - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/ef49067b43da4e19ba14152b7a50e69a">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/ef49067b43da4e19ba14152b7a50e69a-740a4f6b19f2eaf5-full-play.gif">
    </a>
  </div>

## 💻 Code Explanation

Below is a summary of the key Python code used for cleaning the data:

```python
import pandas as pd
import numpy as np
import sqlite3

# Load the dataset
data = pd.read_csv(r'csv/layoffs_2024.csv')

# Initial data inspection
print("Initial data structure:")
print(data.info())

# Remove duplicate rows
data = data.drop_duplicates()

# Impute missing values
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for column in numeric_columns:
    mean_value = round(data[column].mean(), 2)
    data[column] = data[column].fillna(mean_value)

categorical_columns = data.select_dtypes(include=['object']).columns
for column in categorical_columns:
    mode_value = data[column].mode()[0]
    data[column] = data[column].fillna(mode_value)

# Normalize text data
for column in categorical_columns:
    data[column] = data[column].str.lower()

# Standardize date formats
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

# Ensure correct data types
data['total_laid_off'] = pd.to_numeric(data['total_laid_off'], errors='coerce')
data['percentage_laid_off'] = pd.to_numeric(data['percentage_laid_off'], errors='coerce')
data['funds_raised'] = pd.to_numeric(data['funds_raised'], errors='coerce')

# Save cleaned data to CSV and SQL
cleaned_file_path = 'cleaned_layoffs_2024.csv'
data.to_csv(cleaned_file_path, index=False)

conn = sqlite3.connect('cleaned_layoffs.db')
data.to_sql('cleaned_layoffs', conn, if_exists='replace', index=False)
conn.close()
```

## 📝 Key Steps

1. **Load Dataset**: The dataset is loaded from a CSV file.
2. **Remove Duplicates**: Duplicate rows are dropped.
3. **Impute Missing Values**: Missing values in numeric and categorical columns are imputed using the mean and mode, respectively.
4. **Normalize Data**: Text data is converted to lowercase, and date columns are standardized.
5. **Save the Cleaned Data**: The cleaned data is saved in both CSV and SQLite formats.

## 📈 Results

- **Data Cleaned**: The dataset was cleaned of duplicate entries, and missing values were imputed.
- **Visualizations Created**: After cleaning the data, the following Power BI visualizations were created:
  - **Line Chart**: Showed layoffs by year and industry from 2020 to 2024.
  - **Map Chart**: Visualized the geographic distribution of layoffs by country.
  - **Summary Card**: Displayed the total number of layoffs (1.03M).

## 🏃‍♀️ How to Run the Project

1. **Clone or download the repository**.
2. **Make sure you have the required Python libraries installed**:
    ```bash
    pip install pandas numpy sqlite3
    ```
3. **Place the `layoffs_2024.csv` file in the `csv/` directory**.
4. **Run the Python script to clean the dataset**:
    ```bash
    python clean_layoffs_data.py
    ```
5. **Import the cleaned dataset (`cleaned_layoffs_2024.csv`) into **Power BI** for visualization**.

## 👏 Credits

- **Dataset**: [Layoffs.fyi](https://layoffs.fyi/)
- **Author**: Roger Lee
- **Project Developer**: Willie Conway ✨

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
