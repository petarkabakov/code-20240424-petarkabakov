import pandas as pd
import numpy as np
from scipy import stats

# loading the file as a pandas data frame
df = pd.read_csv('interview_analysis_molecule_x_10mg_v1.tsv', sep='\t')

# displaying and looking at the schema of the file and the data types
df

df.info()

# checking that all the contract_id values are unique
unique_contract_id = df['contract_id'].unique()
num_unique_names = len(unique_contract_id)
num_rows = len(df)
if num_unique_names == num_rows:
    print('All values in the contract_id column are unique.')
else:
    print('There are duplicate values in the contract_id column.')

df['check_lowest_price'] = ((df['winner_price'] < df['second_place_price']) | (df['second_place_price'].isna())) & (df['outcome'] == 'won')
df = df[df['check_lowest_price'] == True]

z_scores = abs(df['winner_price'] - df['winner_price'].mean()) / df['winner_price'].std() #creating z-score
outliers = df[z_scores > 3]  # filtering out the outliers

# Remove outliers from the dataset
df = df[~df.isin(outliers)].dropna()
