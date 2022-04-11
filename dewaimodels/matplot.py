from matplotlib import pyplot as plt
from matplotlib import axes
import pandas as pd
test = pd.DataFrame({'cluster':["0", "1", "2"],
                     'x':[2,3,1],
                     'y':[10,5,1],
                     'z':[-10,-5, 2]})
fig = plt.figure(figsize=(7,7))
ax= plt.axes(fig)
x=test['x']
y=test['y']
z=test['z']
clusters = test['cluster']

ax.scatter(x,y,z, c=clusters, marker='x', cmap= 'tab20b', depthshade =False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()