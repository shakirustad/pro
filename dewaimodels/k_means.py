from sklearn.datasets import load_sample_image
from matplotlib import pyplot as plt
import numpy as np

china = load_sample_image("china.jpg")
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(china)

print(china.shape)
print("testing1")
data = china
data = data.reshape(427 * 640, 3)
print(data.shape)
print("testing2")

def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data

    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    #colors = colors[i]
    R, G, B = data[i].T
    print("testing_3")

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    # ax[0].scatter(R, G, color =colors, marker='.')
    # ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))
    print("testing_4")
    ax[0].scatter(R, B, c=colors[i], marker='.')
    ax[0].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title, size=20);

plot_pixels(data, title='Input color space: 16 million possible colors')
plt.show()


import warnings;

warnings.simplefilter('ignore')

from sklearn.cluster import MiniBatchKMeans

kmeans = MiniBatchKMeans(16)
kmeans.fit(data)

new_colors = kmeans.cluster_centers_[kmeans.predict(data)]
plot_pixels(data, colors=new_colors, title=' reduced color space: 16 colors')

plt.show()
china_recolored = new_colors.reshape(china.shape)

fig, ax = plt.subplot(1, 2, figsize=(16, 6), sub_plot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(china)
ax[0].set_title('original_image', size=16)

ax[0].imshow(china_recolored)
ax[0].set_title('original_image', size=16)
plt.show()
