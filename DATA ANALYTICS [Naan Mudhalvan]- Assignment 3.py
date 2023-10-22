#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load the dataset
df = pd.read_csv('House Price India.csv')
import matplotlib.pyplot as plt
import seaborn as sns


# Univariate Analysis
#Univariate analysis is about analyzing individual variables.

# Create a histogram for the 'Price' column
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.show()


#Bivariate Analysis
#Bivariate analysis involves analyzing two variables together
# Create a scatter plot for 'living area' vs. 'Price'

plt.figure(figsize=(10, 6))
sns.scatterplot(x='living area', y='Price', data=df)
plt.title('Living Area vs. Price')
plt.show()


#Multi-Variate Analysis
#Multi-variate analysis can involve visualizing relationships between three or more variables. 
# Create a pair plot for selected columns
selected_columns = ['living area', 'Price', 'Number of schools nearby', 'Distance from the airport']
sns.pairplot(df[selected_columns])
plt.show()

#Descriptive Statistics
#You can use Pandas to compute descriptive statistics for the dataset:
# Generate descriptive statistics
stats = df.describe()
print(stats)

#Handle Missing Values

#To handle missing values, you can either impute them or remove rows/columns with missing data, 
#depending on the extent of missing values in your dataset
# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Impute missing values with the mean
df['waterfront present'].fillna(df['number of views'].mean(), inplace=True)



# In[ ]:




