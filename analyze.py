# This is the main driver code for GT CS 7641 - Unsupervized Learning and Dimensionality Reduction
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import metrics 

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, FastICA

from scipy.spatial.distance import cdist 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import time

# import files from the project directory
import data_adult
import data_wine
import plot


def kmeans(train_x, clusters_max):
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


	
	

def expectation_max(train_x, n_components):
	''' '''

	results = []
	covariances = ['full', 'tied', 'diag', 'spherical'] # 

	for covariance_type in covariances:

		for i in range(1, n_components):

			classifier = GaussianMixture(n_components=i, covariance_type=covariance_type, tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans', 
				weights_init=None, means_init=None, precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10)
			fit_start = time.time()
			cluster_labels = classifier.fit(train_x)
			fit_end = time.time() - fit_start

			results.append({"n_components": i, "covariance": covariance_type, "training_time": fit_end, "bic": classifier.bic(train_x), "aic": classifier.aic(train_x)})



	return results


def apply_PCA(train_x, train_y, n):
	''' ''' 

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)

	if n == 2: 
		pca = PCA(n_components=2)
		principalComponents = pca.fit_transform(scaled)

		principal_df = pd.DataFrame(data = principalComponents, columns = ['principal_component_' + str(i) for i in range(1, n+1)])

		principal_df['label'] = train_y

		plot.PCA_adult_2(principal_df)

		return principal_df

	elif n == 3: 
		pca = PCA(n_components=3)
		principalComponents = pca.fit_transform(scaled)

		principal_df = pd.DataFrame(data = principalComponents, columns = ['principal_component_' + str(i) for i in range(1, n+1)])

		principal_df['label'] = train_y

		plot.PCA_adult_3(principal_df)

		return principal_df

	else: 
		pca = PCA(.95)
		principalComponents = pca.fit_transform(scaled)
		principal_df = pd.DataFrame(data = principalComponents, columns = ['principal_component_' + str(i) for i in range(1, principalComponents.shape[1] + 1)])


		return principal_df



def apply_ICA(train_x):
	''' ''' 

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)


	ica = FastICA(n_components=10)
	independent_components = ica.fit_transform(scaled)
	independent_df = pd.DataFrame(data = independent_components, columns = ['independent_component_' + str(i) for i in range(1, independent_components.shape[1] + 1)])


	return independent_df





if __name__ == '__main__':
	# Adult Dataset
	train_x, train_y, test_x, test_y = data_adult.main('adult_data.csv')
	# print(kmeans(train_x, 10))
	# print(expectation_max(train_x, 20))
	# apply_PCA(train_x, train_y, 3)
	pca_adult = apply_PCA(train_x, train_y, 4)
	# print(pca_adult.shape)
	# print(kmeans(pca_adult, 200))
	print(expectation_max(pca_adult, 20))
	# ica_adult = apply_ICA(train_x)
	# print(kmeans(ica_adult, 20))
	# print(expectation_max(ica_adult, 20))





	# Wine Dataset
	# train_x, train_y, test_x, test_y = data_wine.main('winequality-white.csv')
	# # print(kmeans(train_x, 20))
	# # print(expectation_max(train_x, 20))
	# # pca_wine = apply_PCA(train_x, train_y, 4)
	# # print(pca_wine.shape)
	# print(kmeans(pca_wine, 200))
	# print(expectation_max(pca_wine, 20))
	# ica_wine = apply_ICA(train_x)
	# print(kmeans(ica_wine, 20))
	# print(expectation_max(ica_wine, 20))







