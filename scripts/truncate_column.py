import pandas as pd
import sys

args = sys.argv

csv_file_path = args[1]

truncated_csv_file_path = args[2]

index_of_column_to_truncate = int(args[3])

data = pd.read_csv(csv_file_path)

truncated_data = data.drop(data.columns[index_of_column_to_truncate], axis=1)

truncated_data.to_csv(truncated_csv_file_path, index=False)
