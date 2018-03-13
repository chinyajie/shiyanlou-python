import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
data = pd.read_json("user_study.json")
print(data)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
y = data[['user_id','minutes']].groupby('user_id').sum()['minutes']
x = np.arange(0, len(y), 1)

ax.set_title('StudyData')
ax.plot(x, y)




plt.show()
