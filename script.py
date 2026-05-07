# Standard Data Analytics pipeline:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Step 2 Load the data
df = pd.read_csv("Financial_datasets_log.csv")

print(df.head())
print(df.info())

#Step 3 Cleaning the data
#Handle missing values , Remove duplicate data  , Correct data type 

# Gives sum of null values if present
print(df.isnull().sum())

# Removing Duplicate Rows
df.drop_duplicates(inplace=True) # inplace=True Means modify original dataframe directly 
print(df.info())

# Step 4 := Transformation
# Feature Engineering : New Col addition
# Categorization :- Group of numeric data for better analysis

df['Amount_Category'] = pd.cut(df['amount'] , bins=[0 , 5000 ,10000, 20000] , labels=['Low' , 'Medium' , 'High'])
print(df.head())

# Step 5 Data Aggregation := Groupby or pivot using pandas
transaction_summary = df.groupby("type").agg(
    total_amount = ("amount" , "sum"),
    avg_amount = ("amount" , "mean"),
    count_trans = ("amount" , "count")
).reset_index()

# Step 6 Visualization

plt.figure(figsize=(10,6))
sns.barplot(x="type" , y="total_amount" , data=transaction_summary)
plt.title("Bank Data For Amount Groups")
plt.show()