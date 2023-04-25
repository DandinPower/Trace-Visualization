import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('trace/target_MSR_mds_0.csv', header=None, dtype=np.float64).values
Y = np.array(data[:, 4], dtype=np.int32)

# Transfer col lba into lba_diff
data[1:, 2] = np.diff(data[:, 2])
data[0, 2] = 0
LbaDiff = data[:, 2]

# Standardize x data (lba_diff)
scaler_diff = StandardScaler()
LbaDiff = scaler_diff.fit_transform(data[:, 2].reshape(-1, 1)).flatten()

NumBytes = data[:, 3]

# Standardize x data (bytes)
scaler_bytes = StandardScaler()
NumBytes = scaler_bytes.fit_transform(data[:, 3].reshape(-1, 1)).flatten()


df = pd.DataFrame({'LbaDiff': LbaDiff, 'NumBytes': NumBytes, 'Y': Y})
sns.pairplot(df, hue='Y')
plt.savefig('test.png')
plt.clf()