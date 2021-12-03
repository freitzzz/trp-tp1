import pandas as pd
import sys

args = sys.argv

csv_file_path = args[1]

data = pd.read_csv(csv_file_path)

unique_columns_data = [data[data.columns[x]].unique()
                       for x in range(0, len(data.columns))]

for unique_column_data in unique_columns_data:
    print(unique_column_data.tolist())
