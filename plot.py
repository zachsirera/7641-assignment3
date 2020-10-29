import matplotlib.lines as mlines
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np

def kmeans_adult():
	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5865223038402563, 'training_time': 1.166788101196289, 'distortion': 52751.567453108786, 'inertia': 121826826751721.27}, 
	{'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5865223038402563, 'training_time': 0.8215968608856201, 'distortion': 52751.567453108786, 'inertia': 121826826751721.27}, 
	{'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5517669524863584, 'training_time': 1.1698510646820068, 'distortion': 36123.85972711497, 'inertia': 66052939465350.086}, 
	{'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5517669524863584, 'training_time': 0.820457935333252, 'distortion': 36123.85972711497, 'inertia': 66052939465350.086}, 
	{'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5592090387800095, 'training_time': 1.8423190116882324, 'distortion': 31030.119045013977, 'inertia': 43444928215785.375}, 
	{'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5592090387800095, 'training_time': 1.365248203277588, 'distortion': 31030.119045013977, 'inertia': 43444928215785.375}, 
	{'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5333474384235639, 'training_time': 1.9076948165893555, 'distortion': 26610.83601715731, 'inertia': 31290385205421.79}, 
	{'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5333474384235639, 'training_time': 1.3921360969543457, 'distortion': 26610.83601715731, 'inertia': 31290385205421.793}, 
	{'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5430271733428783, 'training_time': 2.576388120651245, 'distortion': 21272.585578471302, 'inertia': 22610836704215.812}, 
	{'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5430271733428783, 'training_time': 1.8347148895263672, 'distortion': 21272.585578471302, 'inertia': 22610836704215.812}, 
	{'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.5448058632628574, 'training_time': 2.4871480464935303, 'distortion': 18849.527875047614, 'inertia': 17176993745185.088}, 
	{'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.5448058632628574, 'training_time': 1.7632479667663574, 'distortion': 18849.527875047614, 'inertia': 17176993745185.088}, 
	{'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5301869497388189, 'training_time': 3.703871250152588, 'distortion': 16708.339629629594, 'inertia': 13884318822915.793}, 
	{'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5301869497388189, 'training_time': 2.5703978538513184, 'distortion': 16708.339629629594, 'inertia': 13884318822915.791}, 
	{'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5311034755426721, 'training_time': 3.5702571868896484, 'distortion': 15537.844633914983, 'inertia': 11060160353585.314}, 
	{'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5311034755426721, 'training_time': 2.554086685180664, 'distortion': 15537.844633914985, 'inertia': 11060160353585.314}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Adult \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Adult \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_elbow')
	plt.cla()




def kmeans_wine():

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5088576530792768, 'training_time': 0.18029999732971191, 'distortion': 24.73301121578461, 'inertia': 3317570.305845764}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5088576530792768, 'training_time': 0.08179306983947754, 'distortion': 24.73301121578461, 'inertia': 3317570.305845764}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.416044002719533, 'training_time': 0.1737961769104004, 'distortion': 20.11095432699167, 'inertia': 2181527.8418932576}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.416044002719533, 'training_time': 0.16067886352539062, 'distortion': 20.11095432699167, 'inertia': 2181527.8418932576}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.3744806902731421, 'training_time': 0.1745309829711914, 'distortion': 17.499588680669596, 'inertia': 1662359.3314866319}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.3744806902731421, 'training_time': 0.17269468307495117, 'distortion': 17.499588680669596, 'inertia': 1662359.3314866319}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.3439980993015658, 'training_time': 0.25998973846435547, 'distortion': 16.035020350302418, 'inertia': 1398726.365979052}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.3439980993015658, 'training_time': 0.246412992477417, 'distortion': 16.035020350302418, 'inertia': 1398726.365979052}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.3127264618811414, 'training_time': 0.2476179599761963, 'distortion': 14.937696048232054, 'inertia': 1239465.9690630068}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.3127264618811414, 'training_time': 0.22252178192138672, 'distortion': 14.937696048232054, 'inertia': 1239465.9690630068}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.3157993858233707, 'training_time': 0.24338078498840332, 'distortion': 14.136018188400632, 'inertia': 1109414.5685694653}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.3157993858233707, 'training_time': 0.24815893173217773, 'distortion': 14.136018188400632, 'inertia': 1109414.5685694653}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.3035499205449552, 'training_time': 0.30432724952697754, 'distortion': 13.60366384537656, 'inertia': 1005405.2218885622}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.3035499205449552, 'training_time': 0.32088398933410645, 'distortion': 13.603663845376563, 'inertia': 1005405.2218885623}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.30170891217100665, 'training_time': 0.2773759365081787, 'distortion': 13.28982920007203, 'inertia': 909706.3476137802}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.30170891217100665, 'training_time': 0.30554890632629395, 'distortion': 13.28982920007203, 'inertia': 909706.3476137802}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.302625497901241, 'training_time': 0.3271012306213379, 'distortion': 12.783804036806234, 'inertia': 821867.101216824}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.302625497901241, 'training_time': 0.38152599334716797, 'distortion': 12.783804036806234, 'inertia': 821867.1012168239}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.30679761696405267, 'training_time': 0.3269460201263428, 'distortion': 12.19847205261005, 'inertia': 752857.8347908347}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.30679761696405267, 'training_time': 0.37319302558898926, 'distortion': 12.19847205261005, 'inertia': 752857.8347908345}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.29801577777823085, 'training_time': 0.32795023918151855, 'distortion': 11.717665012729865, 'inertia': 701756.7408289575}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.29801577777823085, 'training_time': 0.394428014755249, 'distortion': 11.717665012729869, 'inertia': 701756.7408289578}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.29088171061234125, 'training_time': 0.36582517623901367, 'distortion': 11.434420309653301, 'inertia': 660917.958438777}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.29088171061234125, 'training_time': 0.4704110622406006, 'distortion': 11.434420309653301, 'inertia': 660917.9584387771}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.29558772234698727, 'training_time': 0.3533627986907959, 'distortion': 11.059633217741947, 'inertia': 616612.1550589317}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.29558772234698727, 'training_time': 0.39894795417785645, 'distortion': 11.059633217741947, 'inertia': 616612.1550589317}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.29716319706174704, 'training_time': 0.36095213890075684, 'distortion': 10.834744038664125, 'inertia': 583373.8663188692}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.29716319706174704, 'training_time': 0.47913193702697754, 'distortion': 10.834744038664125, 'inertia': 583373.8663188693}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.29568825864820397, 'training_time': 0.40163612365722656, 'distortion': 10.681778442874812, 'inertia': 550498.810916899}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.29568825864820397, 'training_time': 0.5187819004058838, 'distortion': 10.681778442874812, 'inertia': 550498.810916899}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.2923828719884941, 'training_time': 0.40685009956359863, 'distortion': 10.435851180773136, 'inertia': 520986.06610218214}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.2923828719884941, 'training_time': 0.5077300071716309, 'distortion': 10.435851180773136, 'inertia': 520986.0661021822}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.28971144092616824, 'training_time': 0.4256601333618164, 'distortion': 10.160221481626, 'inertia': 494423.84806151764}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.28971144092616824, 'training_time': 0.48012208938598633, 'distortion': 10.160221481625996, 'inertia': 494423.8480615176}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.2802402536560421, 'training_time': 0.38751888275146484, 'distortion': 9.925008881613511, 'inertia': 477117.20900842844}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.2802402536560421, 'training_time': 0.4432098865509033, 'distortion': 9.925008881613511, 'inertia': 477117.20900842844}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Wine \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Wine \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_elbow')
	plt.cla()

def em_adult():
	''' ''' 
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.44460105895996094, 'bic': -5774469.676362746, 'aic': -5823434.206914893}, 
	{'n_components': 2, 'covariance': 'full', 'training_time': 1.8922197818756104, 'bic': -10945403.223188551, 'aic': -11043340.453216862}, 
	{'n_components': 3, 'covariance': 'full', 'training_time': 4.914860010147095, 'bic': -13558177.233583348, 'aic': -13705087.163087822}, 
	{'n_components': 4, 'covariance': 'full', 'training_time': 6.567550897598267, 'bic': -13598041.046190768, 'aic': -13793923.675171405}, 
	{'n_components': 5, 'covariance': 'full', 'training_time': 6.0605268478393555, 'bic': -15206368.91152479, 'aic': -15451224.23998159}, 
	{'n_components': 6, 'covariance': 'full', 'training_time': 10.42217493057251, 'bic': -15863485.789142946, 'aic': -16157313.81707591}, 
	{'n_components': 7, 'covariance': 'full', 'training_time': 12.17871904373169, 'bic': -15954063.529027108, 'aic': -16296864.256436236}, 
	{'n_components': 8, 'covariance': 'full', 'training_time': 9.946491956710815, 'bic': -17436447.512472034, 'aic': -17828220.939357325}, 
	{'n_components': 9, 'covariance': 'full', 'training_time': 16.79282307624817, 'bic': -16968202.5592267, 'aic': -17408948.685588155}, 
	{'n_components': 10, 'covariance': 'full', 'training_time': 14.224200963973999, 'bic': -17506955.537663277, 'aic': -17996674.363500893}, 
	{'n_components': 11, 'covariance': 'full', 'training_time': 21.310129165649414, 'bic': -17069214.86411466, 'aic': -17607906.38942844}, 
	{'n_components': 12, 'covariance': 'full', 'training_time': 21.05184316635132, 'bic': -19019381.927365653, 'aic': -19607046.152155597}, 
	{'n_components': 13, 'covariance': 'full', 'training_time': 21.11690330505371, 'bic': -19049787.424775127, 'aic': -19686424.349041235}, 
	{'n_components': 14, 'covariance': 'full', 'training_time': 32.10809922218323, 'bic': -18946584.419726092, 'aic': -19632194.043468364}, 
	{'n_components': 15, 'covariance': 'full', 'training_time': 31.41608691215515, 'bic': -17927401.214426417, 'aic': -18661983.537644852}, 
	{'n_components': 16, 'covariance': 'full', 'training_time': 50.06889295578003, 'bic': -18571975.561887886, 'aic': -19355530.584582485}, 
	{'n_components': 17, 'covariance': 'full', 'training_time': 57.96249222755432, 'bic': -19145266.214970786, 'aic': -19977793.937141545}, 
	{'n_components': 18, 'covariance': 'full', 'training_time': 62.046610832214355, 'bic': -18728971.276476637, 'aic': -19610471.69812356}, 
	{'n_components': 19, 'covariance': 'full', 'training_time': 40.026890993118286, 'bic': -18386428.844021376, 'aic': -19316901.965144463}, 
	{'n_components': 1, 'covariance': 'tied', 'training_time': 0.39142394065856934, 'bic': -5774469.676362882, 'aic': -5823434.206915029}, 
	{'n_components': 2, 'covariance': 'tied', 'training_time': 1.8434083461761475, 'bic': -6017274.213934254, 'aic': -6067129.157204149}, 
	{'n_components': 3, 'covariance': 'tied', 'training_time': 4.389049768447876, 'bic': -6073015.7536394615, 'aic': -6123761.109627105}, 
	{'n_components': 4, 'covariance': 'tied', 'training_time': 5.489330053329468, 'bic': -6317668.309800801, 'aic': -6369304.078506193}, 
	{'n_components': 5, 'covariance': 'tied', 'training_time': 4.613890171051025, 'bic': -6121766.2344831545, 'aic': -6174292.415906295}, 
	{'n_components': 6, 'covariance': 'tied', 'training_time': 8.80658507347107, 'bic': -6359729.94460103, 'aic': -6413146.538741919}, 
	{'n_components': 7, 'covariance': 'tied', 'training_time': 12.891736030578613, 'bic': -6797700.254549426, 'aic': -6852007.261408064}, 
	{'n_components': 8, 'covariance': 'tied', 'training_time': 14.271899938583374, 'bic': -6711503.941806639, 'aic': -6766701.361383025}, 
	{'n_components': 9, 'covariance': 'tied', 'training_time': 16.89057993888855, 'bic': -6943478.226737649, 'aic': -6999566.059031784}, 
	{'n_components': 10, 'covariance': 'tied', 'training_time': 16.65296721458435, 'bic': -6947113.881294337, 'aic': -7004092.12630622}, 
	{'n_components': 11, 'covariance': 'tied', 'training_time': 18.378248929977417, 'bic': -6948235.823922033, 'aic': -7006104.481651665}, 
	{'n_components': 12, 'covariance': 'tied', 'training_time': 22.67099642753601, 'bic': -6804098.587725962, 'aic': -6862857.658173341}, 
	{'n_components': 13, 'covariance': 'tied', 'training_time': 21.828579664230347, 'bic': -7248309.580633055, 'aic': -7307959.063798184}, 
	{'n_components': 14, 'covariance': 'tied', 'training_time': 22.33247208595276, 'bic': -7021752.956243777, 'aic': -7082292.852126653}, 
	{'n_components': 15, 'covariance': 'tied', 'training_time': 28.323994874954224, 'bic': -7488093.691751296, 'aic': -7549524.000351921}, 
	{'n_components': 16, 'covariance': 'tied', 'training_time': 27.116087198257446, 'bic': -7862807.090152909, 'aic': -7925127.8114712825}, 
	{'n_components': 17, 'covariance': 'tied', 'training_time': 31.734958171844482, 'bic': -7413527.549971835, 'aic': -7476738.684007957}, 
	{'n_components': 18, 'covariance': 'tied', 'training_time': 30.536468982696533, 'bic': -7678619.796492406, 'aic': -7742721.3432462765}, 
	{'n_components': 19, 'covariance': 'tied', 'training_time': 32.61918902397156, 'bic': -8067504.624668959, 'aic': -8132496.584140577}, 
	{'n_components': 1, 'covariance': 'diag', 'training_time': 0.16138005256652832, 'bic': -2731596.204130766, 'aic': -2733360.691718231}, 
	{'n_components': 2, 'covariance': 'diag', 'training_time': 0.4393880367279053, 'bic': -7908062.360569935, 'aic': -7911599.504668881}, 
	{'n_components': 3, 'covariance': 'diag', 'training_time': 0.6771438121795654, 'bic': -11024896.499206105, 'aic': -11030206.299816532}, 
	{'n_components': 4, 'covariance': 'diag', 'training_time': 1.018484115600586, 'bic': -10849508.831860851, 'aic': -10856591.288982758}, 
	{'n_components': 5, 'covariance': 'diag', 'training_time': 0.7299060821533203, 'bic': -12591326.089252833, 'aic': -12600181.202886222}, 
	{'n_components': 6, 'covariance': 'diag', 'training_time': 0.9452059268951416, 'bic': -13124988.57180258, 'aic': -13135616.34194745}, 
	{'n_components': 7, 'covariance': 'diag', 'training_time': 1.395216941833496, 'bic': -13837335.014049044, 'aic': -13849735.440705394}, 
	{'n_components': 8, 'covariance': 'diag', 'training_time': 1.5690510272979736, 'bic': -15479985.336566167, 'aic': -15494158.419733997}, 
	{'n_components': 9, 'covariance': 'diag', 'training_time': 1.3286480903625488, 'bic': -16249802.747595023, 'aic': -16265748.487274334}, 
	{'n_components': 10, 'covariance': 'diag', 'training_time': 1.7586922645568848, 'bic': -16561869.22643325, 'aic': -16579587.622624042}, 
	{'n_components': 11, 'covariance': 'diag', 'training_time': 1.408385992050171, 'bic': -16959754.020099353, 'aic': -16979245.072801627}, 
	{'n_components': 12, 'covariance': 'diag', 'training_time': 1.9474260807037354, 'bic': -17026940.44197232, 'aic': -17048204.15118607}, 
	{'n_components': 13, 'covariance': 'diag', 'training_time': 1.8667409420013428, 'bic': -17506565.835588876, 'aic': -17529602.20131411}, 
	{'n_components': 14, 'covariance': 'diag', 'training_time': 1.2950482368469238, 'bic': -17561791.202443108, 'aic': -17586600.224679824}, 
	{'n_components': 15, 'covariance': 'diag', 'training_time': 1.5369987487792969, 'bic': -17810392.43223838, 'aic': -17836974.11098658}, 
	{'n_components': 16, 'covariance': 'diag', 'training_time': 1.7809419631958008, 'bic': -17897008.672309313, 'aic': -17925363.00756899}, 
	{'n_components': 17, 'covariance': 'diag', 'training_time': 1.6746256351470947, 'bic': -18330258.085701592, 'aic': -18360385.07747275}, 
	{'n_components': 18, 'covariance': 'diag', 'training_time': 2.8735129833221436, 'bic': -18287586.086785194, 'aic': -18319485.735067833}, 
	{'n_components': 19, 'covariance': 'diag', 'training_time': 2.21657395362854, 'bic': -18396601.624713536, 'aic': -18430273.929507654}, 
	{'n_components': 1, 'covariance': 'spherical', 'training_time': 0.15887117385864258, 'bic': 59975229.988115236, 'aic': 59974339.57539749}, 
	{'n_components': 2, 'covariance': 'spherical', 'training_time': 0.5152831077575684, 'bic': 57204100.54409319, 'aic': 57202311.549733676}, 
	{'n_components': 3, 'covariance': 'spherical', 'training_time': 0.6553161144256592, 'bic': 54471371.51666194, 'aic': 54468683.94066066}, 
	{'n_components': 4, 'covariance': 'spherical', 'training_time': 3.2255570888519287, 'bic': 53069842.79019475, 'aic': 53066256.63255171}, 
	{'n_components': 5, 'covariance': 'spherical', 'training_time': 2.191431999206543, 'bic': 51927147.15703931, 'aic': 51922662.4177545}, 
	{'n_components': 6, 'covariance': 'spherical', 'training_time': 3.4231581687927246, 'bic': 50567751.684124224, 'aic': 50562368.363197654}, 
	{'n_components': 7, 'covariance': 'spherical', 'training_time': 4.665366888046265, 'bic': 49785316.42608569, 'aic': 49779034.523517355}, 
	{'n_components': 8, 'covariance': 'spherical', 'training_time': 5.284813165664673, 'bic': 49071073.1600116, 'aic': 49063892.6758015}, 
	{'n_components': 9, 'covariance': 'spherical', 'training_time': 5.20818305015564, 'bic': 48464757.969733246, 'aic': 48456678.90388138}, 
	{'n_components': 10, 'covariance': 'spherical', 'training_time': 5.387628793716431, 'bic': 48091481.470540576, 'aic': 48082503.823046945}, 
	{'n_components': 11, 'covariance': 'spherical', 'training_time': 5.791970729827881, 'bic': 47577103.08534483, 'aic': 47567226.856209435}, 
	{'n_components': 12, 'covariance': 'spherical', 'training_time': 6.3044469356536865, 'bic': 47488939.672161855, 'aic': 47478164.8613847}, 
	{'n_components': 13, 'covariance': 'spherical', 'training_time': 6.19012713432312, 'bic': 46946367.39272036, 'aic': 46934694.000301436}, 
	{'n_components': 14, 'covariance': 'spherical', 'training_time': 6.576258182525635, 'bic': 46865312.73139184, 'aic': 46852740.757331155}, 
	{'n_components': 15, 'covariance': 'spherical', 'training_time': 6.659095048904419, 'bic': 46294470.035491064, 'aic': 46280999.47978862}, 
	{'n_components': 16, 'covariance': 'spherical', 'training_time': 6.548668146133423, 'bic': 45981375.184813164, 'aic': 45967006.047468945}, 
	{'n_components': 17, 'covariance': 'spherical', 'training_time': 6.769140005111694, 'bic': 45877531.19788366, 'aic': 45862263.478897676}, 
	{'n_components': 18, 'covariance': 'spherical', 'training_time': 6.961733102798462, 'bic': 45397138.658574276, 'aic': 45380972.35794653}, 
	{'n_components': 19, 'covariance': 'spherical', 'training_time': 7.342148065567017, 'bic': 45311775.028563544, 'aic': 45294710.146294035}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Adult \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_adult")
	plt.cla()

def em_wine():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.018931865692138672, 'bic': 21419.48440344007, 'aic': 21011.66777329107}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.0808568000793457, 'bic': 14679.474136199715, 'aic': 13857.56677389942}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.21753191947937012, 'bic': 11952.686643438836, 'aic': 10716.688548987246}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.23929381370544434, 'bic': 11027.847218425128, 'aic': 9377.758391822244}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.3452422618865967, 'bic': 10516.820411816967, 'aic': 8452.64085306279}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.496807336807251, 'bic': 10086.116701318479, 'aic': 7607.846410413009}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.3713672161102295, 'bic': 10158.84466509111, 'aic': 7266.483642034345}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.4181690216064453, 'bic': 10183.041149475564, 'aic': 6876.589394267505}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.5157690048217773, 'bic': 9866.18435709771, 'aic': 6145.641869738358}, {'n_components': 10, 'covariance': 'full', 'training_time': 0.5662510395050049, 'bic': 10716.51402141754, 'aic': 6581.880801906895}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.5767951011657715, 'bic': 11064.161737316477, 'aic': 6515.437785654537}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.9631807804107666, 'bic': 10617.04018012754, 'aic': 5654.225496314308}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.8097188472747803, 'bic': 10549.32937143207, 'aic': 5172.423955467542}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.9375972747802734, 'bic': 10891.074921875908, 'aic': 5100.078773760088}, {'n_components': 15, 'covariance': 'full', 'training_time': 0.8827600479125977, 'bic': 11000.961694188814, 'aic': 4795.8748139217005}, {'n_components': 16, 'covariance': 'full', 'training_time': 0.9721038341522217, 'bic': 11734.59003612341, 'aic': 5115.412423705002}, {'n_components': 17, 'covariance': 'full', 'training_time': 1.2374491691589355, 'bic': 11328.029965989796, 'aic': 4294.761621420093}, {'n_components': 18, 'covariance': 'full', 'training_time': 1.705057144165039, 'bic': 12152.117706079665, 'aic': 4704.758629358668}, {'n_components': 19, 'covariance': 'full', 'training_time': 1.4080770015716553, 'bic': 12308.473364634421, 'aic': 4447.023555762132}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.017412900924682617, 'bic': 21419.48440335915, 'aic': 21011.66777321015}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.07529306411743164, 'bic': 20805.244159587233, 'aic': 20328.412407413016}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.06631970405578613, 'bic': 21402.440878816662, 'aic': 20856.59400461723}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.2596297264099121, 'bic': 19299.33740438378, 'aic': 18684.47540815913}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.2876400947570801, 'bic': 16495.676564288544, 'aic': 15811.79944603868}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.3179051876068115, 'bic': 15477.524210482095, 'aic': 14724.631970207016}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.38173580169677734, 'bic': 15411.455785799579, 'aic': 14589.548423499284}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.354691743850708, 'bic': 15058.469262503872, 'aic': 14167.546778178361}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.43117809295654297, 'bic': 15228.120626105665, 'aic': 14268.183019754939}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.5842230319976807, 'bic': 14918.665598524018, 'aic': 13889.712870148076}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.4605598449707031, 'bic': 15418.803441438195, 'aic': 14320.835591037037}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.5757839679718018, 'bic': 14785.974120105475, 'aic': 13618.991147679102}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.5891289710998535, 'bic': 14726.599108221297, 'aic': 13490.601013769707}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.5950980186462402, 'bic': 14854.146664563097, 'aic': 13549.133448086293}, {'n_components': 15, 'covariance': 'tied', 'training_time': 0.8557097911834717, 'bic': 14530.53177940142, 'aic': 13156.5034408994}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.7148768901824951, 'bic': 14333.474157481438, 'aic': 12890.430696954201}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.7939040660858154, 'bic': 14404.349368399902, 'aic': 12892.29078584745}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.6366991996765137, 'bic': 14577.934325551441, 'aic': 12996.860620973774}, {'n_components': 19, 'covariance': 'tied', 'training_time': 1.0535130500793457, 'bic': 13098.151598886292, 'aic': 11448.062772283409}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.01596522331237793, 'bic': 32606.717965948308, 'aic': 32481.23592590246}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.03276205062866211, 'bic': 24096.56412362182, 'aic': 23839.325941527837}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.05278515815734863, 'bic': 20023.091318084113, 'aic': 19634.09699394199}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.08132696151733398, 'bic': 17643.762663125555, 'aic': 17123.01219693529}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.15577983856201172, 'bic': 17205.64855831301, 'aic': 16553.141950074605}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.18203401565551758, 'bic': 16443.01753701286, 'aic': 15658.75478672632}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.21412181854248047, 'bic': 15773.853515525767, 'aic': 14857.834623191087}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.30894994735717773, 'bic': 15018.963539036245, 'aic': 13971.188504653426}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.24345993995666504, 'bic': 14632.85058034489, 'aic': 13453.31940391393}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.15407919883728027, 'bic': 15044.177030597397, 'aic': 13732.8897121183}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.20734310150146484, 'bic': 14326.614476149743, 'aic': 12883.571015622507}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.2519192695617676, 'bic': 13850.878049161658, 'aic': 12276.078446586283}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.256911039352417, 'bic': 13314.034370567111, 'aic': 11607.478625943597}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.2480318546295166, 'bic': 13180.895603784014, 'aic': 11342.583717112362}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.25479888916015625, 'bic': 12975.73083554082, 'aic': 11005.662806821028}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.25787901878356934, 'bic': 12935.62705884493, 'aic': 10833.802888077}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.3184051513671875, 'bic': 12708.382558115869, 'aic': 10474.8022452998}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.28106689453125, 'bic': 12916.248357757808, 'aic': 10550.911902893598}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.29155874252319336, 'bic': 12557.608717734878, 'aic': 10060.51612082253}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.0143280029296875, 'bic': 321485.83037208155, 'aic': 321416.81525005633}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.02788710594177246, 'bic': 289663.756229137, 'aic': 289519.4518830843}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.06713700294494629, 'bic': 274452.6792706285, 'aic': 274233.08570054825}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.07892298698425293, 'bic': 264487.9345797459, 'aic': 264193.0517856382}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.05731678009033203, 'bic': 258737.3637072042, 'aic': 258367.19168906895}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.04715609550476074, 'bic': 254073.48440303825, 'aic': 253628.02316087548}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.10715317726135254, 'bic': 251427.1461992233, 'aic': 250906.39573303304}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.17536687850952148, 'bic': 249229.8587351468, 'aic': 248633.81904492903}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.08707904815673828, 'bic': 243889.97750869356, 'aic': 243218.64859444828}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 0.0870981216430664, 'bic': 243191.94442653732, 'aic': 242445.32628826454}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.25547194480895996, 'bic': 238737.66606899296, 'aic': 237915.75870669266}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.15765714645385742, 'bic': 236185.2534273154, 'aic': 235288.05684098759}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.31006383895874023, 'bic': 236545.04253669575, 'aic': 235572.55672634044}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.16164875030517578, 'bic': 233831.96742051185, 'aic': 232784.19238612903}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.35261106491088867, 'bic': 232191.64398191887, 'aic': 231068.57972350853}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.15249419212341309, 'bic': 230463.97563371607, 'aic': 229265.62215127822}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.22237396240234375, 'bic': 228811.08660146847, 'aic': 227537.44389500312}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.1789548397064209, 'bic': 227915.06893063342, 'aic': 226566.13700014056}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.18297195434570312, 'bic': 226473.52682212493, 'aic': 225049.30566760458}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine")
	plt.cla()


def PCA_adult_2(principal_df):
	''' ''' 

	colors = ['r', 'g']

	list_data = principal_df.dropna().to_dict('records')

	for i in range(len(list_data)):
		plt.plot(list_data[i]['principal_component_1'], list_data[i]['principal_component_2'], marker='o', c=colors[int(list_data[i]['label'])])

	plt.title("PCA: Adult \n Two Components")
	plt.xlabel("Principal Component 1")
	plt.ylabel("Principal Component 2")
	plt.tight_layout()
	plt.savefig("figures/pca_adult_2")
	plt.cla()

def PCA_adult_3(principal_df):
	''' ''' 

	colors = ['r', 'g', 'b']

	list_data = principal_df.dropna().to_dict('records')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	for i in range(len(list_data)):
		x = list_data[i]['principal_component_1']
		y = list_data[i]['principal_component_2']
		z = list_data[i]['principal_component_3']

		ax.plot(x, y, z, marker='o', c=colors[int(list_data[i]['label'])])

	plt.title("PCA: Adult \n Thre Components")
	ax.set_xlabel('Principal Component 1')
	ax.set_ylabel('Principal Component 2')
	ax.set_zlabel('Principal Component 3')
	plt.tight_layout()
	plt.savefig("figures/pca_adult_3")
	plt.cla()


def kmeans_adult_pca():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5855745718946339, 'training_time': 1.1628410816192627, 'distortion': 52527.51047044468, 'inertia': 120134194847036.45}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5855745718946339, 'training_time': 0.6222000122070312, 'distortion': 52527.51047044468, 'inertia': 120134194847036.45}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5526105895303167, 'training_time': 1.9433927536010742, 'distortion': 35872.23302124003, 'inertia': 64857995335625.8}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5526105895303167, 'training_time': 1.2942578792572021, 'distortion': 35872.23302124003, 'inertia': 64857995335625.8}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5558723945421823, 'training_time': 1.3213460445404053, 'distortion': 30486.36449203527, 'inertia': 43066652332946.2}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5558723945421823, 'training_time': 0.9633171558380127, 'distortion': 30486.36449203527, 'inertia': 43066652332946.2}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5308447238173012, 'training_time': 2.8982460498809814, 'distortion': 26482.234012541212, 'inertia': 31273900018929.734}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5308447238173012, 'training_time': 1.25785493850708, 'distortion': 26482.234012541205, 'inertia': 31273900018929.742}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5443398109948878, 'training_time': 2.197619915008545, 'distortion': 20958.215475541696, 'inertia': 22542372159673.867}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5443398109948878, 'training_time': 1.7661912441253662, 'distortion': 20958.215475541696, 'inertia': 22542372159673.867}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.5438070105851691, 'training_time': 2.2300376892089844, 'distortion': 18840.388180263133, 'inertia': 17326983206508.926}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.5438070105851691, 'training_time': 1.5413780212402344, 'distortion': 18840.388180263133, 'inertia': 17326983206508.926}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5311989257396696, 'training_time': 2.709925889968872, 'distortion': 16729.61604676281, 'inertia': 13905406931651.225}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5311989257396696, 'training_time': 2.00339674949646, 'distortion': 16729.61604676281, 'inertia': 13905406931651.229}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5311803908001561, 'training_time': 4.914248943328857, 'distortion': 15506.331794457597, 'inertia': 11159196597943.828}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5311803908001561, 'training_time': 3.8436970710754395, 'distortion': 15506.331794457597, 'inertia': 11159196597943.828}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Adult (PCA) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_pca_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Adult (PCA) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_pca_elbow')
	plt.cla()


def em_adult_pca():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.31592679023742676, 'bic': 504191.4384922495, 'aic': 482728.95683869935}, {'n_components': 2, 'covariance': 'full', 'training_time': 1.9224181175231934, 'bic': -1621866.5203002782, 'aic': -1664799.653566135}, {'n_components': 3, 'covariance': 'full', 'training_time': 1.8117797374725342, 'bic': -3676648.6060445495, 'aic': -3741052.390922713}, {'n_components': 4, 'covariance': 'full', 'training_time': 3.5002269744873047, 'bic': -5192015.015762684, 'aic': -5277889.4522531545}, {'n_components': 5, 'covariance': 'full', 'training_time': 5.846794128417969, 'bic': -5550706.485038453, 'aic': -5658051.57314123}, {'n_components': 6, 'covariance': 'full', 'training_time': 5.508080005645752, 'bic': -6050762.905168559, 'aic': -6179578.644883643}, {'n_components': 7, 'covariance': 'full', 'training_time': 8.149090051651001, 'bic': -6064467.926001514, 'aic': -6214754.317328905}, {'n_components': 8, 'covariance': 'full', 'training_time': 14.115776062011719, 'bic': -6553106.666751715, 'aic': -6724863.709691413}, {'n_components': 9, 'covariance': 'full', 'training_time': 11.48345398902893, 'bic': -7297546.7185723, 'aic': -7490774.413124304}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.3085041046142578, 'bic': 504191.4384922495, 'aic': 482728.95683869935}, {'n_components': 2, 'covariance': 'tied', 'training_time': 1.9373669624328613, 'bic': 365737.48536682234, 'aic': 343686.76668279804}, {'n_components': 3, 'covariance': 'tied', 'training_time': 3.02838397026062, 'bic': 316303.8870984977, 'aic': 293664.93138399924}, {'n_components': 4, 'covariance': 'tied', 'training_time': 6.561094760894775, 'bic': 102143.72850639826, 'aic': 78916.53576142564}, {'n_components': 5, 'covariance': 'tied', 'training_time': 5.6194469928741455, 'bic': 267871.14772998076, 'aic': 244055.717954534}, {'n_components': 6, 'covariance': 'tied', 'training_time': 9.117411136627197, 'bic': 77884.25701059093, 'aic': 53480.590204669985}, {'n_components': 7, 'covariance': 'tied', 'training_time': 14.063969850540161, 'bic': 7432.755645908677, 'aic': -17559.148190486416}, {'n_components': 8, 'covariance': 'tied', 'training_time': 13.741280794143677, 'bic': -116455.83544188339, 'aic': -142035.97630875264}, {'n_components': 9, 'covariance': 'tied', 'training_time': 16.266123056411743, 'bic': -267020.51917437516, 'aic': -293188.8970717186}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.269366979598999, 'bic': 478919.090982134, 'aic': 477758.9568386988}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.7129111289978027, 'bic': -2021028.3434828522, 'aic': -2023356.781728479}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.748089075088501, 'bic': -2330236.4543052227, 'aic': -2333733.1966530415}, {'n_components': 4, 'covariance': 'diag', 'training_time': 3.1802561283111572, 'bic': -2564938.6718093613, 'aic': -2569603.718259372}, {'n_components': 5, 'covariance': 'diag', 'training_time': 2.203761339187622, 'bic': -2827374.855710638, 'aic': -2833208.2062628404}, {'n_components': 6, 'covariance': 'diag', 'training_time': 2.6485378742218018, 'bic': -2812029.0577512924, 'aic': -2819030.7124056863}, {'n_components': 7, 'covariance': 'diag', 'training_time': 3.9410738945007324, 'bic': -3079917.1227843305, 'aic': -3088087.081540916}, {'n_components': 8, 'covariance': 'diag', 'training_time': 2.650520086288452, 'bic': -2951738.857103248, 'aic': -2961077.1199620254}, {'n_components': 9, 'covariance': 'diag', 'training_time': 2.083189010620117, 'bic': -3056105.022469269, 'aic': -3066611.589430238}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.20123600959777832, 'bic': 40245582.95566509, 'aic': 40244994.71863461}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.7442879676818848, 'bic': 38418224.692841396, 'aic': 38417040.04882169}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.9094982147216797, 'bic': 36631213.68440941, 'aic': 36629432.63340048}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 6.309692144393921, 'bic': 35729039.198945604, 'aic': 35726661.74094744}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 3.2351760864257812, 'bic': 34799585.202975206, 'aic': 34796611.33798781}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 3.7486231327056885, 'bic': 34104610.829063796, 'aic': 34101040.55708717}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 5.572569131851196, 'bic': 33605369.19278399, 'aic': 33601202.51381813}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 7.412057876586914, 'bic': 33106658.511890553, 'aic': 33101895.425935462}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 10.90459394454956, 'bic': 32728465.19075867, 'aic': 32723105.697814353}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Adult (PCA) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_adult_pca")
	plt.cla()


def kmeans_wine_pca():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5079409805468327, 'training_time': 0.19659209251403809, 'distortion': 24.708229620476505, 'inertia': 3329844.992458443}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5079409805468327, 'training_time': 0.07902956008911133, 'distortion': 24.708229620476505, 'inertia': 3329844.992458443}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.4125470861199443, 'training_time': 0.16112399101257324, 'distortion': 20.23983161448192, 'inertia': 2209683.442906402}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.4125470861199443, 'training_time': 0.14164519309997559, 'distortion': 20.23983161448192, 'inertia': 2209683.442906402}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.3787614190793391, 'training_time': 0.22783994674682617, 'distortion': 17.418557078922287, 'inertia': 1665851.0194672453}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.3787614190793391, 'training_time': 0.2041008472442627, 'distortion': 17.418557078922287, 'inertia': 1665851.0194672453}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.3490034430398302, 'training_time': 0.20883393287658691, 'distortion': 16.07269422369797, 'inertia': 1401416.1650537644}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.3490034430398302, 'training_time': 0.23116612434387207, 'distortion': 16.07269422369797, 'inertia': 1401416.1650537644}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.3168996960670385, 'training_time': 0.21790480613708496, 'distortion': 14.890753972316633, 'inertia': 1236283.6885107155}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.3168996960670385, 'training_time': 0.2618851661682129, 'distortion': 14.890753972316633, 'inertia': 1236283.6885107153}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.3183812436074841, 'training_time': 0.2551279067993164, 'distortion': 14.087803254481722, 'inertia': 1104890.1177109196}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.3183812436074841, 'training_time': 0.24921894073486328, 'distortion': 14.087803254481722, 'inertia': 1104890.1177109194}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.31932672728540357, 'training_time': 0.251483678817749, 'distortion': 13.995271545165668, 'inertia': 1005131.8483184254}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.31932672728540357, 'training_time': 0.29776716232299805, 'distortion': 13.995271545165668, 'inertia': 1005131.8483184252}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.3010325263368494, 'training_time': 0.4600028991699219, 'distortion': 13.300249966660504, 'inertia': 913148.4489228334}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.3010325263368494, 'training_time': 0.3441910743713379, 'distortion': 13.300249966660504, 'inertia': 913148.4489228334}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Wine (PCA) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_pca_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Wine (PCA) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_pca_elbow')
	plt.cla()


def em_wine_pca():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.015290021896362305, 'bic': 94501.51782059316, 'aic': 94332.25513893648}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.14153099060058594, 'bic': 91431.79924671576, 'aic': 91087.00489519289}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.1436312198638916, 'bic': 91038.07469750964, 'aic': 90517.7486761206}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.21741390228271484, 'bic': 90473.73102187747, 'aic': 89777.87333062223}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.21717023849487305, 'bic': 90445.63319664734, 'aic': 89574.24383552591}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.27666258811950684, 'bic': 90214.58122949167, 'aic': 89167.66019850406}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.2562990188598633, 'bic': 90195.61715274146, 'aic': 88973.16445188766}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.38683629035949707, 'bic': 90100.57838740075, 'aic': 88702.59401668076}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.32135725021362305, 'bic': 90430.64979359052, 'aic': 88857.13375300435}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.013124704360961914, 'bic': 94501.51782059316, 'aic': 94332.25513893648}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.05813121795654297, 'bic': 93884.10194413165, 'aic': 93670.95634500842}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.18068313598632812, 'bic': 93648.49940126772, 'aic': 93391.47088467795}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.14776301383972168, 'bic': 93501.56108354234, 'aic': 93200.64964948602}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.1892096996307373, 'bic': 93574.91494059011, 'aic': 93230.12058906724}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.20040488243103027, 'bic': 93376.76494924721, 'aic': 92988.0876802578}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.21549105644226074, 'bic': 93489.23018564918, 'aic': 93056.66999919323}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.2815539836883545, 'bic': 93433.4217940318, 'aic': 92956.9786901093}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.5285272598266602, 'bic': 93109.4599563965, 'aic': 92589.13393500746}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.017466068267822266, 'bic': 94377.48299745057, 'aic': 94302.2551389365}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.044302940368652344, 'bic': 93265.4312863451, 'aic': 93108.70658110744}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.07635903358459473, 'bic': 92927.3735141421, 'aic': 92689.15196218085}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.1147770881652832, 'bic': 92507.30392290243, 'aic': 92187.58552421759}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.22584772109985352, 'bic': 92070.71897471875, 'aic': 91669.50372931032}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.14570307731628418, 'bic': 91816.74037087924, 'aic': 91334.02827874722}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.23771166801452637, 'bic': 91576.67210546842, 'aic': 91012.46316661281}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.172774076461792, 'bic': 91657.29950235134, 'aic': 91011.59371677216}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.13562893867492676, 'bic': 91590.30584188618, 'aic': 90863.10320958341}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.017986059188842773, 'bic': 203939.90273631926, 'aic': 203896.0198188527}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.01993107795715332, 'bic': 187026.62110715694, 'aic': 186932.58628401434}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.04430389404296875, 'bic': 179562.83969807805, 'aic': 179418.6529692594}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.05158567428588867, 'bic': 173761.3905258095, 'aic': 173567.0518913148}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.04325294494628906, 'bic': 171074.7873879557, 'aic': 170830.29684778495}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.07106566429138184, 'bic': 168420.41219548116, 'aic': 168125.76974963435}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.08165812492370605, 'bic': 167003.5340937276, 'aic': 166658.73974220472}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.10206985473632812, 'bic': 165187.17865175556, 'aic': 164792.23239455663}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.11369991302490234, 'bic': 163682.16867125046, 'aic': 163237.07050837547}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine (PCA) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine_pca")
	plt.cla()



def em_wine_ica():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.022740840911865234, 'bic': -42692.4308205516, 'aic': -42723.81152164939}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.023231983184814453, 'bic': -43180.3860509144, 'aic': -43249.42359332954}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.03907895088195801, 'bic': -43198.73187739884, 'aic': -43305.42626113133}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.053510189056396484, 'bic': -43223.84584876655, 'aic': -43368.197073816395}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.0762488842010498, 'bic': -43303.62757537844, 'aic': -43485.63564174564}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.09492111206054688, 'bic': -43327.958596761695, 'aic': -43547.623504446245}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.09151077270507812, 'bic': -43318.460236420266, 'aic': -43575.78198542216}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.09882688522338867, 'bic': -43316.11387163115, 'aic': -43611.09246195039}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.08408808708190918, 'bic': -43287.22498784921, 'aic': -43619.860419485805}, {'n_components': 10, 'covariance': 'full', 'training_time': 0.10374116897583008, 'bic': -43248.96340571323, 'aic': -43619.25567866718}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.11153292655944824, 'bic': -43195.2254919217, 'aic': -43603.174606193}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.12507987022399902, 'bic': -43205.77281109969, 'aic': -43651.37876668834}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.11893916130065918, 'bic': -43162.19883088873, 'aic': -43645.461627794735}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.1212000846862793, 'bic': -43090.65172684063, 'aic': -43611.57136506398}, {'n_components': 15, 'covariance': 'full', 'training_time': 0.14934206008911133, 'bic': -43035.50586501024, 'aic': -43594.08234455094}, {'n_components': 16, 'covariance': 'full', 'training_time': 0.16418790817260742, 'bic': -43027.59949042545, 'aic': -43623.8328112835}, {'n_components': 17, 'covariance': 'full', 'training_time': 0.14531397819519043, 'bic': -42991.54597982313, 'aic': -43625.436141998536}, {'n_components': 18, 'covariance': 'full', 'training_time': 0.26602602005004883, 'bic': -42973.836876499445, 'aic': -43645.3838799922}, {'n_components': 19, 'covariance': 'full', 'training_time': 0.19164490699768066, 'bic': -42889.003879895965, 'aic': -43598.20772470607}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.01986098289489746, 'bic': -42692.4308205516, 'aic': -42723.81152164939}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.026112794876098633, 'bic': -42706.7123948401, 'aic': -42756.921516596565}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.057270050048828125, 'bic': -42905.16093727316, 'aic': -42974.198479688304}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.16543006896972656, 'bic': -43118.4276252638, 'aic': -43206.29358833762}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.09212613105773926, 'bic': -43085.13714959923, 'aic': -43191.83153333172}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.08064389228820801, 'bic': -43073.65331381762, 'aic': -43199.17611820879}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.11195087432861328, 'bic': -43093.4293566218, 'aic': -43237.78058167164}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.14334893226623535, 'bic': -43086.80586166024, 'aic': -43249.985507368765}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.19461703300476074, 'bic': -43320.9852137349, 'aic': -43502.9932801021}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.13011789321899414, 'bic': -43058.43525624435, 'aic': -43259.27174327023}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.11767315864562988, 'bic': -43059.32212199755, 'aic': -43278.9870296821}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.1429150104522705, 'bic': -43021.245372690806, 'aic': -43259.738701034024}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.13516640663146973, 'bic': -43251.23927194384, 'aic': -43508.56102094574}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.3815741539001465, 'bic': -43250.052419184794, 'aic': -43526.202588845365}, {'n_components': 15, 'covariance': 'tied', 'training_time': 0.13239097595214844, 'bic': -43211.90224087427, 'aic': -43506.88083119351}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.16695594787597656, 'bic': -43200.78657421185, 'aic': -43514.593585189774}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.14318394660949707, 'bic': -43223.71120726875, 'aic': -43556.34663890535}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.1690969467163086, 'bic': -43221.92415996931, 'aic': -43573.388012264586}, {'n_components': 19, 'covariance': 'tied', 'training_time': 0.19927191734313965, 'bic': -43186.74829944601, 'aic': -43557.04057239996}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.021047115325927734, 'bic': -42700.70696077115, 'aic': -42725.81152164939}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.020489931106567383, 'bic': -43158.94490968165, 'aic': -43215.43017165768}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.029720067977905273, 'bic': -43200.12720669092, 'aic': -43287.99316976474}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.044156789779663086, 'bic': -43232.49635627273, 'aic': -43351.74302044434}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.05019783973693848, 'bic': -43273.9147090634, 'aic': -43424.5420743328}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.043953895568847656, 'bic': -43307.94043919632, 'aic': -43489.948505563516}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.04941892623901367, 'bic': -43311.47865289307, 'aic': -43524.86742035806}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.06411981582641602, 'bic': -43373.78711683864, 'aic': -43618.55658540142}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.04590797424316406, 'bic': -43332.00639565464, 'aic': -43608.15656531521}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.060363054275512695, 'bic': -43291.489180404766, 'aic': -43599.020051163134}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.0883188247680664, 'bic': -43259.42650647257, 'aic': -43598.33807832873}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.08662199974060059, 'bic': -43227.435915626265, 'aic': -43597.728188580215}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.0807948112487793, 'bic': -43238.65490020117, 'aic': -43640.32787425291}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.05974984169006348, 'bic': -43156.114104821856, 'aic': -43589.16777997139}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.09017705917358398, 'bic': -43183.98881170698, 'aic': -43648.42318795431}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.09099173545837402, 'bic': -43174.48783147671, 'aic': -43670.30290882183}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.08761000633239746, 'bic': -43122.04944010409, 'aic': -43649.245218547}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.07871794700622559, 'bic': -43078.09169940638, 'aic': -43636.66817894708}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.08568811416625977, 'bic': -43020.07289066838, 'aic': -43610.03007130687}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.013770103454589844, 'bic': -42708.983100990714, 'aic': -42727.81152164939}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.020657777786254883, 'bic': -43048.959106939845, 'aic': -43092.89208847676}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.03716588020324707, 'bic': -43113.14717231585, 'aic': -43182.18471473099}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.032124996185302734, 'bic': -43060.06712504781, 'aic': -43154.20922834119}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.06694197654724121, 'bic': -43350.56286448024, 'aic': -43469.80952865185}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.08529472351074219, 'bic': -43308.1625855437, 'aic': -43452.51381059355}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.046320199966430664, 'bic': -43392.946370595295, 'aic': -43562.40215652337}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.04957389831542969, 'bic': -43362.39751893537, 'aic': -43556.957865741686}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.06981897354125977, 'bic': -43327.305239168585, 'aic': -43546.970146853135}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 0.05420708656311035, 'bic': -43301.9516322682, 'aic': -43546.72110083098}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.0671072006225586, 'bic': -43309.69481998185, 'aic': -43579.56884942287}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.06205606460571289, 'bic': -43288.79856395489, 'aic': -43583.77715427414}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.06156182289123535, 'bic': -43243.63245416226, 'aic': -43563.71560535974}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.06854915618896484, 'bic': -43251.81794808786, 'aic': -43597.00566016357}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.06751513481140137, 'bic': -43259.8183955953, 'aic': -43630.11066854925}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.07347822189331055, 'bic': -43244.19516046383, 'aic': -43639.59199429602}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.09059500694274902, 'bic': -43198.57412185997, 'aic': -43619.07551657039}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.09406113624572754, 'bic': -43217.43107631892, 'aic': -43663.037031907574}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.14000701904296875, 'bic': -43158.725350533954, 'aic': -43629.43586700084}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine (ICA) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine_ica")
	plt.cla()



def kmeans_adult_ica():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.9164853971439654, 'training_time': 0.2547800540924072, 'distortion': 0.004930647235042559, 'inertia': 1.1262110498815607}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.9164853971439654, 'training_time': 0.1110987663269043, 'distortion': 0.004930647235042559, 'inertia': 1.1262110498815607}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5503125910903748, 'training_time': 0.2501368522644043, 'distortion': 0.0034750020854553716, 'inertia': 0.5400889427820954}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5503125910903748, 'training_time': 0.23674798011779785, 'distortion': 0.0034750020854553716, 'inertia': 0.5400889427820954}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5025887585980732, 'training_time': 0.8236899375915527, 'distortion': 0.0025613188110810993, 'inertia': 0.3499842431629436}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5025887585980732, 'training_time': 0.985029935836792, 'distortion': 0.0025613188110810993, 'inertia': 0.3499842431629436}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5325111386386788, 'training_time': 0.44229817390441895, 'distortion': 0.0023215343508563055, 'inertia': 0.271696144484565}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5325111386386788, 'training_time': 0.42983102798461914, 'distortion': 0.0023215343508563055, 'inertia': 0.27169614448456514}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5335474560474576, 'training_time': 0.36029696464538574, 'distortion': 0.00201284621391013, 'inertia': 0.19671893393530135}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5335474560474576, 'training_time': 1.0062751770019531, 'distortion': 0.00201284621391013, 'inertia': 0.19671893393530135}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.5116646927339491, 'training_time': 0.44736528396606445, 'distortion': 0.0018080938296016755, 'inertia': 0.1568784778433497}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.5116646927339491, 'training_time': 0.6504557132720947, 'distortion': 0.0018080938296016755, 'inertia': 0.1568784778433497}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5088501018658239, 'training_time': 0.48072314262390137, 'distortion': 0.001542462595245718, 'inertia': 0.12777750731629006}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5088501018658239, 'training_time': 0.5434701442718506, 'distortion': 0.001542462595245718, 'inertia': 0.12777750731629003}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5136197982187933, 'training_time': 0.679326057434082, 'distortion': 0.0013836326112916105, 'inertia': 0.10931749075340624}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5136197982187933, 'training_time': 0.7071759700775146, 'distortion': 0.00138363261129161, 'inertia': 0.10931749075340623}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.5239694456672505, 'training_time': 0.7067530155181885, 'distortion': 0.0013068951673386507, 'inertia': 0.09536972334432978}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.5239694456672505, 'training_time': 0.8258259296417236, 'distortion': 0.0013068951673386505, 'inertia': 0.09536972334432978}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.5152463560214519, 'training_time': 0.6589429378509521, 'distortion': 0.001241392143403146, 'inertia': 0.08430150165564913}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.5152463560214519, 'training_time': 0.6323447227478027, 'distortion': 0.001241392143403146, 'inertia': 0.08430150165564913}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.5119722770490782, 'training_time': 0.6682610511779785, 'distortion': 0.0011398920628601073, 'inertia': 0.0742954497829615}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.5119722770490782, 'training_time': 0.6155459880828857, 'distortion': 0.0011398920628601073, 'inertia': 0.07429544978296149}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.5121758080031314, 'training_time': 0.6399881839752197, 'distortion': 0.0010965194623596514, 'inertia': 0.06482410995507154}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.5121758080031314, 'training_time': 0.74381422996521, 'distortion': 0.0010965194623596514, 'inertia': 0.06482410995507154}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.5098821369468849, 'training_time': 0.9151451587677002, 'distortion': 0.0009999041612557377, 'inertia': 0.058750027286256765}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.5098821369468849, 'training_time': 1.3339910507202148, 'distortion': 0.000999904161255738, 'inertia': 0.05875002728625676}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.5115081382960625, 'training_time': 0.8134651184082031, 'distortion': 0.0009811451791519878, 'inertia': 0.053943776461605406}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.5115081382960625, 'training_time': 1.3548829555511475, 'distortion': 0.0009811451791519874, 'inertia': 0.053943776461605406}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.5080814938882432, 'training_time': 0.6577370166778564, 'distortion': 0.0009402100820677788, 'inertia': 0.049367989236152876}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.5080814938882432, 'training_time': 0.9811720848083496, 'distortion': 0.0009402100820677788, 'inertia': 0.04936798923615288}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.5083273356068327, 'training_time': 0.6901803016662598, 'distortion': 0.0009119964449812245, 'inertia': 0.04493319085179595}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.5083273356068327, 'training_time': 0.8216509819030762, 'distortion': 0.0009119964449812246, 'inertia': 0.044933190851795944}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.5069690191055227, 'training_time': 0.7308809757232666, 'distortion': 0.0008578367211157103, 'inertia': 0.04150034225815425}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.5069690191055227, 'training_time': 0.9709818363189697, 'distortion': 0.0008578367211157101, 'inertia': 0.041500342258154244}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.5028006603157366, 'training_time': 0.72705078125, 'distortion': 0.0008131481479914177, 'inertia': 0.038954755415499705}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.5028006603157366, 'training_time': 0.8370487689971924, 'distortion': 0.0008131481479914177, 'inertia': 0.038954755415499705}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Adult (ICA) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_ica_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Adult (ICA) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_ica_elbow')
	plt.cla()


def em_adult_ica():
	''' ''' 
	
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.17223501205444336, 'bic': -381436.5548402641, 'aic': -381477.38928896264}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.06401205062866211, 'bic': -434161.91059983417, 'aic': -434251.74638697103}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.25515079498291016, 'bic': -478429.18904056516, 'aic': -478568.0261661403}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.2359321117401123, 'bic': -481130.9954294664, 'aic': -481318.83389347984}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.2999451160430908, 'bic': -482245.37306728796, 'aic': -482482.2128697397}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.6186830997467041, 'bic': -482748.3082541633, 'aic': -483034.1493950533}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.34713101387023926, 'bic': -483360.2699981771, 'aic': -483695.11247750535}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.4852559566497803, 'bic': -484005.9087851464, 'aic': -484389.752602913}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.6338109970092773, 'bic': -483642.38546987536, 'aic': -484075.2306260802}, {'n_components': 10, 'covariance': 'full', 'training_time': 0.5768482685089111, 'bic': -483573.0495318679, 'aic': -484054.89602651104}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.7088298797607422, 'bic': -484357.01617780403, 'aic': -484887.8640108854}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.5170049667358398, 'bic': -483907.98498299095, 'aic': -484487.83415451064}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.579193115234375, 'bic': -484391.4162749684, 'aic': -485020.2667849264}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.5202271938323975, 'bic': -484351.388500151, 'aic': -485029.24034854723}, {'n_components': 15, 'covariance': 'full', 'training_time': 1.3820691108703613, 'bic': -484294.7314289646, 'aic': -485021.58461579913}, {'n_components': 16, 'covariance': 'full', 'training_time': 0.9294860363006592, 'bic': -484575.1625369642, 'aic': -485351.017062237}, {'n_components': 17, 'covariance': 'full', 'training_time': 0.6099252700805664, 'bic': -484669.59465978877, 'aic': -485494.45052349987}, {'n_components': 18, 'covariance': 'full', 'training_time': 0.6610031127929688, 'bic': -484136.66612702457, 'aic': -485010.523329174}, {'n_components': 19, 'covariance': 'full', 'training_time': 0.4556710720062256, 'bic': -484463.13983789267, 'aic': -485385.9983784803}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.03067803382873535, 'bic': -381436.5548402641, 'aic': -381477.38928896264}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.13538098335266113, 'bic': -384235.7580135127, 'aic': -384301.0931314304}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.20141816139221191, 'bic': -436768.1198867838, 'aic': -436857.9556739207}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.19730305671691895, 'bic': -436749.0797473149, 'aic': -436863.4162036709}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.2678079605102539, 'bic': -460918.97354513046, 'aic': -461057.81067070557}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.2711658477783203, 'bic': -461366.4727065616, 'aic': -461529.8105013559}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.3160860538482666, 'bic': -461380.3467547618, 'aic': -461568.18521877524}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.36971020698547363, 'bic': -461359.9275442372, 'aic': -461572.2666774697}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.5421469211578369, 'bic': -461817.02916316397, 'aic': -462053.8689656157}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.46288299560546875, 'bic': -461736.7073818246, 'aic': -461998.04785349546}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.9854929447174072, 'bic': -480652.54988213704, 'aic': -480938.391023027}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.8504490852355957, 'bic': -480644.4978395218, 'aic': -480954.83964963094}, {'n_components': 13, 'covariance': 'tied', 'training_time': 1.2412598133087158, 'bic': -480616.5282679653, 'aic': -480951.3707472936}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.9078779220581055, 'bic': -480637.4462311794, 'aic': -480996.7893797268}, {'n_components': 15, 'covariance': 'tied', 'training_time': 1.0252101421356201, 'bic': -480816.88434782514, 'aic': -481200.7281655917}, {'n_components': 16, 'covariance': 'tied', 'training_time': 1.3626387119293213, 'bic': -480781.34513939195, 'aic': -481189.68962637766}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.6756248474121094, 'bic': -480940.3782061163, 'aic': -481373.22336232115}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.8156402111053467, 'bic': -480807.58066465205, 'aic': -481264.926490076}, {'n_components': 19, 'covariance': 'tied', 'training_time': 0.8128409385681152, 'bic': -480780.35232440464, 'aic': -481262.1988190478}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.03614497184753418, 'bic': -381446.7217300037, 'aic': -381479.3892889626}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.04439496994018555, 'bic': -434181.1856393242, 'aic': -434254.6876469816}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.19506478309631348, 'bic': -478453.5929504405, 'aic': -478567.92940679647}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.25629210472106934, 'bic': -480606.49063345534, 'aic': -480761.6615385099}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.23463201522827148, 'bic': -482293.9765718666, 'aic': -482489.9819256197}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.5825850963592529, 'bic': -483235.5963616264, 'aic': -483472.4361640781}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.24707722663879395, 'bic': -483348.27518628276, 'aic': -483625.94943743304}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.404371976852417, 'bic': -483563.89757898735, 'aic': -483882.4062788362}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.5658268928527832, 'bic': -483819.5082356827, 'aic': -484178.8513842301}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.5067191123962402, 'bic': -484033.7521581225, 'aic': -484433.92975536844}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.3489971160888672, 'bic': -483647.6110797481, 'aic': -484088.62312569265}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.32468104362487793, 'bic': -484508.2803947384, 'aic': -484990.12688938156}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.40271592140197754, 'bic': -484529.2249402291, 'aic': -485051.9058835708}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.8082990646362305, 'bic': -484493.16003848705, 'aic': -485056.6754305273}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.37581396102905273, 'bic': -484416.29612717987, 'aic': -485020.6459679187}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.33818817138671875, 'bic': -484523.8518495996, 'aic': -485169.036139037}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.9047667980194092, 'bic': -484702.0160627369, 'aic': -485388.0348008729}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.5732438564300537, 'bic': -484735.69118376635, 'aic': -485462.5443706009}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.44137096405029297, 'bic': -484815.5184518386, 'aic': -485583.2060873717}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.09934091567993164, 'bic': -381456.88861974346, 'aic': -381481.3892889626}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.08563899993896484, 'bic': -409867.7414543918, 'aic': -409924.9096825698}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.20958900451660156, 'bic': -429334.4362356295, 'aic': -429424.27202276635}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.29213380813598633, 'bic': -445099.9862577149, 'aic': -445222.48960381065}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.17711496353149414, 'bic': -453127.7664248513, 'aic': -453282.93732990586}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.24486303329467773, 'bic': -457853.5486251792, 'aic': -458041.38708919263}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.2566237449645996, 'bic': -460989.2433927818, 'aic': -461209.7494157541}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.48961615562438965, 'bic': -460108.64330709336, 'aic': -460361.8168890245}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.634044885635376, 'bic': -466449.4504578154, 'aic': -466735.29159870534}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 1.3578479290008545, 'bic': -468012.7115429038, 'aic': -468331.22024275264}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.8182010650634766, 'bic': -468063.73556353204, 'aic': -468414.91182233975}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.4547152519226074, 'bic': -469245.71536440455, 'aic': -469629.5591821711}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.5342209339141846, 'bic': -469549.6177814683, 'aic': -469966.1291581937}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.541748046875, 'bic': -469571.8201732615, 'aic': -470020.9991089458}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.5744800567626953, 'bic': -470192.22202760255, 'aic': -470674.0685222457}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.4733848571777344, 'bic': -470206.8859059178, 'aic': -470721.3999595198}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.5126562118530273, 'bic': -470471.17348945525, 'aic': -471018.35510201607}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.6555800437927246, 'bic': -470255.01515119744, 'aic': -470834.8643227171}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.6721329689025879, 'bic': -470586.739689864, 'aic': -471199.25642034254}]
	
	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Adult (ICA) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_adult_ica")
	plt.cla()

def kmeans_wine_ica():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.34088104602551655, 'training_time': 0.20052599906921387, 'distortion': 0.015429228447953212, 'inertia': 1.3502674231155132}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.34088104602551655, 'training_time': 0.1065220832824707, 'distortion': 0.015429228447953212, 'inertia': 1.3502674231155134}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.3645438010991279, 'training_time': 0.17587018013000488, 'distortion': 0.012864033743954293, 'inertia': 0.8975400621612435}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.3645438010991279, 'training_time': 0.1505138874053955, 'distortion': 0.012864033743954293, 'inertia': 0.8975400621612435}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.32580591295628936, 'training_time': 0.18370890617370605, 'distortion': 0.011556399559354774, 'inertia': 0.7421744603163513}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.32580591295628936, 'training_time': 0.1944870948791504, 'distortion': 0.011556399559354774, 'inertia': 0.7421744603163513}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.3323062952517981, 'training_time': 0.3133711814880371, 'distortion': 0.010608589890583777, 'inertia': 0.6184257826743425}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.3323062952517981, 'training_time': 0.2889671325683594, 'distortion': 0.010608589890583777, 'inertia': 0.6184257826743425}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.33781373219151867, 'training_time': 0.22145986557006836, 'distortion': 0.00966931878496865, 'inertia': 0.514438401739804}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.33781373219151867, 'training_time': 0.2371370792388916, 'distortion': 0.00966931878496865, 'inertia': 0.514438401739804}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.32385768213834965, 'training_time': 0.24932408332824707, 'distortion': 0.008927740784074753, 'inertia': 0.4600798676481182}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.32385768213834965, 'training_time': 0.33035993576049805, 'distortion': 0.008927740784074753, 'inertia': 0.4600798676481182}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.33205150473790207, 'training_time': 0.30615711212158203, 'distortion': 0.008650115458854806, 'inertia': 0.4029602268006303}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.33205150473790207, 'training_time': 0.55283522605896, 'distortion': 0.008650115458854806, 'inertia': 0.4029602268006303}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.3235400118947206, 'training_time': 0.35921502113342285, 'distortion': 0.00822802932833905, 'inertia': 0.3675372823586018}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.3235400118947206, 'training_time': 0.6925070285797119, 'distortion': 0.00822802932833905, 'inertia': 0.3675372823586018}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.3375599407731247, 'training_time': 0.33890509605407715, 'distortion': 0.007652517962740306, 'inertia': 0.3281970423336659}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.3375599407731247, 'training_time': 0.3833279609680176, 'distortion': 0.007652517962740306, 'inertia': 0.32819704233366587}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.3394895227435749, 'training_time': 0.3107781410217285, 'distortion': 0.007603455094070204, 'inertia': 0.30070581018867304}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.3394895227435749, 'training_time': 0.37427186965942383, 'distortion': 0.007603455094070204, 'inertia': 0.300705810188673}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.342023220256869, 'training_time': 0.4224050045013428, 'distortion': 0.007297152339910014, 'inertia': 0.274452161805368}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.342023220256869, 'training_time': 0.4964790344238281, 'distortion': 0.007297152339910014, 'inertia': 0.274452161805368}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.34199774069358513, 'training_time': 0.34452199935913086, 'distortion': 0.007023361230324792, 'inertia': 0.2530105064601068}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.34199774069358513, 'training_time': 0.5982801914215088, 'distortion': 0.007023361230324792, 'inertia': 0.2530105064601068}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.33404674535765705, 'training_time': 0.46457791328430176, 'distortion': 0.006747411670315846, 'inertia': 0.23460196327082544}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.33404674535765705, 'training_time': 0.4039139747619629, 'distortion': 0.006747411670315845, 'inertia': 0.23460196327082544}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.32813639190573995, 'training_time': 0.3840522766113281, 'distortion': 0.006489782519930686, 'inertia': 0.21962178508428948}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.32813639190573995, 'training_time': 0.3922100067138672, 'distortion': 0.006489782519930686, 'inertia': 0.21962178508428948}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.3298332122202938, 'training_time': 0.30959200859069824, 'distortion': 0.006234106787868879, 'inertia': 0.20575329516036198}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.3298332122202938, 'training_time': 0.40990376472473145, 'distortion': 0.006234106787868879, 'inertia': 0.20575329516036198}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.33022602220313513, 'training_time': 0.3558499813079834, 'distortion': 0.006122514441480181, 'inertia': 0.1940331744933048}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.33022602220313513, 'training_time': 0.4175269603729248, 'distortion': 0.006122514441480181, 'inertia': 0.1940331744933048}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.3279531487596763, 'training_time': 0.3624701499938965, 'distortion': 0.005927147987098429, 'inertia': 0.18459606092946138}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.3279531487596763, 'training_time': 0.5346317291259766, 'distortion': 0.005927147987098429, 'inertia': 0.18459606092946135}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.3275974092569727, 'training_time': 0.40788912773132324, 'distortion': 0.005806795883728544, 'inertia': 0.1740525254895376}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.3275974092569727, 'training_time': 0.4557971954345703, 'distortion': 0.005806795883728545, 'inertia': 0.17405252548953756}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Wine (ICA) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_ica_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Wine (iCA) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_ica_elbow')
	plt.cla()


def adult_reconstruction_error():
	''' ''' 

	results = [{'n_components': 1, 'reconstruction_error': 3595257.4121999415}, {'n_components': 11, 'reconstruction_error': 1578116.3650108727}, {'n_components': 21, 'reconstruction_error': 2221095.502646234}, {'n_components': 31, 'reconstruction_error': 7957077.931938618}, {'n_components': 41, 'reconstruction_error': 4183048.191310688}, {'n_components': 51, 'reconstruction_error': 2228000.2506673774}, {'n_components': 61, 'reconstruction_error': 6357808.779139418}, {'n_components': 71, 'reconstruction_error': 1848020.295083082}, {'n_components': 81, 'reconstruction_error': 1849946.785652501}, {'n_components': 91, 'reconstruction_error': 5892140.937570505}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.xlabel("No. of Components")
	plt.ylabel("Average Reconstruction Error")
	plt.title("Adult (RP) \n 10 runs at each N")
	plt.tight_layout()
	plt.savefig("figures/adult_rp")
	plt.cla()

def wine_reconstruction_error():

	results = [{'n_components': 1, 'reconstruction_error': 1.8175004341750697e-27}, {'n_components': 2, 'reconstruction_error': 3.4042950634414595e-27}, {'n_components': 3, 'reconstruction_error': 3.591960944777136e-28}, {'n_components': 4, 'reconstruction_error': 3.7229152371511215e-27}, {'n_components': 5, 'reconstruction_error': 2.7844772551050772e-28}, {'n_components': 6, 'reconstruction_error': 1.74641821985774e-28}, {'n_components': 7, 'reconstruction_error': 8.232488845272395e-28}, {'n_components': 8, 'reconstruction_error': 6.59587535072091e-27}, {'n_components': 9, 'reconstruction_error': 6.61671116928303e-27}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.xlabel("No. of Components")
	plt.ylabel("Average Reconstruction Error")
	plt.title("Wine (RP) \n 10 runs at each N")
	plt.tight_layout()
	plt.savefig("figures/wine_rp")
	plt.cla()


def kmeans_adult_rand():
	
	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5877579431233132, 'training_time': 0.2763388156890869, 'distortion': 44655.91730970932, 'inertia': 87978623023768.81}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5877579431233132, 'training_time': 0.20975399017333984, 'distortion': 44655.91730970932, 'inertia': 87978623023768.81}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5536431872749599, 'training_time': 0.23723268508911133, 'distortion': 30541.804984751332, 'inertia': 47879127756002.19}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5536431872749599, 'training_time': 0.2215719223022461, 'distortion': 30541.804984751343, 'inertia': 47879127756002.19}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5601869969321311, 'training_time': 0.42570996284484863, 'distortion': 26151.814775306495, 'inertia': 31511290650779.395}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5601869969321311, 'training_time': 0.48711609840393066, 'distortion': 26151.814775306495, 'inertia': 31511290650779.39}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5337264059517104, 'training_time': 0.4247102737426758, 'distortion': 22462.235879487678, 'inertia': 22661564658868.07}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5337264059517104, 'training_time': 0.48005008697509766, 'distortion': 22462.235879487675, 'inertia': 22661564658868.07}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5460181958777099, 'training_time': 0.549659013748169, 'distortion': 17864.62144245438, 'inertia': 16389779999535.123}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5460181958777099, 'training_time': 0.620628833770752, 'distortion': 17864.621442454376, 'inertia': 16389779999535.123}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.5488758332820022, 'training_time': 0.48998212814331055, 'distortion': 16132.51270511807, 'inertia': 12259653950367.28}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.5488758332820022, 'training_time': 0.6885888576507568, 'distortion': 16132.512705118068, 'inertia': 12259653950367.28}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5416572526277954, 'training_time': 0.5600707530975342, 'distortion': 14850.888461913972, 'inertia': 9564141381656.385}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5416572526277954, 'training_time': 0.6584229469299316, 'distortion': 14850.888461913972, 'inertia': 9564141381656.385}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5362897174874279, 'training_time': 0.5870809555053711, 'distortion': 12911.006870477275, 'inertia': 7550139047158.216}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5362897174874279, 'training_time': 0.6637508869171143, 'distortion': 12911.006870477275, 'inertia': 7550139047158.218}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Adult (RP) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_rp_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Adult (RP) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_rp_elbow')
	plt.cla()


def em_adult_rand():
	''' ''' 
	
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.03990626335144043, 'bic': 1988127.3098174515, 'aic': 1987841.509042551}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.17064189910888672, 'bic': 1449480.4549558705, 'aic': 1448900.6876696437}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.2543017864227295, 'bic': 1427557.8511648793, 'aic': 1426684.117367326}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.40627598762512207, 'bic': 1403865.5119055917, 'aic': 1402697.811596712}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.9084270000457764, 'bic': 1394184.503360434, 'aic': 1392722.8365402282}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.8404979705810547, 'bic': 1403660.4375150597, 'aic': 1401904.8041835276}, {'n_components': 7, 'covariance': 'full', 'training_time': 1.0999510288238525, 'bic': 1401606.7371359346, 'aic': 1399557.1372930761}, {'n_components': 8, 'covariance': 'full', 'training_time': 1.5085630416870117, 'bic': 1391087.5361815104, 'aic': 1388743.9698273255}, {'n_components': 9, 'covariance': 'full', 'training_time': 2.2401950359344482, 'bic': 1381257.8343168092, 'aic': 1378620.3014512982}, {'n_components': 10, 'covariance': 'full', 'training_time': 3.172664165496826, 'bic': 1377739.0278802344, 'aic': 1374807.528503397}, {'n_components': 11, 'covariance': 'full', 'training_time': 3.244901180267334, 'bic': 1379074.6964622233, 'aic': 1375849.2305740595}, {'n_components': 12, 'covariance': 'full', 'training_time': 3.2419180870056152, 'bic': 1381448.8527395122, 'aic': 1377929.4203400223}, {'n_components': 13, 'covariance': 'full', 'training_time': 3.4340429306030273, 'bic': 1384546.5854705174, 'aic': 1380733.186559701}, {'n_components': 14, 'covariance': 'full', 'training_time': 4.152354001998901, 'bic': 1376287.1079049667, 'aic': 1372179.742482824}, {'n_components': 15, 'covariance': 'full', 'training_time': 7.1175618171691895, 'bic': 1373668.43168284, 'aic': 1369267.099749371}, {'n_components': 16, 'covariance': 'full', 'training_time': 6.3255250453948975, 'bic': 1374166.2437555466, 'aic': 1369470.9453107514}, {'n_components': 17, 'covariance': 'full', 'training_time': 4.624091148376465, 'bic': 1381877.236049762, 'aic': 1376887.9710936404}, {'n_components': 18, 'covariance': 'full', 'training_time': 6.02508807182312, 'bic': 1370189.962478691, 'aic': 1364906.731011243}, {'n_components': 19, 'covariance': 'full', 'training_time': 4.60038685798645, 'bic': 1375455.6082836841, 'aic': 1369878.4103049098}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.037741661071777344, 'bic': 1988127.3098174469, 'aic': 1987841.5090425464}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.16720795631408691, 'bic': 1985325.3894942293, 'aic': 1984974.2628279228}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.2557802200317383, 'bic': 1985407.3608594772, 'aic': 1984990.9083017649}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.2917191982269287, 'bic': 1984191.8440799543, 'aic': 1983710.0656308362}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.4214158058166504, 'bic': 1984262.5467220086, 'aic': 1983715.4423814847}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.5455970764160156, 'bic': 1983989.779083677, 'aic': 1983377.3488517473}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.6128249168395996, 'bic': 1983632.8303588508, 'aic': 1982955.0742355152}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.7129268646240234, 'bic': 1983384.311996866, 'aic': 1982641.2299821244}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.5913848876953125, 'bic': 1983494.4318878865, 'aic': 1982686.023981739}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.7939708232879639, 'bic': 1928539.3961459706, 'aic': 1927665.6623484173}, {'n_components': 11, 'covariance': 'tied', 'training_time': 2.1167140007019043, 'bic': 1909667.257561211, 'aic': 1908728.197872252}, {'n_components': 12, 'covariance': 'tied', 'training_time': 1.3224539756774902, 'bic': 1928603.4578621872, 'aic': 1927599.0722818223}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.7244529724121094, 'bic': 1983006.6181796214, 'aic': 1981936.9067078508}, {'n_components': 14, 'covariance': 'tied', 'training_time': 2.6791763305664062, 'bic': 1819125.3091729006, 'aic': 1817990.271809724}, {'n_components': 15, 'covariance': 'tied', 'training_time': 4.471181154251099, 'bic': 1815443.0040904665, 'aic': 1814242.640835884}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.8714859485626221, 'bic': 1982770.9477002441, 'aic': 1981505.2585542558}, {'n_components': 17, 'covariance': 'tied', 'training_time': 3.1725807189941406, 'bic': 1847632.4017989954, 'aic': 1846301.3867616013}, {'n_components': 18, 'covariance': 'tied', 'training_time': 5.093432188034058, 'bic': 1814641.9774208828, 'aic': 1813245.6364920828}, {'n_components': 19, 'covariance': 'tied', 'training_time': 4.599579095840454, 'bic': 1794010.8362830218, 'aic': 1792549.169462816}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.031751155853271484, 'bic': 3932023.885847534, 'aic': 3931909.565537574}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.08551907539367676, 'bic': 3782076.471515494, 'aic': 3781839.6651591477}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.17573809623718262, 'bic': 3632909.51935057, 'aic': 3632550.226947838}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.40384888648986816, 'bic': 3564537.152064117, 'aic': 3564055.373614999}, {'n_components': 5, 'covariance': 'diag', 'training_time': 1.1242728233337402, 'bic': 3486913.1790050943, 'aic': 3486308.9145095902}, {'n_components': 6, 'covariance': 'diag', 'training_time': 1.313385248184204, 'bic': 3433732.058560611, 'aic': 3433005.308018721}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.9906120300292969, 'bic': 3393227.223991152, 'aic': 3392377.987402876}, {'n_components': 8, 'covariance': 'diag', 'training_time': 1.8907196521759033, 'bic': 3357845.534607727, 'aic': 3356873.811973065}, {'n_components': 9, 'covariance': 'diag', 'training_time': 2.052122116088867, 'bic': 3330093.1554897903, 'aic': 3328998.9468087424}, {'n_components': 10, 'covariance': 'diag', 'training_time': 2.102185010910034, 'bic': 3309942.3910988295, 'aic': 3308725.6963713956}, {'n_components': 11, 'covariance': 'diag', 'training_time': 2.4173319339752197, 'bic': 3288855.5548391403, 'aic': 3287516.3740653205}, {'n_components': 12, 'covariance': 'diag', 'training_time': 2.6308209896087646, 'bic': 3269292.435317695, 'aic': 3267830.7684974894}, {'n_components': 13, 'covariance': 'diag', 'training_time': 2.8238041400909424, 'bic': 3257606.6654275786, 'aic': 3256022.512560987}, {'n_components': 14, 'covariance': 'diag', 'training_time': 2.9373481273651123, 'bic': 3230311.0636035185, 'aic': 3228604.424690541}, {'n_components': 15, 'covariance': 'diag', 'training_time': 3.171193838119507, 'bic': 3221670.4397980697, 'aic': 3219841.314838706}, {'n_components': 16, 'covariance': 'diag', 'training_time': 2.985321044921875, 'bic': 3198709.0108802617, 'aic': 3196757.399874512}, {'n_components': 17, 'covariance': 'diag', 'training_time': 3.1280369758605957, 'bic': 3192108.2976729544, 'aic': 3190034.200620819}, {'n_components': 18, 'covariance': 'diag', 'training_time': 3.606551170349121, 'bic': 3186955.0867559747, 'aic': 3184758.503657453}, {'n_components': 19, 'covariance': 'diag', 'training_time': 3.9892308712005615, 'bic': 3171235.0500783995, 'aic': 3168915.980933492}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.03031015396118164, 'bic': 4314930.506800984, 'aic': 4314865.180909578}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.08862590789794922, 'bic': 4162883.9766030903, 'aic': 4162745.159083853}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.1992640495300293, 'bic': 4008755.843567724, 'aic': 4008543.5344206546}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.5992300510406494, 'bic': 3933611.748534585, 'aic': 3933325.947759684}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.7287569046020508, 'bic': 3868120.1361873504, 'aic': 3867760.843784618}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 1.1709697246551514, 'bic': 3791430.5231891423, 'aic': 3790997.7391585787}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 1.2649857997894287, 'bic': 3747896.6845829436, 'aic': 3747390.4089245484}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 1.9140090942382812, 'bic': 3705741.2346543376, 'aic': 3705161.4673681105}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 2.0146491527557373, 'bic': 3671355.0776957083, 'aic': 3670701.8187816497}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 2.1220548152923584, 'bic': 3649073.468191722, 'aic': 3648346.717649832}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 2.4895150661468506, 'bic': 3624622.2379012066, 'aic': 3623821.995731485}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 2.5872912406921387, 'bic': 3610960.986202723, 'aic': 3610087.25240517}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 2.7398319244384766, 'bic': 3588524.747259956, 'aic': 3587577.521834571}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 2.8486859798431396, 'bic': 3555975.5085762306, 'aic': 3554954.791523014}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 3.0768771171569824, 'bic': 3545479.9876463846, 'aic': 3544385.7789653367}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 3.1308040618896484, 'bic': 3540326.77424279, 'aic': 3539159.0739339106}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 3.3897979259490967, 'bic': 3516512.029803616, 'aic': 3515270.8378669047}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 3.5048508644104004, 'bic': 3505785.3346668137, 'aic': 3504470.651102271}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 3.850229024887085, 'bic': 3511540.9512108974, 'aic': 3510152.776018523}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine (RP) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine_rp")
	plt.cla()

def em_wine_rand():
	''' ''' 
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.012521028518676758, 'bic': 93993.63862296559, 'aic': 93905.84052582388}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.08620810508728027, 'bic': 91966.01099276975, 'aic': 91784.14350583334}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.09399008750915527, 'bic': 91669.41940073697, 'aic': 91393.48252400587}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.12461709976196289, 'bic': 91458.53041639863, 'aic': 91088.52414987284}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.14298701286315918, 'bic': 91390.62428371023, 'aic': 90926.54862738975}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.2515261173248291, 'bic': 91250.11111073788, 'aic': 90691.96606462271}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.38713598251342773, 'bic': 91249.45807930427, 'aic': 90597.24364339441}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.30610203742980957, 'bic': 91301.89337639506, 'aic': 90555.60955069051}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.27027273178100586, 'bic': 91499.49166444036, 'aic': 90659.13844894111}, {'n_components': 10, 'covariance': 'full', 'training_time': 0.280869722366333, 'bic': 91621.73345504224, 'aic': 90687.3108497483}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.3123469352722168, 'bic': 91656.53285734414, 'aic': 90628.04086225551}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.5141439437866211, 'bic': 91490.72179326376, 'aic': 90368.16040838044}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.5083870887756348, 'bic': 91673.64571217376, 'aic': 90457.01493749575}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.5566740036010742, 'bic': 91607.46332782684, 'aic': 90296.76316335415}, {'n_components': 15, 'covariance': 'full', 'training_time': 0.54215407371521, 'bic': 91607.12915373345, 'aic': 90202.35959946606}, {'n_components': 16, 'covariance': 'full', 'training_time': 0.43018507957458496, 'bic': 91833.79259993431, 'aic': 90334.95365587223}, {'n_components': 17, 'covariance': 'full', 'training_time': 0.6380200386047363, 'bic': 91749.58676298223, 'aic': 90156.67842912546}, {'n_components': 18, 'covariance': 'full', 'training_time': 0.5981829166412354, 'bic': 91934.83823963953, 'aic': 90247.86051598807}, {'n_components': 19, 'covariance': 'full', 'training_time': 0.8029050827026367, 'bic': 91830.8986359228, 'aic': 90049.85152247665}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.014837026596069336, 'bic': 93993.63862296562, 'aic': 93905.8405258239}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.05394101142883301, 'bic': 93321.22985120423, 'aic': 93202.07529079763}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.04958915710449219, 'bic': 93946.1680960535, 'aic': 93795.65707238199}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.09724903106689453, 'bic': 93255.06540393092, 'aic': 93073.19791699451}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.12193894386291504, 'bic': 93283.31430792253, 'aic': 93070.09035772123}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.1938798427581787, 'bic': 93123.17156775203, 'aic': 92878.59115428582}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.24423718452453613, 'bic': 92963.56864585787, 'aic': 92687.63176912678}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.26476216316223145, 'bic': 92860.73160839819, 'aic': 92553.4382684022}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.19936108589172363, 'bic': 93517.62607313979, 'aic': 93178.9762698789}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.2441868782043457, 'bic': 93216.66354413335, 'aic': 92846.65727760756}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.2766261100769043, 'bic': 92700.48052992881, 'aic': 92299.11780013813}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.42633700370788574, 'bic': 92687.66741564817, 'aic': 92254.94822259259}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.40709495544433594, 'bic': 92614.81786470607, 'aic': 92150.74220838559}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.29068708419799805, 'bic': 92801.0426386408, 'aic': 92305.61051905544}, {'n_components': 15, 'covariance': 'tied', 'training_time': 0.4024519920349121, 'bic': 92739.72472828263, 'aic': 92212.93614543235}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.4986898899078369, 'bic': 92907.93638585125, 'aic': 92349.79133973608}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.6410238742828369, 'bic': 92868.91822155783, 'aic': 92279.41671217777}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.6064679622650146, 'bic': 92672.10492244452, 'aic': 92051.24694979955}, {'n_components': 19, 'covariance': 'tied', 'training_time': 0.6208150386810303, 'bic': 92895.33599145706, 'aic': 92243.1215555472}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.011480093002319336, 'bic': 142250.6667387091, 'aic': 142200.49639748526}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.016749858856201172, 'bic': 132759.66685506006, 'aic': 132653.0548799594}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.028443098068237305, 'bic': 128686.25346204365, 'aic': 128523.19985306618}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.030627965927124023, 'bic': 125724.59348356776, 'aic': 125505.09824071349}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.03908991813659668, 'bic': 123824.44814504315, 'aic': 123548.51126831205}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.033364295959472656, 'bic': 122211.66120328016, 'aic': 121879.28269267225}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.041877031326293945, 'bic': 121576.13171951161, 'aic': 121187.31157502689}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.07462191581726074, 'bic': 120567.53223541917, 'aic': 120122.27045705763}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.04475808143615723, 'bic': 119587.63950469774, 'aic': 119085.9360924594}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.05509018898010254, 'bic': 118929.11491404474, 'aic': 118370.96986792957}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.10640907287597656, 'bic': 118520.8786372044, 'aic': 117906.29195721241}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.09421396255493164, 'bic': 117827.81232399645, 'aic': 117156.78401012765}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.11804413795471191, 'bic': 117621.11695021077, 'aic': 116893.64700246515}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.0957949161529541, 'bic': 116861.92079064385, 'aic': 116078.00920902143}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.1855030059814453, 'bic': 116661.15534013776, 'aic': 115820.80212463852}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.09343314170837402, 'bic': 116149.65076013433, 'aic': 115252.85591075828}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.13312506675720215, 'bic': 115813.44898124674, 'aic': 114860.21249799387}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.16344690322875977, 'bic': 115791.2361064633, 'aic': 114781.55798933361}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.1563119888305664, 'bic': 115758.02245453716, 'aic': 114691.90270353066}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.020754098892211914, 'bic': 150478.64491118398, 'aic': 150447.28844791907}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.016163110733032227, 'bic': 139444.1724160499, 'aic': 139375.18819686712}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.029618024826049805, 'bic': 133618.58672847605, 'aic': 133511.9747533754}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.041882991790771484, 'bic': 128851.1243645766, 'aic': 128706.88463355806}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.28427815437316895, 'bic': 125800.16537626853, 'aic': 125618.29788933213}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.03384995460510254, 'bic': 123783.1656547566, 'aic': 123563.67041190232}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.04411506652832031, 'bic': 122552.00201019211, 'aic': 122294.87901141995}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.05025601387023926, 'bic': 121122.60489490077, 'aic': 120827.85414021074}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.04669785499572754, 'bic': 120735.07200383785, 'aic': 120402.69349322993}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 0.07346010208129883, 'bic': 119293.61017496609, 'aic': 118923.6039084403}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.05668139457702637, 'bic': 119138.56907242692, 'aic': 118730.93504998327}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.06197476387023926, 'bic': 118729.91689012363, 'aic': 118284.65511176208}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.09756112098693848, 'bic': 118255.07945144303, 'aic': 117772.18991716362}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.09946584701538086, 'bic': 118194.83625660291, 'aic': 117674.31896640561}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.07572817802429199, 'bic': 117967.54426861201, 'aic': 117409.39922249684}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.09941983222961426, 'bic': 117612.32366582839, 'aic': 117016.55086379535}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.08683609962463379, 'bic': 117336.01974951045, 'aic': 116702.61919155953}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.0865178108215332, 'bic': 116935.06581740773, 'aic': 116264.03750353893}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.0907278060913086, 'bic': 116567.40482215871, 'aic': 115858.74875237205}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine (RP) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine_rp")
	plt.cla()


def kmeans_wine_rand():
	
	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5486871964678666, 'training_time': 0.18793821334838867, 'distortion': 29.318049898477714, 'inertia': 4996322.36816868}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5486871964678666, 'training_time': 0.06193184852600098, 'distortion': 29.318049898477714, 'inertia': 4996322.36816868}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.47053772793858517, 'training_time': 0.15404796600341797, 'distortion': 22.90930465485205, 'inertia': 3015680.1301940265}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.47053772793858517, 'training_time': 0.13863277435302734, 'distortion': 22.90930465485205, 'inertia': 3015680.130194027}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.4439915502823269, 'training_time': 0.1557459831237793, 'distortion': 18.91054618874037, 'inertia': 2095474.5978663715}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.4439915502823269, 'training_time': 0.11910486221313477, 'distortion': 18.91054618874037, 'inertia': 2095474.5978663715}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.41943576711282116, 'training_time': 0.21718096733093262, 'distortion': 16.87623288677546, 'inertia': 1642557.0626928955}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.41943576711282116, 'training_time': 0.2551591396331787, 'distortion': 16.87623288677546, 'inertia': 1642557.0626928955}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.4020283417153079, 'training_time': 0.2447490692138672, 'distortion': 15.111810184843721, 'inertia': 1352476.7915434416}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.4020283417153079, 'training_time': 0.20308613777160645, 'distortion': 15.111810184843721, 'inertia': 1352476.7915434416}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.4022500375093383, 'training_time': 0.2140491008758545, 'distortion': 14.965327337817882, 'inertia': 1154853.5474858147}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.4022500375093383, 'training_time': 0.2144629955291748, 'distortion': 14.965327337817882, 'inertia': 1154853.5474858147}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.37716338260992266, 'training_time': 0.22510290145874023, 'distortion': 13.877671415242464, 'inertia': 995869.8683754439}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.37716338260992266, 'training_time': 0.23108601570129395, 'distortion': 13.877671415242467, 'inertia': 995869.868375444}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.3592708616870622, 'training_time': 0.28234434127807617, 'distortion': 13.131593767061629, 'inertia': 876760.6667183852}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.3592708616870622, 'training_time': 0.3672659397125244, 'distortion': 13.131593767061627, 'inertia': 876760.6667183854}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.336565633847698, 'training_time': 0.2546417713165283, 'distortion': 12.459987350264456, 'inertia': 794829.4335301451}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.336565633847698, 'training_time': 0.2727549076080322, 'distortion': 12.459987350264456, 'inertia': 794829.4335301451}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.324505659813503, 'training_time': 0.25842928886413574, 'distortion': 11.873325402852743, 'inertia': 730841.9120657741}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.324505659813503, 'training_time': 0.2684009075164795, 'distortion': 11.873325402852746, 'inertia': 730841.9120657741}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.3245991332074482, 'training_time': 0.283829927444458, 'distortion': 11.731875292427885, 'inertia': 672688.9738129249}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.3245991332074482, 'training_time': 0.31682515144348145, 'distortion': 11.731875292427885, 'inertia': 672688.9738129249}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.3066211687086786, 'training_time': 0.27567005157470703, 'distortion': 11.323432000969412, 'inertia': 629504.3201778487}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.3066211687086786, 'training_time': 0.3021841049194336, 'distortion': 11.323432000969412, 'inertia': 629504.3201778487}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.3074598474234134, 'training_time': 0.29931187629699707, 'distortion': 11.001380353313749, 'inertia': 588227.2678907495}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.3074598474234134, 'training_time': 0.33479928970336914, 'distortion': 11.001380353313749, 'inertia': 588227.2678907494}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.3027262690783409, 'training_time': 0.298856258392334, 'distortion': 10.681941694539185, 'inertia': 556171.6344314446}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.3027262690783409, 'training_time': 0.3165321350097656, 'distortion': 10.681941694539185, 'inertia': 556171.6344314446}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.298533151990037, 'training_time': 0.2886466979980469, 'distortion': 10.44383043932264, 'inertia': 529857.3457188712}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.298533151990037, 'training_time': 0.35610103607177734, 'distortion': 10.44383043932264, 'inertia': 529857.3457188712}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.2962255552295377, 'training_time': 0.3405451774597168, 'distortion': 10.15513340674314, 'inertia': 499303.24431291333}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.2962255552295377, 'training_time': 0.4085550308227539, 'distortion': 10.15513340674314, 'inertia': 499303.24431291333}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.2909615281701416, 'training_time': 0.3438541889190674, 'distortion': 9.87051482064628, 'inertia': 475256.15292312205}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.2909615281701416, 'training_time': 0.3947310447692871, 'distortion': 9.870514820646282, 'inertia': 475256.15292312205}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.2913155513000014, 'training_time': 0.3621349334716797, 'distortion': 9.743265608418154, 'inertia': 454849.22830643924}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.2913155513000014, 'training_time': 0.3779289722442627, 'distortion': 9.743265608418152, 'inertia': 454849.22830643924}]


	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Wine (RP) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_rp_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Wine (RP) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_rp_elbow')
	plt.cla()

def wine_svd_explained_variance():

	results = [{'algorithm': 'randomized', 'n_components': 9, 'explained_variance': [0.9083913808938145, 0.07905368466676116, 0.010159333114936915, 0.0022947227669795197, 8.37299139098472e-05, 6.805716140385703e-06, 5.394654520894456e-06, 4.252420266544504e-06, 4.840391445595898e-07]}, {'algorithm': 'arpack', 'n_components': 9, 'explained_variance': [0.9083913808938158, 0.07905368466676155, 0.010159333114936924, 0.0022947227669795323, 8.372991390984729e-05, 6.8057161403857e-06, 5.394654520894445e-06, 4.252420266544507e-06, 4.840391445595619e-07]}]

	algorithms = list({x['algorithm'] for x in results})
	colors = ['r', 'g']

	for index, algorithm in enumerate(algorithms):
		for result in results:
			if result['algorithm'] == algorithm:
				n_components = result['n_components']

				x = [i for i in range(1, n_components + 1)]
				y = result['explained_variance']

				plt.plot(x, y, c=colors[index], label=algorithm)

	plt.title("SVD: Wine")
	plt.xlabel("No. of Components")
	plt.ylabel("Percent of Explained Variance")
	plt.legend(loc="upper right")
	plt.tight_layout()
	plt.savefig("figures/wine_svd")
	plt.cla()


def adult_svd_explained_variance():
	''' ''' 

	results = [{'algorithm': 'randomized', 'n_components': 10, 'explained_variance': [0.9952330199240069, 0.004752331177381073, 1.4564320321403852e-05, 6.926694029049662e-08, 1.4050933421922794e-08, 8.675856039975017e-10, 6.887180892743038e-11, 3.333662974903899e-11, 2.6952601394698942e-11, 2.3054567864125995e-11]}, {'algorithm': 'arpack', 'n_components': 10, 'explained_variance': [0.995233019924011, 0.00475233117738106, 1.45643203214039e-05, 6.926694029049622e-08, 1.40509334219228e-08, 0.0, 0.0, 0.0, 0.0, 0.0]}]

	algorithms = list({x['algorithm'] for x in results})
	colors = ['r', 'g']

	for index, algorithm in enumerate(algorithms):
		for result in results:
			if result['algorithm'] == algorithm:
				n_components = result['n_components']

				x = [i for i in range(1, n_components + 1)]
				y = result['explained_variance']

				plt.plot(x, y, c=colors[index], label=algorithm)

	plt.title("SVD: Adult")
	plt.xlabel("No. of Components")
	plt.ylabel("Percent of Explained Variance")
	plt.legend(loc="upper right")
	plt.tight_layout()
	plt.savefig("figures/adult_svd")
	plt.cla()


def kmeans_adult_svd():
	''' ''' 

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5896115883606865, 'training_time': 0.25523829460144043, 'distortion': 52462.078733778064, 'inertia': 121333093182588.47}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5896115883606865, 'training_time': 0.27245497703552246, 'distortion': 52462.078733778064, 'inertia': 121333093182588.47}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5580453092477939, 'training_time': 0.21614599227905273, 'distortion': 35750.24571543385, 'inertia': 65086261321941.54}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5580453092477939, 'training_time': 0.29784512519836426, 'distortion': 35750.24571543385, 'inertia': 65086261321941.55}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5666856670137999, 'training_time': 0.23601722717285156, 'distortion': 30536.039302228808, 'inertia': 42544490801510.72}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5666856670137999, 'training_time': 0.25487780570983887, 'distortion': 30536.039302228808, 'inertia': 42544490801510.72}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5440493262438527, 'training_time': 0.31217098236083984, 'distortion': 26122.537684775598, 'inertia': 30533955926425.582}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5440493262438527, 'training_time': 0.37581586837768555, 'distortion': 26122.537684775598, 'inertia': 30533955926425.582}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5556485954960306, 'training_time': 0.3837108612060547, 'distortion': 20303.025002951872, 'inertia': 21905050592221.582}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5556485954960306, 'training_time': 0.4766499996185303, 'distortion': 20303.025002951872, 'inertia': 21905050592221.58}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.556321496694536, 'training_time': 0.42116308212280273, 'distortion': 18525.177254133636, 'inertia': 16215869157050.475}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.556321496694536, 'training_time': 0.5334711074829102, 'distortion': 18525.177254133636, 'inertia': 16215869157050.47}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5514247507432799, 'training_time': 0.38829684257507324, 'distortion': 17140.348975973247, 'inertia': 12538626427227.463}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5514247507432799, 'training_time': 0.4751129150390625, 'distortion': 17140.348975973255, 'inertia': 12538626427227.465}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5466770181055167, 'training_time': 0.5249888896942139, 'distortion': 14862.82066219195, 'inertia': 9751038742012.602}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5466770181055167, 'training_time': 0.6441330909729004, 'distortion': 14862.820662191945, 'inertia': 9751038742012.602}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Adult (SVD) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_svd_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Adult (SVD) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_adult_svd_elbow')
	plt.cla()


def em_adult_svd():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.029237031936645508, 'bic': 675774.3275115318, 'aic': 675757.9953464125}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.07039999961853027, 'bic': 671514.0471889584, 'aic': 671473.2167761603}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.11465096473693848, 'bic': 671286.366639946, 'aic': 671221.0379794692}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.11435389518737793, 'bic': 670161.3610030406, 'aic': 670071.5340948849}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.13783502578735352, 'bic': 670171.2607495327, 'aic': 670056.9355936982}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.20213723182678223, 'bic': 668713.6659302233, 'aic': 668574.8425267099}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.20815801620483398, 'bic': 668623.1505060716, 'aic': 668459.8288548794}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.20855212211608887, 'bic': 668745.8360918019, 'aic': 668558.0161929309}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.24149084091186523, 'bic': 668712.2028957325, 'aic': 668499.8847491826}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.021922826766967773, 'bic': 675774.3275115317, 'aic': 675757.9953464124}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.07897186279296875, 'bic': 672922.3782586892, 'aic': 672889.7139284507}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.1318368911743164, 'bic': 672943.8090898732, 'aic': 672894.8125945155}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.15337300300598145, 'bic': 671809.1729127835, 'aic': 671743.8442523066}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.23813986778259277, 'bic': 671733.5456217158, 'aic': 671651.8847961198}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.2684211730957031, 'bic': 671491.4201073103, 'aic': 671393.427116595}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.2453629970550537, 'bic': 671132.501169885, 'aic': 671018.1760140505}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.2373640537261963, 'bic': 671025.0717975942, 'aic': 670894.4144766404}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.29038119316101074, 'bic': 670839.3574745172, 'aic': 670692.3679884442}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.023104190826416016, 'bic': 675774.3275115317, 'aic': 675757.9953464124}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.07693099975585938, 'bic': 671518.6648379129, 'aic': 671477.8344251148}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.1028597354888916, 'bic': 671260.8022285673, 'aic': 671195.4735680905}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.09970474243164062, 'bic': 670171.7993279076, 'aic': 670081.9724197519}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.15137195587158203, 'bic': 670162.2211444576, 'aic': 670047.895988623}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.29636073112487793, 'bic': 668657.9126512503, 'aic': 668519.0892477368}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.3023369312286377, 'bic': 668610.3883847768, 'aic': 668447.0667335845}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.1793820858001709, 'bic': 668733.6248726442, 'aic': 668545.8049737732}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.20145392417907715, 'bic': 668707.6687394254, 'aic': 668495.3505928755}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.024103164672851562, 'bic': 675774.3275115317, 'aic': 675757.9953464124}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.06482934951782227, 'bic': 671514.2425424515, 'aic': 671473.4121296534}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.1190328598022461, 'bic': 671283.2648128397, 'aic': 671217.9361523628}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.10152292251586914, 'bic': 670174.9385363116, 'aic': 670085.1116281559}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.24584722518920898, 'bic': 668753.4937848677, 'aic': 668639.1686290331}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.2966651916503906, 'bic': 668695.4320669734, 'aic': 668556.60866346}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.22441601753234863, 'bic': 668656.306669232, 'aic': 668492.9850180397}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.2234790325164795, 'bic': 668699.284645558, 'aic': 668511.464746687}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.2545020580291748, 'bic': 668710.9991674031, 'aic': 668498.6810208532}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Adult (SVD) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_adult_svd")
	plt.cla()


def kmeans_wine_svd():
	''' ''' 

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5158235106724537, 'training_time': 0.40070199966430664, 'distortion': 24.23063073753145, 'inertia': 3119172.4407925247}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5158235106724537, 'training_time': 0.08007001876831055, 'distortion': 24.23063073753145, 'inertia': 3119172.4407925247}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.42666008488576523, 'training_time': 0.24015021324157715, 'distortion': 19.517465123704806, 'inertia': 1996826.676173031}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.42666008488576523, 'training_time': 1.5248072147369385, 'distortion': 19.517465123704806, 'inertia': 1996826.676173031}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.3940207379046822, 'training_time': 1.0246188640594482, 'distortion': 16.713833708924145, 'inertia': 1479788.974224105}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.3940207379046822, 'training_time': 0.15581798553466797, 'distortion': 16.713833708924145, 'inertia': 1479788.974224105}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.3666099679353495, 'training_time': 0.2448720932006836, 'distortion': 15.213602984818953, 'inertia': 1219651.360333131}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.3666099679353495, 'training_time': 0.3565711975097656, 'distortion': 15.213602984818953, 'inertia': 1219651.360333131}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.3357920989327605, 'training_time': 0.21376276016235352, 'distortion': 14.005055252164036, 'inertia': 1063552.0720958852}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.3357920989327605, 'training_time': 0.5539610385894775, 'distortion': 14.005055252164036, 'inertia': 1063552.0720958852}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.34361804122808987, 'training_time': 0.25902295112609863, 'distortion': 13.15707496447533, 'inertia': 928616.407801016}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.34361804122808987, 'training_time': 0.26557207107543945, 'distortion': 13.15707496447533, 'inertia': 928616.407801016}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.3303550382038212, 'training_time': 0.2802412509918213, 'distortion': 12.370494157103163, 'inertia': 837940.3591064385}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.3303550382038212, 'training_time': 0.3165409564971924, 'distortion': 12.370494157103163, 'inertia': 837940.3591064384}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.33098447301180717, 'training_time': 0.3120839595794678, 'distortion': 11.920432016574003, 'inertia': 751816.5900274037}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.33098447301180717, 'training_time': 0.38044190406799316, 'distortion': 11.920432016574003, 'inertia': 751816.590027404}]

	algorithms = list({x['algorithm'] for x in scores})
	colors = ['r', 'g']
	line_styles = ['-', ':']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['silhouette_score'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Silhouette Score", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['training_time'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Training Time (s)", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]


	plt.title("K Means: Wine (SVD) \n Silhouette")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_svd_sil')
	plt.cla()

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, algo in enumerate(algorithms):

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['distortion'] for y in scores if y['algorithm'] == algo]
		
		ax1.plot(x, y, color=colors[0], ls=line_styles[index])
		ax1.set_ylabel("Distortion", color=colors[0])
		ax1.set_xlabel("Number of Clusters")

		x = [x['n_clusters'] for x in scores if x['algorithm'] == algo]
		y = [y['inertia'] for y in scores if y['algorithm'] == algo]

		ax2.plot(x, y, color=colors[1], ls=line_styles[index])
		ax2.set_ylabel("Inertia", color=colors[1])

	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
		mlines.Line2D([0], [0], color='k', lw=2, ls=':')]

	legend_labels = [algorithms[0], algorithms[1]]

	plt.title("K Means: Wine (SVD) \n Elbow")
	plt.legend(legend_items, legend_labels, loc="upper right")
	plt.tight_layout()
	plt.savefig('figures/km_wine_svd_elbow')
	plt.cla()


def em_wine_svd():
	''' ''' 

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.01922607421875, 'bic': 70893.90495684813, 'aic': 70862.60637204302}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.03324103355407715, 'bic': 70451.59436992633, 'aic': 70382.7374833551}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.05013108253479004, 'bic': 70454.20993463213, 'aic': 70347.79474629476}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.06633210182189941, 'bic': 70421.12945422815, 'aic': 70277.15596412466}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.11476874351501465, 'bic': 70424.03081017434, 'aic': 70242.49901830472}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.1230309009552002, 'bic': 70463.89376081605, 'aic': 70244.8036671803}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.11742305755615234, 'bic': 70476.06596975245, 'aic': 70219.41757435058}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.09402799606323242, 'bic': 70456.86216646347, 'aic': 70162.65546929545}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.22437667846679688, 'bic': 70511.83226247574, 'aic': 70180.0672635416}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.022765636444091797, 'bic': 70893.90495684813, 'aic': 70862.60637204302}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.02801203727722168, 'bic': 70861.25504240235, 'aic': 70811.17730671418}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.05924797058105469, 'bic': 70903.89963987198, 'aic': 70835.04275330075}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.08162999153137207, 'bic': 70857.93002839034, 'aic': 70770.29399093604}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.0943148136138916, 'bic': 70713.14425832444, 'aic': 70606.72906998706}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.17379975318908691, 'bic': 70714.50645199676, 'aic': 70589.31211277633}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.17460203170776367, 'bic': 70623.38321420446, 'aic': 70479.40972410096}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.18932318687438965, 'bic': 70646.68316171576, 'aic': 70483.9305207292}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.15323686599731445, 'bic': 70771.93358134407, 'aic': 70590.40178947445}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.019244909286499023, 'bic': 70891.50842760483, 'aic': 70866.46955976075}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.028753042221069336, 'bic': 70437.93875265302, 'aic': 70381.60130000382}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.0418698787689209, 'bic': 70442.54582043443, 'aic': 70354.90978298013}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.047911882400512695, 'bic': 70407.11076333748, 'aic': 70288.17614107807}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.06882214546203613, 'bic': 70405.18015622313, 'aic': 70254.9469491586}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.10651969909667969, 'bic': 70417.37815481448, 'aic': 70235.84636294485}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.11318778991699219, 'bic': 70436.83973888506, 'aic': 70224.00936221033}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.10202908515930176, 'bic': 70463.15464994776, 'aic': 70219.02568846791}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.08488702774047852, 'bic': 70436.80950624266, 'aic': 70161.38195995771}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.018665313720703125, 'bic': 75661.95465780237, 'aic': 75643.1755069193}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.01805400848388672, 'bic': 72947.61420485038, 'aic': 72903.79618612323}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.046681880950927734, 'bic': 71939.90019032422, 'aic': 71871.04330375299}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.03167295455932617, 'bic': 71209.50487787713, 'aic': 71115.6091234618}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.049067020416259766, 'bic': 70980.17510820343, 'aic': 70861.24048594403}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.05364584922790527, 'bic': 70905.69192874782, 'aic': 70761.71843864433}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.05297994613647461, 'bic': 70809.05236322306, 'aic': 70640.04000527548}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.06753110885620117, 'bic': 70814.00555292745, 'aic': 70619.95432713578}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.09573507308959961, 'bic': 70721.17705263353, 'aic': 70502.08695899778}]

	covariances = list({x['covariance'] for x in results})

	colors = ['r', 'g', 'b', 'c']

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx() 

	for index, covariance in enumerate(covariances):

		x = [x['n_components'] for x in results if x['covariance'] == covariance]
		y = [y['aic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls="-")

		y = [y['bic'] for y in results if y['covariance'] == covariance]

		ax1.plot(x, y, c=colors[index], ls=":")

		y = [y['training_time'] for y in results if y['covariance'] == covariance]

		ax2.plot(x, y, c=colors[index], ls="-.", lw=1)


	legend_items = [mlines.Line2D([0], [0], color='k', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='k', lw=2, ls=':'),
					mlines.Line2D([0], [0], color='k', lw=2, ls='-.'),
					mlines.Line2D([0], [0], color='r', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='g', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='b', lw=2, ls='-'),
					mlines.Line2D([0], [0], color='c', lw=2, ls='-')]

	legend_labels = ['AIC', 'BIC', 'training_time', covariances[0], covariances[1], covariances[2], covariances[3]]

	
	ax1.set_xlabel("No. of Components")
	ax1.set_ylabel("AIC/BIC score")
	ax2.set_ylabel("Training Time (s)")

	plt.title("Expectation Maximization: Wine (SVD) \n AIC/BIC")
	plt.legend(legend_items, legend_labels, loc="upper left")
	plt.tight_layout()
	plt.savefig("figures/em_wine_svd")
	plt.cla()

def adult_ica_kurtosis():
	''' ''' 

	results = [{'n_components': 1, 'algorithm': 'parallel', 'avg_kurtosis': -1.3407631440073555}, {'n_components': 2, 'algorithm': 'parallel', 'avg_kurtosis': -0.5121873114439119}, {'n_components': 3, 'algorithm': 'parallel', 'avg_kurtosis': 1.878688407391543}, {'n_components': 4, 'algorithm': 'parallel', 'avg_kurtosis': 2.9826877822338944}, {'n_components': 5, 'algorithm': 'parallel', 'avg_kurtosis': 3.865547393777298}, {'n_components': 6, 'algorithm': 'parallel', 'avg_kurtosis': 4.812628433275557}, {'n_components': 7, 'algorithm': 'parallel', 'avg_kurtosis': 4.629307574359039}, {'n_components': 8, 'algorithm': 'parallel', 'avg_kurtosis': 6.530780181394142}, {'n_components': 9, 'algorithm': 'parallel', 'avg_kurtosis': 6.877805297798172}, {'n_components': 1, 'algorithm': 'deflation', 'avg_kurtosis': -1.3407631440073555}, {'n_components': 2, 'algorithm': 'deflation', 'avg_kurtosis': -0.5133128017819938}, {'n_components': 3, 'algorithm': 'deflation', 'avg_kurtosis': 1.9507661308457802}, {'n_components': 4, 'algorithm': 'deflation', 'avg_kurtosis': 2.7869411172508554}, {'n_components': 5, 'algorithm': 'deflation', 'avg_kurtosis': 3.604519512595003}, {'n_components': 6, 'algorithm': 'deflation', 'avg_kurtosis': 4.761494682521484}, {'n_components': 7, 'algorithm': 'deflation', 'avg_kurtosis': 4.373955864483118}, {'n_components': 8, 'algorithm': 'deflation', 'avg_kurtosis': 6.447769138538035}, {'n_components': 9, 'algorithm': 'deflation', 'avg_kurtosis': 6.504615490571031}]

	algorithms = list({x['algorithm'] for x in results})

	colors = ['r', 'g']

	for algorithm in algorithms:

		x = [x['n_components'] for x in results if x['algorithm'] == algorithm]
		y = [y['avg_kurtosis'] for y in results if y['algorithm'] == algorithm]

		plt.plot(x, y, label=algorithm)

	plt.title("Adult (ICA)")
	plt.xlabel("No. of Components")
	plt.ylabel("Avg Kurtosis of Components")
	plt.legend(loc="upper right")
	plt.tight_layout()
	plt.savefig("figures/adult_ica")
	plt.cla()


def wine_ica_kurtosis():
	''' ''' 

	results = [{'n_components': 1, 'algorithm': 'parallel', 'avg_kurtosis': 1.053996845239968}, {'n_components': 2, 'algorithm': 'parallel', 'avg_kurtosis': 1.054690177956393}, {'n_components': 3, 'algorithm': 'parallel', 'avg_kurtosis': 1.4249460767877828}, {'n_components': 4, 'algorithm': 'parallel', 'avg_kurtosis': 5.02518171946973}, {'n_components': 5, 'algorithm': 'parallel', 'avg_kurtosis': 6.291043540539038}, {'n_components': 6, 'algorithm': 'parallel', 'avg_kurtosis': 8.187794798599617}, {'n_components': 7, 'algorithm': 'parallel', 'avg_kurtosis': 8.071066920840947}, {'n_components': 8, 'algorithm': 'parallel', 'avg_kurtosis': 7.471051418433604}, {'n_components': 9, 'algorithm': 'parallel', 'avg_kurtosis': 7.406063713663694}, {'n_components': 1, 'algorithm': 'deflation', 'avg_kurtosis': 1.053996845239967}, {'n_components': 2, 'algorithm': 'deflation', 'avg_kurtosis': 0.896862586606902}, {'n_components': 3, 'algorithm': 'deflation', 'avg_kurtosis': 1.3956479869715672}, {'n_components': 4, 'algorithm': 'deflation', 'avg_kurtosis': 5.104492177448957}, {'n_components': 5, 'algorithm': 'deflation', 'avg_kurtosis': 6.674676321187346}, {'n_components': 6, 'algorithm': 'deflation', 'avg_kurtosis': 7.941694636381722}, {'n_components': 7, 'algorithm': 'deflation', 'avg_kurtosis': 8.196475813276688}, {'n_components': 8, 'algorithm': 'deflation', 'avg_kurtosis': 7.0424392188434}, {'n_components': 9, 'algorithm': 'deflation', 'avg_kurtosis': 7.393961553186863}]

	algorithms = list({x['algorithm'] for x in results})

	colors = ['r', 'g']

	for algorithm in algorithms:

		x = [x['n_components'] for x in results if x['algorithm'] == algorithm]
		y = [y['avg_kurtosis'] for y in results if y['algorithm'] == algorithm]

		plt.plot(x, y, label=algorithm)

	plt.title("Wine (ICA)")
	plt.xlabel("No. of Components")
	plt.ylabel("Avg Kurtosis of Components")
	plt.legend(loc="upper right")
	plt.tight_layout()
	plt.savefig("figures/wine_ica")
	plt.cla()

def adult_pca(): 


	results = [{'n_components': 1, 'reconstruction_error': 0.9580307847490702}, {'n_components': 2, 'reconstruction_error': 0.9301378850160402}, {'n_components': 3, 'reconstruction_error': 0.9060268977601845}, {'n_components': 4, 'reconstruction_error': 0.8832987294280475}, {'n_components': 5, 'reconstruction_error': 0.8618334717084564}, {'n_components': 6, 'reconstruction_error': 0.844142794855347}, {'n_components': 7, 'reconstruction_error': 0.8281322333623502}, {'n_components': 8, 'reconstruction_error': 0.8132214056338856}, {'n_components': 9, 'reconstruction_error': 0.7995759770481718}, {'n_components': 10, 'reconstruction_error': 0.7865624344183834}, {'n_components': 11, 'reconstruction_error': 0.7771820680909507}, {'n_components': 12, 'reconstruction_error': 0.7649433314213573}, {'n_components': 13, 'reconstruction_error': 0.7530489223166292}, {'n_components': 14, 'reconstruction_error': 0.7432327304035303}, {'n_components': 15, 'reconstruction_error': 0.7324253910684817}, {'n_components': 16, 'reconstruction_error': 0.7208187901106657}, {'n_components': 17, 'reconstruction_error': 0.710091010771061}, {'n_components': 18, 'reconstruction_error': 0.6999359042633194}, {'n_components': 19, 'reconstruction_error': 0.6893101979701503}, {'n_components': 20, 'reconstruction_error': 0.6793536362659355}, {'n_components': 21, 'reconstruction_error': 0.668948086710663}, {'n_components': 22, 'reconstruction_error': 0.6606976504797468}, {'n_components': 23, 'reconstruction_error': 0.6489494204225571}, {'n_components': 24, 'reconstruction_error': 0.639104225249256}, {'n_components': 25, 'reconstruction_error': 0.628664874015873}, {'n_components': 26, 'reconstruction_error': 0.6192881468581836}, {'n_components': 27, 'reconstruction_error': 0.6083520987245481}, {'n_components': 28, 'reconstruction_error': 0.5992937583193962}, {'n_components': 29, 'reconstruction_error': 0.589504642990106}, {'n_components': 30, 'reconstruction_error': 0.5784215762900121}, {'n_components': 31, 'reconstruction_error': 0.56952103573166}, {'n_components': 32, 'reconstruction_error': 0.5596872693178688}, {'n_components': 33, 'reconstruction_error': 0.5498320577181028}, {'n_components': 34, 'reconstruction_error': 0.5410420906018734}, {'n_components': 35, 'reconstruction_error': 0.530165995982477}, {'n_components': 36, 'reconstruction_error': 0.520464140468378}, {'n_components': 37, 'reconstruction_error': 0.5115393397583029}, {'n_components': 38, 'reconstruction_error': 0.5010219987452932}, {'n_components': 39, 'reconstruction_error': 0.4921049753297943}, {'n_components': 40, 'reconstruction_error': 0.4825203975835944}, {'n_components': 41, 'reconstruction_error': 0.472593342987543}, {'n_components': 42, 'reconstruction_error': 0.46361754985517056}, {'n_components': 43, 'reconstruction_error': 0.45328080512962926}, {'n_components': 44, 'reconstruction_error': 0.4449485670135687}, {'n_components': 45, 'reconstruction_error': 0.4347237919720876}, {'n_components': 46, 'reconstruction_error': 0.42517694248318527}, {'n_components': 47, 'reconstruction_error': 0.4157752047711945}, {'n_components': 48, 'reconstruction_error': 0.40617528680087994}, {'n_components': 49, 'reconstruction_error': 0.3968824926993091}, {'n_components': 50, 'reconstruction_error': 0.38713222128838826}, {'n_components': 51, 'reconstruction_error': 0.37809543872092555}, {'n_components': 52, 'reconstruction_error': 0.3686472246410119}, {'n_components': 53, 'reconstruction_error': 0.35944949927430797}, {'n_components': 54, 'reconstruction_error': 0.34981298756797796}, {'n_components': 55, 'reconstruction_error': 0.340336460255983}, {'n_components': 56, 'reconstruction_error': 0.331044984932631}, {'n_components': 57, 'reconstruction_error': 0.3217319266267711}, {'n_components': 58, 'reconstruction_error': 0.3125506413523508}, {'n_components': 59, 'reconstruction_error': 0.303253639112763}, {'n_components': 60, 'reconstruction_error': 0.2936728904458082}, {'n_components': 61, 'reconstruction_error': 0.2846583105320788}, {'n_components': 62, 'reconstruction_error': 0.2753145692187069}, {'n_components': 63, 'reconstruction_error': 0.2654594936724849}, {'n_components': 64, 'reconstruction_error': 0.256234101610484}, {'n_components': 65, 'reconstruction_error': 0.2473280261213009}, {'n_components': 66, 'reconstruction_error': 0.2380066924563343}, {'n_components': 67, 'reconstruction_error': 0.229286001802209}, {'n_components': 68, 'reconstruction_error': 0.2198861070639747}, {'n_components': 69, 'reconstruction_error': 0.21058576425137854}, {'n_components': 70, 'reconstruction_error': 0.20181971337482654}, {'n_components': 71, 'reconstruction_error': 0.19200590721574484}, {'n_components': 72, 'reconstruction_error': 0.1833953538324119}, {'n_components': 73, 'reconstruction_error': 0.1737548014038412}, {'n_components': 74, 'reconstruction_error': 0.16504397503594823}, {'n_components': 75, 'reconstruction_error': 0.15617915527860585}, {'n_components': 76, 'reconstruction_error': 0.14675871364023635}, {'n_components': 77, 'reconstruction_error': 0.13839780079123223}, {'n_components': 78, 'reconstruction_error': 0.12901132027010523}, {'n_components': 79, 'reconstruction_error': 0.12014124952241752}, {'n_components': 80, 'reconstruction_error': 0.11162496392472165}, {'n_components': 81, 'reconstruction_error': 0.10279536699352969}, {'n_components': 82, 'reconstruction_error': 0.09508905382788126}, {'n_components': 83, 'reconstruction_error': 0.08554596483249305}, {'n_components': 84, 'reconstruction_error': 0.07746472291604044}, {'n_components': 85, 'reconstruction_error': 0.06980556101888381}, {'n_components': 86, 'reconstruction_error': 0.06175744451191508}, {'n_components': 87, 'reconstruction_error': 0.05434929164755603}, {'n_components': 88, 'reconstruction_error': 0.04707106323376237}, {'n_components': 89, 'reconstruction_error': 0.04024162100304194}, {'n_components': 90, 'reconstruction_error': 0.03355648705037205}, {'n_components': 91, 'reconstruction_error': 0.027454161481240854}, {'n_components': 92, 'reconstruction_error': 0.021688397876383658}, {'n_components': 93, 'reconstruction_error': 0.01614952694988553}, {'n_components': 94, 'reconstruction_error': 0.011091886987191223}, {'n_components': 95, 'reconstruction_error': 0.006516635661228246}, {'n_components': 96, 'reconstruction_error': 0.0026222571129356914}, {'n_components': 97, 'reconstruction_error': 0.0001836642774953911}, {'n_components': 98, 'reconstruction_error': 4.9927149141199134e-30}, {'n_components': 99, 'reconstruction_error': 4.983518112468809e-30}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.title("Adult (PCA)")
	plt.xlabel("No. of Components")
	plt.ylabel("Reconstruction Error")
	plt.tight_layout()
	plt.savefig("figures/adult_pca")
	plt.cla()


def wine_pca():
	''' '''

	results = [{'n_components': 1, 'reconstruction_error': 0.7308050568513736}, {'n_components': 2, 'reconstruction_error': 0.5730592390525808}, {'n_components': 3, 'reconstruction_error': 0.4524203755025463}, {'n_components': 4, 'reconstruction_error': 0.35049645411595504}, {'n_components': 5, 'reconstruction_error': 0.25466763914265755}, {'n_components': 6, 'reconstruction_error': 0.16816264949141096}, {'n_components': 7, 'reconstruction_error': 0.09731472434025153}, {'n_components': 8, 'reconstruction_error': 0.039363449234619756}, {'n_components': 9, 'reconstruction_error': 0.008592893195206614}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.title("Wine (PCA)")
	plt.xlabel("No. of Components")
	plt.ylabel("Reconstruction Error")
	plt.tight_layout()
	plt.savefig("figures/wine_pca")
	plt.cla()


def nn_3d(): 
	''' ''' 
	results = [{'layer_1': 1, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 0.09032487869262695, 'iterations': 17}, {'layer_1': 1, 'layer_2': 2, 'accuracy': 0.4620758483033932, 'training_time': 0.9772727489471436, 'iterations': 217}, {'layer_1': 1, 'layer_2': 3, 'accuracy': 0.46407185628742514, 'training_time': 6.036705017089844, 'iterations': 1497}, {'layer_1': 1, 'layer_2': 4, 'accuracy': 0.48602794411177647, 'training_time': 2.283704996109009, 'iterations': 550}, {'layer_1': 1, 'layer_2': 5, 'accuracy': 0.4660678642714571, 'training_time': 4.147724151611328, 'iterations': 961}, {'layer_1': 1, 'layer_2': 6, 'accuracy': 0.47305389221556887, 'training_time': 2.606400966644287, 'iterations': 621}, {'layer_1': 1, 'layer_2': 7, 'accuracy': 0.47105788423153694, 'training_time': 6.4673449993133545, 'iterations': 1271}, {'layer_1': 1, 'layer_2': 8, 'accuracy': 0.46407185628742514, 'training_time': 1.2690129280090332, 'iterations': 259}, {'layer_1': 1, 'layer_2': 9, 'accuracy': 0.47005988023952094, 'training_time': 3.640263319015503, 'iterations': 682}, {'layer_1': 2, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 0.6037530899047852, 'iterations': 89}, {'layer_1': 2, 'layer_2': 2, 'accuracy': 0.4930139720558882, 'training_time': 3.5915029048919678, 'iterations': 920}, {'layer_1': 2, 'layer_2': 3, 'accuracy': 0.4620758483033932, 'training_time': 1.094146966934204, 'iterations': 228}, {'layer_1': 2, 'layer_2': 4, 'accuracy': 0.4880239520958084, 'training_time': 6.04141092300415, 'iterations': 1609}, {'layer_1': 2, 'layer_2': 5, 'accuracy': 0.46706586826347307, 'training_time': 3.5221519470214844, 'iterations': 851}, {'layer_1': 2, 'layer_2': 6, 'accuracy': 0.4810379241516966, 'training_time': 8.845054388046265, 'iterations': 1695}, {'layer_1': 2, 'layer_2': 7, 'accuracy': 0.4750499001996008, 'training_time': 7.849733829498291, 'iterations': 1308}, {'layer_1': 2, 'layer_2': 8, 'accuracy': 0.4880239520958084, 'training_time': 4.734203815460205, 'iterations': 1162}, {'layer_1': 2, 'layer_2': 9, 'accuracy': 0.48403193612774453, 'training_time': 12.620036840438843, 'iterations': 2159}, {'layer_1': 3, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 0.10611414909362793, 'iterations': 18}, {'layer_1': 3, 'layer_2': 2, 'accuracy': 0.46107784431137727, 'training_time': 1.3841321468353271, 'iterations': 262}, {'layer_1': 3, 'layer_2': 3, 'accuracy': 0.47105788423153694, 'training_time': 3.52181077003479, 'iterations': 463}, {'layer_1': 3, 'layer_2': 4, 'accuracy': 0.48902195608782434, 'training_time': 6.964730262756348, 'iterations': 1722}, {'layer_1': 3, 'layer_2': 5, 'accuracy': 0.49800399201596807, 'training_time': 4.674324989318848, 'iterations': 988}, {'layer_1': 3, 'layer_2': 6, 'accuracy': 0.49101796407185627, 'training_time': 3.2475430965423584, 'iterations': 700}, {'layer_1': 3, 'layer_2': 7, 'accuracy': 0.4940119760479042, 'training_time': 8.920577049255371, 'iterations': 1582}, {'layer_1': 3, 'layer_2': 8, 'accuracy': 0.48602794411177647, 'training_time': 15.582042217254639, 'iterations': 2977}, {'layer_1': 3, 'layer_2': 9, 'accuracy': 0.48602794411177647, 'training_time': 3.113574981689453, 'iterations': 778}, {'layer_1': 4, 'layer_2': 1, 'accuracy': 0.4590818363273453, 'training_time': 3.536159038543701, 'iterations': 540}, {'layer_1': 4, 'layer_2': 2, 'accuracy': 0.4820359281437126, 'training_time': 2.0600697994232178, 'iterations': 451}, {'layer_1': 4, 'layer_2': 3, 'accuracy': 0.49700598802395207, 'training_time': 8.132596254348755, 'iterations': 1822}, {'layer_1': 4, 'layer_2': 4, 'accuracy': 0.4930139720558882, 'training_time': 2.206561803817749, 'iterations': 413}, {'layer_1': 4, 'layer_2': 5, 'accuracy': 0.47704590818363274, 'training_time': 8.40475583076477, 'iterations': 1806}, {'layer_1': 4, 'layer_2': 6, 'accuracy': 0.49600798403193613, 'training_time': 5.895766973495483, 'iterations': 1313}, {'layer_1': 4, 'layer_2': 7, 'accuracy': 0.49101796407185627, 'training_time': 3.734257221221924, 'iterations': 805}, {'layer_1': 4, 'layer_2': 8, 'accuracy': 0.49201596806387227, 'training_time': 7.324709892272949, 'iterations': 1512}, {'layer_1': 4, 'layer_2': 9, 'accuracy': 0.49600798403193613, 'training_time': 13.485341310501099, 'iterations': 2495}, {'layer_1': 5, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 0.07919192314147949, 'iterations': 17}, {'layer_1': 5, 'layer_2': 2, 'accuracy': 0.499001996007984, 'training_time': 5.239800930023193, 'iterations': 1325}, {'layer_1': 5, 'layer_2': 3, 'accuracy': 0.48003992015968067, 'training_time': 3.252802848815918, 'iterations': 653}, {'layer_1': 5, 'layer_2': 4, 'accuracy': 0.4630738522954092, 'training_time': 1.3745450973510742, 'iterations': 201}, {'layer_1': 5, 'layer_2': 5, 'accuracy': 0.48602794411177647, 'training_time': 2.4901928901672363, 'iterations': 501}, {'layer_1': 5, 'layer_2': 6, 'accuracy': 0.4820359281437126, 'training_time': 10.06949782371521, 'iterations': 2150}, {'layer_1': 5, 'layer_2': 7, 'accuracy': 0.4750499001996008, 'training_time': 9.401965141296387, 'iterations': 2022}, {'layer_1': 5, 'layer_2': 8, 'accuracy': 0.47704590818363274, 'training_time': 5.476380109786987, 'iterations': 1219}, {'layer_1': 5, 'layer_2': 9, 'accuracy': 0.4940119760479042, 'training_time': 11.878022909164429, 'iterations': 2260}, {'layer_1': 6, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 0.0758368968963623, 'iterations': 17}, {'layer_1': 6, 'layer_2': 2, 'accuracy': 0.4620758483033932, 'training_time': 0.07061886787414551, 'iterations': 15}, {'layer_1': 6, 'layer_2': 3, 'accuracy': 0.48902195608782434, 'training_time': 9.228090047836304, 'iterations': 1979}, {'layer_1': 6, 'layer_2': 4, 'accuracy': 0.4870259481037924, 'training_time': 12.892588138580322, 'iterations': 2821}, {'layer_1': 6, 'layer_2': 5, 'accuracy': 0.48502994011976047, 'training_time': 11.501774787902832, 'iterations': 2572}, {'layer_1': 6, 'layer_2': 6, 'accuracy': 0.49201596806387227, 'training_time': 15.022615194320679, 'iterations': 1478}, {'layer_1': 6, 'layer_2': 7, 'accuracy': 0.49101796407185627, 'training_time': 9.381207942962646, 'iterations': 1694}, {'layer_1': 6, 'layer_2': 8, 'accuracy': 0.4880239520958084, 'training_time': 14.296661853790283, 'iterations': 2690}, {'layer_1': 6, 'layer_2': 9, 'accuracy': 0.49101796407185627, 'training_time': 14.198133945465088, 'iterations': 3033}, {'layer_1': 7, 'layer_2': 1, 'accuracy': 0.4810379241516966, 'training_time': 1.273055076599121, 'iterations': 291}, {'layer_1': 7, 'layer_2': 2, 'accuracy': 0.47704590818363274, 'training_time': 1.0020079612731934, 'iterations': 236}, {'layer_1': 7, 'layer_2': 3, 'accuracy': 0.4870259481037924, 'training_time': 7.341955661773682, 'iterations': 1657}, {'layer_1': 7, 'layer_2': 4, 'accuracy': 0.5029940119760479, 'training_time': 6.565144062042236, 'iterations': 1414}, {'layer_1': 7, 'layer_2': 5, 'accuracy': 0.48502994011976047, 'training_time': 12.01989197731018, 'iterations': 2615}, {'layer_1': 7, 'layer_2': 6, 'accuracy': 0.4780439121756487, 'training_time': 16.04697895050049, 'iterations': 3385}, {'layer_1': 7, 'layer_2': 7, 'accuracy': 0.49101796407185627, 'training_time': 13.205141067504883, 'iterations': 2707}, {'layer_1': 7, 'layer_2': 8, 'accuracy': 0.48403193612774453, 'training_time': 21.87532114982605, 'iterations': 4635}, {'layer_1': 7, 'layer_2': 9, 'accuracy': 0.5059880239520959, 'training_time': 13.309131860733032, 'iterations': 2693}, {'layer_1': 8, 'layer_2': 1, 'accuracy': 0.4620758483033932, 'training_time': 2.5370349884033203, 'iterations': 473}, {'layer_1': 8, 'layer_2': 2, 'accuracy': 0.48902195608782434, 'training_time': 8.385915040969849, 'iterations': 2022}, {'layer_1': 8, 'layer_2': 3, 'accuracy': 0.47604790419161674, 'training_time': 6.288861036300659, 'iterations': 1339}, {'layer_1': 8, 'layer_2': 4, 'accuracy': 0.469061876247505, 'training_time': 4.648652791976929, 'iterations': 713}, {'layer_1': 8, 'layer_2': 5, 'accuracy': 0.47305389221556887, 'training_time': 5.076993942260742, 'iterations': 984}, {'layer_1': 8, 'layer_2': 6, 'accuracy': 0.4930139720558882, 'training_time': 13.45226788520813, 'iterations': 2772}, {'layer_1': 8, 'layer_2': 7, 'accuracy': 0.499001996007984, 'training_time': 17.687772035598755, 'iterations': 3997}, {'layer_1': 8, 'layer_2': 8, 'accuracy': 0.501996007984032, 'training_time': 23.63360095024109, 'iterations': 4908}, {'layer_1': 8, 'layer_2': 9, 'accuracy': 0.48602794411177647, 'training_time': 12.871636867523193, 'iterations': 2397}, {'layer_1': 9, 'layer_2': 1, 'accuracy': 0.49700598802395207, 'training_time': 4.853816032409668, 'iterations': 862}, {'layer_1': 9, 'layer_2': 2, 'accuracy': 0.48902195608782434, 'training_time': 16.404805898666382, 'iterations': 3323}, {'layer_1': 9, 'layer_2': 3, 'accuracy': 0.48502994011976047, 'training_time': 7.7639899253845215, 'iterations': 1463}, {'layer_1': 9, 'layer_2': 4, 'accuracy': 0.4880239520958084, 'training_time': 18.820865869522095, 'iterations': 3190}, {'layer_1': 9, 'layer_2': 5, 'accuracy': 0.49001996007984033, 'training_time': 5.086238861083984, 'iterations': 1044}, {'layer_1': 9, 'layer_2': 6, 'accuracy': 0.4820359281437126, 'training_time': 27.916048049926758, 'iterations': 5022}, {'layer_1': 9, 'layer_2': 7, 'accuracy': 0.49600798403193613, 'training_time': 23.022789239883423, 'iterations': 3981}, {'layer_1': 9, 'layer_2': 8, 'accuracy': 0.4870259481037924, 'training_time': 20.188467979431152, 'iterations': 2931}, {'layer_1': 9, 'layer_2': 9, 'accuracy': 0.49800399201596807, 'training_time': 21.165727853775024, 'iterations': 2214}]

	max_layer_1 = max([x['layer_1'] for x in results])
	max_layer_2 = max([x['layer_2'] for x in results])

	ordered = [[0 for i in range(1, max_layer_1 + 1)] for j in range(1, max_layer_2 + 1)]

	for result in results: 
		ordered[result['layer_1'] - 1][result['layer_2'] - 1] = result['accuracy']

	# print(ordered)

	x = y = np.arange(1, len(ordered) + 1, 1)
	X, Y = np.meshgrid(x, y)

	fig, ax = plt.subplots()

	for i in range(0, max_layer_1):
	    for j in range(0, max_layer_2):
	        text = ax.text(j, i, round(ordered[i][j], 2),
	                       ha="center", va="center", color="w")


	ax.set_xticks([i for i in range(max_layer_1)])
	ax.set_xticklabels([i + 1 for i in range(max_layer_1)])
	ax.set_yticks([i for i in range(max_layer_2)])
	ax.set_yticklabels([i + 1 for i in range(max_layer_2)])
	ax.imshow(ordered)
	plt.title("Neural Network Tuning\nAccuracy")
	plt.xlabel("Number of nodes in Layer 1")
	plt.ylabel("Number of nodes in Layer 2")
	plt.tight_layout()
	plt.savefig("figures/nn_accuracy")
	plt.cla()


	ordered = [[0 for i in range(1, max_layer_1 + 1)] for j in range(1, max_layer_2 + 1)]

	for result in results: 
		ordered[result['layer_1'] - 1][result['layer_2'] - 1] = result['training_time']


	x = y = np.arange(1, len(ordered) + 1, 1)
	X, Y = np.meshgrid(x, y)

	fig, ax = plt.subplots()

	for i in range(0, max_layer_1):
	    for j in range(0, max_layer_2):
	        text = ax.text(j, i, round(ordered[i][j], 2),
	                       ha="center", va="center", color="w")


	ax.set_xticks([i for i in range(max_layer_1)])
	ax.set_xticklabels([i + 1 for i in range(max_layer_1)])
	ax.set_yticks([i for i in range(max_layer_2)])
	ax.set_yticklabels([i + 1 for i in range(max_layer_2)])
	ax.imshow(ordered)
	plt.title("Neural Network Tuning\nTraining Time")
	plt.xlabel("Number of nodes in Layer 1")
	plt.ylabel("Number of nodes in Layer 2")
	plt.tight_layout()
	# plt.show()
	plt.savefig("figures/nn_training_time")
	plt.cla()






if __name__ == '__main__':

	#### Adult Dataset
	# kmeans_adult()
	# em_adult()
	# adult_pca()
	# kmeans_adult_pca()
	# em_adult_pca()
	# adult_ica_kurtosis()
	# kmeans_adult_ica()
	# em_adult_ica()
	# kmeans_adult_rand()
	# em_adult_rand()
	# adult_reconstruction_error()
	# adult_svd_explained_variance()
	# kmeans_adult_svd()
	# em_adult_svd()





	#### Wine Dataset
	# kmeans_wine()
	# em_wine()
	# wine_pca()
	# kmeans_wine_pca()
	# em_wine_pca()
	# wine_ica_kurtosis()
	# kmeans_wine_ica()
	# em_wine_ica()
	# kmeans_wine_rand()
	# em_wine_rand()
	# wine_reconstruction_error()
	# wine_svd_explained_variance()
	# kmeans_wine_svd()
	# em_wine_svd()
	nn_3d()

	pass


