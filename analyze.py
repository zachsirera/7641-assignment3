# This is the main driver code for GT CS 7641 - Unsupervized Learning and Dimensionality Reduction
# Zach Sirera - Fall 2020

# import the necessary external libraries
from sklearn import metrics 

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, FastICA, TruncatedSVD
from sklearn.random_projection import johnson_lindenstrauss_min_dim, GaussianRandomProjection
from sklearn.neural_network import MLPClassifier

from scipy.spatial.distance import cdist 
from scipy.stats import kurtosis

from collections import Counter

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


def apply_kmeans(train_x, n, algo):

	classifier = KMeans(n_clusters = n, random_state = 0, algorithm = algo)
	classifier.fit_predict(train_x)

	return classifier


def apply_em(train_x, n, covariance_type):
	''' ''' 

	classifier = GaussianMixture(n_components = n, covariance_type = covariance_type, tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans', 
				weights_init=None, means_init=None, precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10)
	labels = classifier.fit_predict(train_x)

	return labels


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

	for i in range(1, n, 10):

		for j in range(1, 11):

			error = 0

			rand_proj = GaussianRandomProjection(n_components=n)
			reduced_df = rand_proj.fit_transform(train_x)
			
			psuedo_inverse = np.linalg.pinv(rand_proj.components_.T)
			reconstructed = reduced_df.dot(psuedo_inverse)

			error += metrics.mean_squared_error(train_x, reconstructed)
			# # error = (np.linalg.norm(train_x - reconstructed) ** 2) / len(train_x)
			# # error = np.sum(np.square(train_x - reconstructed))
			# error = np.mean((train_x - reconstructed)**2)
			# error =  ((train_x - reconstructed) ** 2).sum(1).mean()
		
		results.append({"n_components": i, "reconstruction_error": error / 10})


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


def simple_nn(train_x, train_y, test_x, test_y): 

	classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6), random_state=1)
	classifier.fit(train_x, train_y)

	predictions = classifier.predict(test_x)
	print(metrics.classification_report(test_y.values.ravel(), predictions, zero_division=0))


def apply_nn(train_x, train_y, test_x, test_y): 
	''' ''' 

	algs = ['none', 'pca', 'ica', 'rp', 'svd']
	results = []

	train_pca_projection = pca_proj(train_x, 6)
	train_ica_projection = ica_proj(train_x, 3)
	train_rp_projection = rand_proj(train_x, 6)
	train_svd_projection = svd_proj(train_x, 2)


	all_train_projections = [train_x, train_pca_projection, train_ica_projection, train_rp_projection, train_svd_projection] # 

	test_pca_projection = pca_proj(test_x, 6)
	test_ica_projection = ica_proj(test_x, 3)
	test_rp_projection = rand_proj(test_x, 6)
	test_svd_projection = svd_proj(test_x, 2)

	all_test_projections = [test_x, test_pca_projection, test_ica_projection, test_rp_projection, test_svd_projection] # 

	for index, train_projection in enumerate(all_train_projections):

		classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6), random_state=1, max_iter=10000)
		fit_start = time.time()
		classifier.fit(train_projection, train_y.values.ravel())
		fit_end = time.time() - fit_start
		predictions = classifier.predict(all_test_projections[index])

		print(algs[index])
		print(metrics.classification_report(test_y.values.ravel(), predictions, zero_division=0))

		count = 0
		correct = 0

		for jindex, prediction in enumerate(predictions):
			if prediction == test_y.values.ravel()[jindex]:
				correct += 1

			count += 1

		results.append({'alg': algs[index], 'accuracy': correct / count, 'training_time': fit_end, "iterations": classifier.n_iter_})

	return results


def apply_kmeans_nn(train_x, train_y, test_x, test_y):
	''' ''' 

	algs = ['none', 'pca', 'ica', 'rp', 'svd']
	cluster_params = [{'n_clusters': 5, 'algorithm': 'full'}, {'n_clusters': 10, 'algorithm': 'elkan'}, {'n_clusters': 7, 'algorithm': 'full'}, {'n_clusters': 2, 'algorithm': 'elkan'}]
	results = []

	train_pca_projection = pca_proj(train_x, 6)
	train_ica_projection = ica_proj(train_x, 3)
	train_rp_projection = rand_proj(train_x, 6)
	train_svd_projection = svd_proj(train_x, 2)

	all_train_projections = [train_pca_projection, train_ica_projection, train_rp_projection, train_svd_projection]
	full_train = [train_x] + [np.append(projection, pd.get_dummies(apply_kmeans(projection, cluster_params[index]['n_clusters'], cluster_params[index]['algorithm']).labels_).values, axis=1) for index, projection in enumerate(all_train_projections)]

	test_pca_projection = pca_proj(test_x, 6)
	test_ica_projection = ica_proj(test_x, 3)
	test_rp_projection = rand_proj(test_x, 6)
	test_svd_projection = svd_proj(test_x, 2)

	all_test_projections = [test_pca_projection, test_ica_projection, test_rp_projection, test_svd_projection]
	full_test = [test_x] + [np.append(projection, pd.get_dummies(apply_kmeans(projection, cluster_params[index]['n_clusters'], cluster_params[index]['algorithm']).labels_).values, axis=1) for index, projection in enumerate(all_test_projections)]


	for index, projection in enumerate(full_train):

		classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6), random_state=1, max_iter=10000)
		fit_start = time.time()
		classifier.fit(projection, train_y.values.ravel())
		fit_end = time.time() - fit_start
		predictions = classifier.predict(full_test[index])

		print(algs[index])
		print(metrics.classification_report(test_y.values.ravel(), predictions, zero_division=0))

		count = 0
		correct = 0

		for jindex, prediction in enumerate(predictions):
			if prediction == test_y.values.ravel()[jindex]:
				correct += 1

			count += 1

		results.append({'alg': algs[index], 'accuracy': correct / count, 'training_time': fit_end, "iterations": classifier.n_iter_})

	return results


def apply_em_nn(train_x, train_y, test_x, test_y):
	''' ''' 

	algs = ['none', 'pca', 'ica', 'rp', 'svd']
	cluster_params = [{'n_clusters': 2, 'covariance_type': 'full'}, {'n_clusters': 7, 'covariance_type': 'full'}, {'n_clusters': 2, 'covariance_type': 'full'}, {'n_clusters': 2, 'covariance_type': 'diag'}]

	results = []

	train_pca_projection = pca_proj(train_x, 6)
	train_ica_projection = ica_proj(train_x, 3)
	train_rp_projection = rand_proj(train_x, 6)
	train_svd_projection = svd_proj(train_x, 2)

	all_train_projections = [train_pca_projection, train_ica_projection, train_rp_projection, train_svd_projection]
	full_train = [train_x] + [np.append(projection, pd.get_dummies(apply_em(projection, cluster_params[index]['n_clusters'], cluster_params[index]['covariance_type'])).values, axis=1) for index, projection in enumerate(all_train_projections)]

	test_pca_projection = pca_proj(test_x, 6)
	test_ica_projection = ica_proj(test_x, 3)
	test_rp_projection = rand_proj(test_x, 6)
	test_svd_projection = svd_proj(test_x, 2)

	all_test_projections = [test_pca_projection, test_ica_projection, test_rp_projection, test_svd_projection]
	full_test = [test_x] + [np.append(projection, pd.get_dummies(apply_em(projection, cluster_params[index]['n_clusters'], cluster_params[index]['covariance_type'])).values, axis=1) for index, projection in enumerate(all_test_projections)]


	for index, projection in enumerate(full_train):

		classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6), random_state=1, max_iter=10000)
		fit_start = time.time()
		classifier.fit(projection, train_y.values.ravel())
		fit_end = time.time() - fit_start
		predictions = classifier.predict(full_test[index])

		print(algs[index])
		print(metrics.classification_report(test_y.values.ravel(), predictions, zero_division=0))

		count = 0
		correct = 0

		for jindex, prediction in enumerate(predictions):
			if prediction == test_y.values.ravel()[jindex]:
				correct += 1

			count += 1

		results.append({'alg': algs[index], 'accuracy': correct / count, 'training_time': fit_end, "iterations": classifier.n_iter_})

	return results

	
def tune_nn(train_x, train_y, test_x, test_y):
	''' ''' 

	results = []

	train_pca_projection = pca_proj(train_x, 6)
	full_train = np.append(train_pca_projection, pd.get_dummies(apply_em(train_pca_projection, 2, "full")).values, axis=1)

	test_pca_projection = pca_proj(test_x, 6)
	full_test = np.append(test_pca_projection, pd.get_dummies(apply_em(test_pca_projection, 2, "full")).values, axis=1)

	print(full_train.shape)

	for i in range(1, 10):
		for j in range(1, 10):


			classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(i, j), random_state=1, max_iter=10000)
			fit_start = time.time()
			classifier.fit(full_train, train_y.values.ravel())
			fit_end = time.time() - fit_start
			predictions = classifier.predict(full_test)

			# print(metrics.classification_report(test_y.values.ravel(), predictions, zero_division=0))

			count = 0
			correct = 0

			for jindex, prediction in enumerate(predictions):
				if prediction == test_y.values.ravel()[jindex]:
					correct += 1

				count += 1

			results.append({'layer_1': i, 'layer_2': j, 'accuracy': correct / count, 'training_time': fit_end, "iterations": classifier.n_iter_})


	return results

def count_labels(train_y, test_y):

	all_data = train_y.append(test_y)

	hist = all_data.hist()
	plt.show()

def svd_plots_adult(train_x, train_t):

	svd = TruncatedSVD(n_components=2, algorithm="randomized")
	reduced_df = svd.fit_transform(train_x.astype("float"))

	principal_df = pd.DataFrame(data = reduced_df, columns = ['principal_component_' + str(i) for i in range(1, 2+1)])

	principal_df['label'] = train_y

	colors = ['r', 'g']

	list_data = principal_df.dropna().to_dict('records')

	for i in range(len(list_data)):
		plt.plot(list_data[i]['principal_component_1'], list_data[i]['principal_component_2'], marker='o', c=colors[int(list_data[i]['label'])])

	plt.title("SVD: Adult \n Two Components")
	plt.xlabel("Principal Component 1")
	plt.ylabel("Principal Component 2")
	plt.tight_layout()
	plt.savefig("figures/svd_adult_2")
	plt.cla()

def ica_plots_adult(train_x, train_t):

	rp = FastICA(n_components = 2)
	reduced_df = rp.fit_transform(train_x)

	principal_df = pd.DataFrame(data = reduced_df, columns = ['principal_component_' + str(i) for i in range(1, 2+1)])

	principal_df['label'] = train_y

	colors = ['r', 'g']

	list_data = principal_df.dropna().to_dict('records')

	for i in range(len(list_data)):
		plt.plot(list_data[i]['principal_component_1'], list_data[i]['principal_component_2'], marker='o', c=colors[int(list_data[i]['label'])])

	plt.title("ICA: Adult \n Two Components")
	plt.xlabel("Principal Component 1")
	plt.ylabel("Principal Component 2")
	plt.tight_layout()
	plt.savefig("figures/ica_adult_2")
	plt.cla()

def ica_plots_wine(train_x):
	
	rp = FastICA(n_components = 3)
	reduced_df = rp.fit_transform(train_x)

	principal_df = pd.DataFrame(data = reduced_df, columns = ['principal_component_' + str(i) for i in range(1, 3+1)])

	principal_df['label'] = train_y


	colors = ['r', 'g', 'b', 'c', 'y', 'k', 'm']

	list_data = principal_df.dropna().to_dict('records')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	for i in range(len(list_data)):
		x = list_data[i]['principal_component_1']
		y = list_data[i]['principal_component_2']
		z = list_data[i]['principal_component_3']

		ax.plot(x, y, z, marker='o', c=colors[int(list_data[i]['label']) - 3])

	plt.title("ICA: Wine \n Three Components")
	ax.set_xlabel('Principal Component 1')
	ax.set_ylabel('Principal Component 2')
	ax.set_zlabel('Principal Component 3')
	plt.tight_layout()
	plt.savefig("figures/ica_wine_3")
	plt.cla()


def svd_plots_wine(train_x):
	
	svd = TruncatedSVD(n_components=2, algorithm="randomized")
	reduced_df = svd.fit_transform(train_x.astype("float"))

	principal_df = pd.DataFrame(data = reduced_df, columns = ['principal_component_' + str(i) for i in range(1, 2+1)])

	principal_df['label'] = train_y

	colors = ['r', 'g', 'b', 'c', 'y', 'k', 'm']


	list_data = principal_df.dropna().to_dict('records')

	for i in range(len(list_data)):
		plt.plot(list_data[i]['principal_component_1'], list_data[i]['principal_component_2'], marker='o', c=colors[int(list_data[i]['label']) - 3])

	plt.title("SVD: Wine \n Two Components")
	plt.xlabel("Principal Component 1")
	plt.ylabel("Principal Component 2")
	plt.tight_layout()
	plt.savefig("figures/svd_wine_2")
	plt.cla()

def get_pca_wine_eigenvalues(train_x): 
	''' ''' 

	results = []

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)
	cov_matr = np.cov(scaled)

	eig_vals, eig_vecs = np.linalg.eig(cov_matr)

	return eig_vals.tolist()

	# plt.hist(eig_vals)
	# plt.title("Wine (PCA)")
	# plt.xlabel("Eigenvalues")
	# plt.savefig("figures/wine_pca_eig")
	# plt.cla()

def get_pca_adult_eigenvalues(train_x): 
	''' ''' 

	results = []

	# Extract the feature names from the dataframe
	features = train_x.columns
	x = train_x.loc[:, features].values

	# Apply the standard scaler to the dataframe. PCA expects this. 
	scaled = StandardScaler().fit_transform(x)
	cov_matr = np.cov(scaled)

	eig_vals, eig_vecs = np.linalg.eig(cov_matr)

	return eig_vals.tolist()

	# plt.hist(eig_vals)
	# plt.title("Adult (PCA)")
	# plt.xlabel("Eigenvalues")
	# plt.savefig("figures/adult_pca_eig")
	# plt.cla()





if __name__ == '__main__':
	# Adult Dataset
	train_x, train_y, test_x, test_y = data_adult.main('adult_data.csv')
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
	# print(rand_proj) # min occurs around 11
	# rp_reduced = rand_proj(train_x, 7)
	# print(kmeans(rp_reduced, 10))
	# print(expectation_max(rp_reduced, 20))
	# print(apply_svd(train_x, 10)) # explained variance occurs at 1 component, either algorithm
	# svd_reduced = svd_proj(train_x, 1)
	# print(kmeans(svd_reduced, 10))
	# print(expectation_max(svd_reduced, 10))
	# print(count_labels(train_y, test_y))
	# svd_plots_adult(train_x, train_y)
	# ica_plots_adult(train_x, train_y)
	print(get_pca_adult_eigenvalues(train_x))


	# Wine Dataset
	# train_x, train_y, test_x, test_y = data_wine.main('winequality-white.csv')
	# # print(kmeans(train_x, 20))
	# # print(expectation_max(train_x, 20))
	# print(apply_PCA(train_x, 10))
	# pca_wine = pca_proj(train_x, 6)
	# # print(pca_wine.shape)
	# pca_projection()
	# print(kmeans(pca_wine, 10))
	# print(expectation_max(pca_wine, 10))
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
	# print(apply_nn(train_x, train_y, test_x, test_y))
	# print(apply_kmeans_nn(train_x, train_y, test_x, test_y))
	# print(apply_em_nn(train_x, train_y, test_x, test_y))
	# print(tune_nn(train_x, train_y, test_x, test_y))
	# ica_plots_wine(train_x)
	# svd_plots_wine(train_x)
	# simple_nn(train_x, train_y, test_x, test_y)
	# print(get_pca_wine_eigenvalues(train_x))

	pass 





