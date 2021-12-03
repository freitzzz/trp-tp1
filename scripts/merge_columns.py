import pandas as pd
import sys

args = sys.argv

csv_file_path = args[1]

merged_csv_file_path = args[2]

index_of_column_a = int(args[3])
index_of_column_b = int(args[4])

merged_column_label = args[5]

operation_mode = args[6]

data = pd.read_csv(csv_file_path)


merged_data_column = data[data.columns[index_of_column_a]] + \
    (data[data.columns[index_of_column_b]]
     * (-1 if operation_mode == 'sub' else 1))


merged_data = data.drop(data.columns[index_of_column_a], axis=1).drop(
    data.columns[index_of_column_b], axis=1)

merged_data.insert(index_of_column_a, merged_column_label, merged_data_column)

merged_data.to_csv(merged_csv_file_path, index=False)
