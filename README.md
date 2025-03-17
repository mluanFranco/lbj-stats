# Statistical Analysis of LeBron James' Performance (College Project)

## Project Description
This project performs a statistical analysis of the basketball player LeBron James' performance based on a dataset containing his game statistics. The Python script processes a CSV file (lebron_stats.csv), cleans and organizes the data, calculates descriptive statistics, and generates visualizations to better understand the player's performance over the years.

## Features
- Reads and processes data from a CSV file.
- Removes irrelevant columns.
- Converts and normalizes data (such as dates and minutes played).
- Calculates descriptive statistical measures, including:
    - Mean
    - Mode
    - Median
    - Standard Deviation
    - Variance
- Generates a histogram to visualize the distribution of points per game.

![Histogram](histograma.png)

- Calculates and analyzes the skewness of the points distribution.

## Requirements
To run the project, the following Python libraries must be installed:

- pandas
- numpy
- scipy
- matplotlib
- statistics
- math

**If not installed, use the following command:**
- pip install pandas numpy scipy matplotlib

## How to run
1. Ensure that the lebron_stats.csv file is in the same directory as the analise_lebron.py script.

2. Run the Python script:
python analise_lebron.py

3. The program will display the calculated statistics in the terminal and generate a histogram for visual analysis.

## Expected Output
- Basic statistics of the processed data.
- Descriptive measures for the "PTS" (points per game) column.
- Histogram of the distribution of points per game.
- Calculation of the skewness coefficient and determination of the type of points distribution.
