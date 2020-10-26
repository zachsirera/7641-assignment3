# This is the main driver code for GT CS 7641 - Unsupervized Learning and Dimensionality Reduction
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import metrics 
from scipy.spatial.distance import cdist 
import numpy as np 
import time

# import files from the project directory
import data_adult
import data_wine


def kmeans(train_x, test_x, clusters_max):
	''' ''' 

	results = []
	algos = ["full", "elkan"]


	for i in range(2, clusters_max):

		for algo in algos:

			classifier = KMeans(n_clusters = i, random_state = 0, algorithm = algo)
			fit_start = time.time()
			cluster_labels = classifier.fit_predict(train_x)
			fit_end = time.time() - fit_start

			silhouette = metrics.silhouette_score(train_x, cluster_labels)
			distortion = sum(np.min(cdist(train_x, classifier.cluster_centers_, 'euclidean'), axis=1)) / train_x.shape[0]
			inertia = classifier.inertia_

			results.append({"n_clusters": i, "algorithm": algo, "silhouette_score": silhouette, "training_time": fit_end, "distortion": distortion, "inertia": inertia})



	return results


	
	

def expectation_max(train_x, test_x):
	''' '''
	classifier = GaussianMixture(n_components=1, covariance_type='full', tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans', 
		weights_init=None, means_init=None, precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10)
	fit_start = time.time()
	classifier.fit(train_x)
	fit_end = time.time() - fit_start



	return classifier.predict(test_x)


if __name__ == '__main__':
	# Adult Dataset
	# train_x, train_y, test_x, test_y = data_adult.main('adult_data.csv')
	# print(kmeans(train_x, test_x, 10))
	# print(expectation_max(train_x, test_x).shape)



	# Wine Dataset
	train_x, train_y, test_x, test_y = data_adult.main('winequality-white.csv')
	print(kmeans(train_x, test_x, 10))






