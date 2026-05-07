Financial Transaction Data Analysis

This project performs data cleaning, transformation, aggregation, and visualization on a financial transaction dataset using Python libraries like Pandas, NumPy, Matplotlib, and Seaborn.

📌 Project Overview
The main objective of this project is to analyze financial transaction data and generate useful insights such as:

Total transaction amount by transaction type
Average transaction amount
Number of transactions
Categorization of transaction amounts
Visualization of aggregated transaction data  

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn

📂 Dataset
The project uses a CSV dataset:
Financial_datasets_log.csv
The dataset contains financial transaction records.

Example columns may include:
Column Name	Description
type	Transaction type
amount	Transaction amount

⚙️ Features Implemented

1. Data Loading
Reads the dataset using Pandas.

2. Data Cleaning
Checks missing values
Removes duplicate records

3. Feature Engineering
Creates a new categorical column called Amount_Category.

Transaction amounts are divided into:
Low
Medium
High

4. Data Aggregation
Groups data based on transaction type and calculates:
Total amount
Average amount
Transaction count

5. Data Visualization
Creates a bar chart showing total transaction amount by transaction type.

📊 Output
The project generates:
Cleaned dataset
Aggregated transaction summary
Bar graph visualization 

▶️ How to Run the Project

Step 1: Install Required Libraries
pip install pandas numpy matplotlib seaborn

Step 2: Place Dataset
Keep the dataset file:
Financial_datasets_log.csv
inside the project folder.

Step 3: Run the Script
python filename.py
Replace filename.py with your Python file name.

📈 Sample Visualization
The output graph displays:
Transaction Types on X-axis
Total Transaction Amount on Y-axis
This helps in understanding transaction distribution and financial trends.

📚 Learning Outcomes
Through this project, you can learn:

Data Cleaning
Data Transformation
Feature Engineering
GroupBy Aggregation
Data Visualization
Exploratory Data Analysis (EDA)
🚀 Future Improvements

Possible future enhancements:

Add more visualizations
Perform fraud detection analysis
Build dashboards using Power BI or Tableau
Apply Machine Learning models
Add real-time transaction analytics
