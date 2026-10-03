# Iris Dataset Analysis with Python

# Project Overview

This project explores the classic Iris dataset using Python to demonstrate fundamental data analysis and visualization techniques.

The analysis focuses on understanding the structure of the dataset, examining distributions, comparing measurements across Iris species, and identifying relationships between numerical features.

# Objectives

The main objectives of this analysis were to:

- Explore and understand the dataset
- Inspect the structure, columns, data types, and summary statistics
- Check for missing values and duplicate records
- Compare measurements across Iris species
- Examine the distribution of sepal length
- Analyze the distribution of petal length across species
- Investigate relationships between numerical measurements
- Communicate findings through data visualizations

# Dataset

The dataset contains measurements for 150 Iris flowers belonging to three species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

The measurements analyzed include:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

# Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

# Analysis Performed

1. Data Exploration

The dataset was inspected using Python and Pandas to understand:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records
- Descriptive statistics

The dataset contains 150 observations and 6 columns. The analysis found no missing values or duplicate records.

2. Species-Level Analysis

The numerical measurements were grouped by species to compare their average values.

The analysis showed clear differences in average petal length:

Species| Average Petal Length (cm)
Iris-setosa| 1.462
Iris-versicolor| 4.260
Iris-virginica| 5.552

Iris-setosa had the lowest average petal length, while Iris-virginica had the highest.

# Visualizations

Average Petal Length by Species

This bar chart compares the average petal length across the three Iris species.

"Average Petal Length by Species" (charts/average_petal_length.png)

Distribution of Sepal Length

The histogram shows how sepal-length measurements are distributed across the dataset.

"Distribution of Sepal Length" (charts/sepal_length_distribution.png)

Petal Length Distribution by Species

The box plot compares the distribution and spread of petal length across the three species.

"Petal Length Distribution by Species" (charts/petal_length_boxplot.png)

Correlation Between Iris Measurements

The correlation heatmap shows the strength and direction of relationships between the numerical measurements.

"Correlation Between Iris Measurements" (charts/correlation_heatmap.png)

# Key Findings

- Petal length differs considerably across the three Iris species.
- Iris-setosa has the smallest average petal length, while Iris-virginica has the largest.
- The distribution of sepal length shows variation across the 150 observations.
- Petal length distributions differ noticeably between the three species.
- Petal length and petal width have a very strong positive correlation of approximately 0.96.
- Sepal length also has strong positive relationships with petal length and petal width.
- Sepal width has comparatively weaker relationships with the other measurements.

# Overall Insight

The analysis indicates that petal measurements contain substantial information for distinguishing the three Iris species. In particular, petal length and petal width show a strong positive relationship, while species-level analysis reveals clear differences in petal measurements.

# Project Structure

Iris Dataset Analysis
│
├── Iris.csv
├── iris_analysis.py
├── requirements.txt
├── README.md
│
└── charts/
    ├── average_petal_length.png
    ├── sepal_length_distribution.png
    ├── petal_length_boxplot.png
    └── correlation_heatmap.png

# How to Run the Project

1. Install Python

Make sure Python is installed on your computer.

2. Install the required libraries

From the project directory, run:

pip install -r requirements.txt

3. Run the analysis

Run:

python iris_analysis.py

The script performs the analysis and generates the visualizations.

# Author

-Genesis Suwa-

Data Analysis Portfolio Project
