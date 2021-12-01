import pandas as pd
import sys

args = sys.argv

csv_file_path = args[1]

index_table_csv_file_path = args[2]

index_of_column_to_map = int(args[3])

data = pd.read_csv(csv_file_path)

unique_column_to_map_data = data[data.columns[index_of_column_to_map]].unique()

index_table_dict = {
    'index': [],
    'value': []
}

index = 0

for value in unique_column_to_map_data:
    index_table_dict['index'].append(index)
    index_table_dict['value'].append(value)
    index += 1

pd.DataFrame(index_table_dict).to_csv(index_table_csv_file_path, index=False)
