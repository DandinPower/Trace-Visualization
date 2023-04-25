import pandas as pd
import numpy as np

data = pd.read_csv('trace/target_MSR_mds_0.csv', header=None, dtype=np.int64)

filtered_data = data.loc[data.iloc[:, 4] == 0]

filtered_data.to_csv('filtered_data.csv', index=False)