# This is the main driver code for GT CS 7641 - Unsupervized Learning and Dimensionality Reduction
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import metrics 

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, FastICA, TruncatedSVD
from sklearn.random_projection import johnson_lindenstrauss_min_dim, GaussianRandomProjection

from scipy.spatial.distance import cdist 
from scipy.stats import kurtosis

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


def apply_PCA(train_x, n):
	''' ''' 

	results = []

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)

	for i in range(1, n):
		pca = PCA(n_components = i)
		reduced_df = pca.fit_transform(scaled)

		psuedo_inverse = np.linalg.pinv(pca.components_.T)
		reconstructed = reduced_df.dot(psuedo_inverse)

		error = metrics.mean_squared_error(scaled, reconstructed)

		results.append({"n_components": i, "reconstruction_error": error})


	return results
	
	




def pca_proj(train_x, n):
	''' ''' 

	rp = PCA(n_components = n)
	reduced_df = rp.fit_transform(train_x)

	return reduced_df



def ica_proj(train_x, n):
	''' ''' 

	rp = FastICA(n_components = n)
	reduced_df = rp.fit_transform(train_x)

	return reduced_df



def apply_ICA(train_x):
	''' ''' 

	results = []
	algorithms = ['parallel', 'deflation']

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)

	for algorithm in algorithms:
		for i in range(1, 10):
			ica = FastICA(n_components=i, algorithm=algorithm)
			independent_components = ica.fit_transform(scaled)
			independent_df = pd.DataFrame(data = independent_components, columns = ['independent_component_' + str(i) for i in range(1, independent_components.shape[1] + 1)])

			kurt = independent_df.kurtosis(axis=0).mean()

			results.append({'n_components': i, 'algorithm': algorithm, 'avg_kurtosis': kurt})

	return results



def rand_proj_reconstruction_error(train_x, n):
	''' '''

	results = [] 

	for i in range(1, n):

		rand_proj = GaussianRandomProjection(n_components=n)
		reduced_df = rand_proj.fit_transform(train_x)
		
		psuedo_inverse = np.linalg.pinv(rand_proj.components_.T)
		reconstructed = reduced_df.dot(psuedo_inverse)

		error = metrics.mean_squared_error(train_x, reconstructed)
		# # error = (np.linalg.norm(train_x - reconstructed) ** 2) / len(train_x)
		# # error = np.sum(np.square(train_x - reconstructed))
		# error = np.mean((train_x - reconstructed)**2)
		# error =  ((train_x - reconstructed) ** 2).sum(1).mean()
	
		results.append({"n_components": i, "reconstruction_error": error})


	return results


def rand_proj(train_x, n):
	''' ''' 

	rp = GaussianRandomProjection(n_components = n)
	reduced_df = rp.fit_transform(train_x)

	return reduced_df


def apply_svd(train_x, n):

	results = []

	algorithms = ['randomized', 'arpack']

	for algorithm in algorithms:
		svd = TruncatedSVD(n_components=n, algorithm=algorithm)
		svd.fit_transform(train_x.astype("float"))

		results.append({'algorithm': algorithm, 'n_components': n, 'explained_variance': list(svd.explained_variance_ratio_)})

	return results

def svd_proj(train_x, n):
	''' ''' 

	svd = TruncatedSVD(n_components=n)
	reduced_df = svd.fit_transform(train_x.astype("float"))

	return reduced_df






if __name__ == '__main__':
	# Adult Dataset
	# train_x, train_y, test_x, test_y = data_adult.main('adult_data.csv')
	# print(type(train_x))
	# print(kmeans(train_x, 10))
	# print(expectation_max(train_x, 20))
	# print(apply_PCA(train_x, 100)) ### 71 components because <20% reconstruction error
	# pca_projection = pca_proj(train_x, 71)
	# print(kmeans(pca_projection, 10))
	# print(expectation_max(pca_projection, 10))
	# ica_adult = apply_ICA(train_x) ## Kurtosis of 0 occurs around 2 components 
	# print(ica_adult)
	# ica_projection = ica_proj(train_x, 2)
	# print(kmeans(ica_projection, 20)) ## 2 clusters has a great silhouette score
	# print(expectation_max(ica_projection, 20))
	# rand_proj = rand_proj_reconstruction_error(train_x, 100)
	# print(rand_proj) # min occurs around 7
	# rp_reduced = rand_proj(train_x, 7)
	# print(kmeans(rp_reduced, 10))
	# print(expectation_max(rp_reduced, 20))
	# print(apply_svd(train_x, 10)) # explained variance occurs at 1 component, either algorithm
	# svd_reduced = svd_proj(train_x, 1)
	# print(kmeans(svd_reduced, 10))
	# print(expectation_max(svd_reduced, 10))



	# Wine Dataset
	train_x, train_y, test_x, test_y = data_wine.main('winequality-white.csv')
	# # print(kmeans(train_x, 20))
	# # print(expectation_max(train_x, 20))
	# print(apply_PCA(train_x, 10))
	pca_wine = pca_proj(train_x, 6)
	# # print(pca_wine.shape)
	# pca_projection()
	print(kmeans(pca_wine, 10))
	print(expectation_max(pca_wine, 10))
	# ica_wine = apply_ICA(train_x) ### kurtosis of 0 doesn't occur, 1 to 3 all around 1. 
	# print(ica_wine)
	# ica_projection = ica_proj(train_x, 2)
	# print(kmeans(ica_projection, 20))
	# print(expectation_max(ica_projection, 20))
	# rand_proj = rand_proj_reconstruction_error(train_x, 10) 
	# print(rand_proj) # min occurs around 4
	# rp_reduced = rand_proj(train_x, 4)
	# print(kmeans(rp_reduced, 20))
	# print(expectation_max(rp_reduced, 20))
	# print(apply_svd(train_x, 9)) # explained variance occurs at 2 components, either algorithm
	# svd_reduced = svd_proj(train_x, 2)
	# print(kmeans(svd_reduced, 10))
	# print(expectation_max(svd_reduced, 10))


	pass 





