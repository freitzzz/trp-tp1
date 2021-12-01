import pandas as pd
import numpy as np
import sys

args = sys.argv

csv_file_path = args[1]

data = pd.read_csv(csv_file_path)

# Pandas usaged based on https://stackoverflow.com/a/69001342
# sample data of all dtypes in pandas (column 'a' has an outlier)         # dtype:
df = data  # category
# limits to a (float), b (int) and e (timedelta)
cols = df.select_dtypes('number').columns
df_sub = df.loc[:, cols]


# OPTION 1: z-score filter: z-score < 3
lim1 = np.abs((df_sub - df_sub.mean()) / df_sub.std(ddof=0)) < 3

# OPTION 2: quantile filter: discard 1% upper / lower values
lim2 = np.logical_or(df_sub < df_sub.quantile(0.99, numeric_only=False),
                     df_sub > df_sub.quantile(0.01, numeric_only=False))

# OPTION 3: iqr filter: within 2.22 IQR (equiv. to z-score < 3)
iqr = df_sub.quantile(0.75, numeric_only=False) - \
    df_sub.quantile(0.25, numeric_only=False)
lim3 = np.abs((df_sub - df_sub.median()) / iqr) < 2.22


# replace outliers with nan
#df.loc[:, cols] = df_sub.where(lim1, np.nan)

# Outlier indexes for z-score
print(lim1.index[lim1['age'] == False].tolist())

# Outlier indexes for quantile-score
print(lim2.index[lim2['age'] == False].tolist())

# Outlier indexes for qr filter
print(lim3.index[lim3['age'] == False].tolist())
