# Diabetes CGM Analysis

## Overview

This project explores continuous glucose monitoring (CGM) data and related physiological and behavioral measurements using Python. The goal is to validate the dataset, investigate glucose patterns, and prepare the data for further analysis and storage in PostgreSQL.

The project is currently focused on data validation and exploratory data analysis (EDA).

## Objectives

- Validate the structure and quality of CSV files.
- Check missing values, duplicate records, and timestamp validity.
- Analyze time intervals between consecutive measurements.
- Explore glucose dynamics and distributions.
- Calculate descriptive statistics and compare glucose ranges.
- Prepare the dataset for PostgreSQL integration.
- Investigate relationships between glucose, insulin delivery, carbohydrate intake, and physical activity.

## Dataset

The dataset consists of 25 CSV files containing time-series measurements.

Available variables include:

| Variable | Description |
|---|---|
| `time` | Timestamp of the observation |
| `glucose` | Glucose measurement |
| `calories` | Calories-related measurement |
| `heart_rate` | Heart rate |
| `steps` | Step count |
| `basal_rate` | Basal insulin delivery |
| `bolus_volume_delivered` | Delivered bolus insulin |
| `carb_input` | Recorded carbohydrate intake |

The exact units and semantics of individual variables should be confirmed using the dataset documentation.

## Data Validation

The validation script checks:

- Number of records and columns
- Column names and data types
- Missing values
- Duplicate rows and timestamps
- Invalid timestamps
- Descriptive statistics
- Time intervals between consecutive observations

### Initial Validation Results

The initial validation covered all 25 CSV files and reported:

- **Total records:** 309,392
- **Missing values:** 0
- **Duplicate rows:** 0
- **Invalid timestamps:** 0

These results describe structural checks and do not guarantee that every measurement is valid or clinically plausible.

## Exploratory Data Analysis

The notebook `01_data_exploration.ipynb` currently includes:

- Glucose measurements over time for one participant
- Glucose distribution histograms with different bin counts
- Descriptive statistics: mean, median, standard deviation, minimum, and maximum
- Percentages of measurements within selected glucose ranges

Further analysis will extend these results to all participants.

## Technologies

- Python
- pandas
- Matplotlib
- Jupyter Notebook
- Git and GitHub
- PostgreSQL (planned)

## Planned Work

- Extend exploratory data analysis to all participants.
- Compare glucose variability and distributions across participants.
- Investigate relationships between glucose, insulin delivery, carbohydrate intake, and physical activity.
- Design a PostgreSQL database and implement data loading.
- Develop machine learning models to explore glucose patterns and evaluate short-term glucose prediction.
- Evaluate model performance using appropriate validation methods and metrics.
- Document analytical findings and limitations.

## Responsible Data Handling

Raw data files are excluded from version control by default. Before publishing datasets or derived results, their license, privacy requirements, and potential for participant re-identification should be reviewed.

This project is for data analysis and educational purposes and is not intended to provide medical advice.
