import pandas as pd  
import numpy as np  

df = pd.read_csv('D:/Lê Văn Hà B22DCCN255/Thư mục code/result.csv', header=2)
data = df[df.columns[4:]].copy()
data = data.apply(pd.to_numeric, errors='coerce').fillna(0)
data.dropna(axis='columns', inplace=True)



data = ((data - data.min()) / (data.max() - data.min())) * 9 + 1




def random_centroids(data, k): 
    centroids = [] 
    for _ in range(k): 
        centroid = data.apply(lambda x: float(x.sample().iloc[0])) 
        centroids.append(centroid)  
    return pd.concat(centroids, axis=1)  



def get_labels(data, centroids): 
    distances = centroids.apply(lambda x: np.sqrt(((data - x) ** 2).sum(axis=1)))  
    return distances.idxmin(axis=1)



def new_centroids(data, labels, k):
    centroids = data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T
    return centroids  



from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 
from IPython.display import clear_output 
import time 



def plot_clusters(data, labels, centroids, iteration):
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data)
    centroids_2d = pca.transform(centroids.T)
    time.sleep(1)
    clear_output(wait=True)
    plt.title(f'Iteration {iteration}')
    plt.scatter(x=data_2d[:,0], y=data_2d[:,1], c=labels)
    plt.scatter(x=centroids_2d[:,0], y=centroids_2d[:,1])
    plt.savefig(r"D:\Lê Văn Hà B22DCCN255\Thư mục hình vẽ\kmeans_pca.png")
    plt.show()



# Khởi tạo K-Means
max_iterations = 100
k = 3

centroids = random_centroids(data, k)
old_centroids = pd.DataFrame()
iteration = 1

while iteration < max_iterations:
    labels = get_labels(data, centroids)
    centroids = new_centroids(data, labels, k)

    # Vẽ biểu đồ chỉ khi centroids không thay đổi
    if centroids.equals(old_centroids):
        plot_clusters(data, labels, centroids, iteration)

    # Cập nhật old_centroids
    old_centroids = centroids
    iteration += 1



