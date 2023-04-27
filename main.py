import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from lba_dict import GetLbaFreqDict

data = pd.read_csv('trace/target_MSR_mds_0.csv', header=None, dtype=np.float64).values
Y = np.array(data[:, 4], dtype=np.int32)


lba_standardized_frequencies = GetLbaFreqDict()
Lbas = data[:, 2].copy()
# Replace the LBA values in the data array with standardized frequency values
for i in range(len(Lbas)):
    index = str(Lbas[i])
    if index in lba_standardized_frequencies:
        Lbas[i] = lba_standardized_frequencies[index]

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


df = pd.DataFrame({'Lba': Lbas, 'LbaDiff': LbaDiff, 'NumBytes': NumBytes, 'Y': Y})
sns.pairplot(df, hue='Y')
plt.savefig('image/feature_distribution.png', dpi=300)
plt.clf()