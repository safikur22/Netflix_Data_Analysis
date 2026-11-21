# Step 1 - Import Pandas and Numpy
import pandas as pd
import numpy as np

# Step 2 - Import CSV File to perform Data analysis process
net = pd.read_csv("netflix_data.csv")
net.info()

# Step 3 - Find is their any null value
net.isna()

# Step 4 - Removing Column
net = pd.read_csv("netflix_data.csv")
net.drop(columns=["description", "show_id"], axis=1, inplace=True)

# Step 5 - Remove duplicates
net.drop_duplicates(inplace=True)

# Step 6 - Check number of duplicates
net.duplicated().sum()

# Step 7 - Change Name of Column
net.rename(columns={'title': 'Movie_title', "type": "Movie_Type"}, inplace=True)

# Step 8 - Replaceing NULL Value
net['director'] = net['director'].fillna('Unknown')
net['cast'] = net['cast'].fillna('Unknown')
net['country'] = net['country'].fillna('Unknown')

# Step 9 - Change Data Type
net["date_added"] = pd.to_datetime(net["date_added"], errors='coerce')
net["release_year"] = net["release_year"].astype('int64')

# Step 10 - Removing Space
text_cols = net.select_dtypes(include='object').columns

for col in text_cols:
    net[col] = net[col].str.strip()

# Step 11 - Verified Clean Data
print("Dataset Shape:", net.shape)
print("Duplicate Rows:", net.duplicated().sum())
print("\nMissing Values:")
print(net.isnull().sum())
print("\nData Types:")
print(net.dtypes)

# Download/Export Data Sheet
net.to_csv("Netflix_cleaned_dataset.csv", index=False)
