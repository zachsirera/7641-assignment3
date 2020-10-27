import matplotlib.lines as mlines
import matplotlib.pyplot as plt

import pandas as pd 

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

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.05799656824078494, 'training_time': 0.5987241268157959, 'distortion': 8.103721227063746, 'inertia': 2585989.79140554}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.05799656824078494, 'training_time': 0.4446260929107666, 'distortion': 8.103721227063746, 'inertia': 2585989.79140554}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.05544977884223554, 'training_time': 2.3404102325439453, 'distortion': 7.480934279396567, 'inertia': 2262174.92092193}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.05544977884223554, 'training_time': 2.3355300426483154, 'distortion': 7.480934279396567, 'inertia': 2262174.92092193}, {'n_clusters': 22, 'algorithm': 'full', 'silhouette_score': 0.07557576170224599, 'training_time': 3.83530592918396, 'distortion': 7.064970175757363, 'inertia': 2005684.321075195}, {'n_clusters': 22, 'algorithm': 'elkan', 'silhouette_score': 0.07557576170224599, 'training_time': 3.6079840660095215, 'distortion': 7.064970175757363, 'inertia': 2005684.321075195}, {'n_clusters': 32, 'algorithm': 'full', 'silhouette_score': 0.09267434134231087, 'training_time': 5.184216022491455, 'distortion': 6.74943769869047, 'inertia': 1753312.57879714}, {'n_clusters': 32, 'algorithm': 'elkan', 'silhouette_score': 0.09267434134231087, 'training_time': 5.689284086227417, 'distortion': 6.749437698690472, 'inertia': 1753312.57879714}, {'n_clusters': 42, 'algorithm': 'full', 'silhouette_score': 0.08893776466298922, 'training_time': 6.205020904541016, 'distortion': 6.5124625443221085, 'inertia': 1527021.7831085117}, {'n_clusters': 42, 'algorithm': 'elkan', 'silhouette_score': 0.08893776466298922, 'training_time': 7.137336254119873, 'distortion': 6.5124625443221085, 'inertia': 1527021.7831085117}, {'n_clusters': 52, 'algorithm': 'full', 'silhouette_score': 0.11126952895070394, 'training_time': 6.72537899017334, 'distortion': 6.116859783963075, 'inertia': 1285588.934062173}, {'n_clusters': 52, 'algorithm': 'elkan', 'silhouette_score': 0.11126952895070394, 'training_time': 6.284549951553345, 'distortion': 6.116859783963075, 'inertia': 1285588.934062173}, {'n_clusters': 62, 'algorithm': 'full', 'silhouette_score': 0.14941587205671503, 'training_time': 8.829002857208252, 'distortion': 5.692231656248377, 'inertia': 1051278.2138979833}, {'n_clusters': 62, 'algorithm': 'elkan', 'silhouette_score': 0.14941587205671503, 'training_time': 7.931082010269165, 'distortion': 5.692231656248377, 'inertia': 1051278.2138979833}, {'n_clusters': 72, 'algorithm': 'full', 'silhouette_score': 0.16211255527491772, 'training_time': 13.535096168518066, 'distortion': 5.327863047660526, 'inertia': 882151.0462508178}, {'n_clusters': 72, 'algorithm': 'elkan', 'silhouette_score': 0.16211255527491772, 'training_time': 10.73881721496582, 'distortion': 5.327863047660526, 'inertia': 882151.0462508178}, {'n_clusters': 82, 'algorithm': 'full', 'silhouette_score': 0.1775459338549726, 'training_time': 16.60728907585144, 'distortion': 5.053738196529259, 'inertia': 772091.2438145321}, {'n_clusters': 82, 'algorithm': 'elkan', 'silhouette_score': 0.1775459338549726, 'training_time': 10.246856212615967, 'distortion': 5.053738196529259, 'inertia': 772091.2438145322}, {'n_clusters': 92, 'algorithm': 'full', 'silhouette_score': 0.18572235040148874, 'training_time': 15.16405701637268, 'distortion': 4.738853544128445, 'inertia': 698162.0834879723}, {'n_clusters': 92, 'algorithm': 'elkan', 'silhouette_score': 0.18572235040148874, 'training_time': 14.109116792678833, 'distortion': 4.738853544128445, 'inertia': 698162.0834879722}, {'n_clusters': 102, 'algorithm': 'full', 'silhouette_score': 0.1905616431696209, 'training_time': 13.994184255599976, 'distortion': 4.560602548552105, 'inertia': 655416.5046807532}, {'n_clusters': 102, 'algorithm': 'elkan', 'silhouette_score': 0.1905616431696209, 'training_time': 12.57411789894104, 'distortion': 4.560602548552105, 'inertia': 655416.5046807532}, {'n_clusters': 112, 'algorithm': 'full', 'silhouette_score': 0.19164350800761387, 'training_time': 14.442511081695557, 'distortion': 4.471749450245514, 'inertia': 638936.8986978186}, {'n_clusters': 112, 'algorithm': 'elkan', 'silhouette_score': 0.19164350800761387, 'training_time': 13.597150087356567, 'distortion': 4.471749450245512, 'inertia': 638936.8986978186}, {'n_clusters': 122, 'algorithm': 'full', 'silhouette_score': 0.1855410541674519, 'training_time': 15.234061241149902, 'distortion': 4.388329950679426, 'inertia': 621021.6689688542}, {'n_clusters': 122, 'algorithm': 'elkan', 'silhouette_score': 0.1855410541674519, 'training_time': 14.841331958770752, 'distortion': 4.388329950679426, 'inertia': 621021.6689688542}, {'n_clusters': 132, 'algorithm': 'full', 'silhouette_score': 0.19191064384210424, 'training_time': 16.122408866882324, 'distortion': 4.307558406078176, 'inertia': 602684.7011040812}, {'n_clusters': 132, 'algorithm': 'elkan', 'silhouette_score': 0.19191064384210424, 'training_time': 15.73504900932312, 'distortion': 4.307558406078176, 'inertia': 602684.7011040812}, {'n_clusters': 142, 'algorithm': 'full', 'silhouette_score': 0.1995995731504486, 'training_time': 16.686106204986572, 'distortion': 4.239853731648842, 'inertia': 587929.0489823385}, {'n_clusters': 142, 'algorithm': 'elkan', 'silhouette_score': 0.1995995731504486, 'training_time': 16.341345071792603, 'distortion': 4.239853731648842, 'inertia': 587929.0489823384}, {'n_clusters': 152, 'algorithm': 'full', 'silhouette_score': 0.20130173480748503, 'training_time': 17.583635091781616, 'distortion': 4.185256562620854, 'inertia': 576374.6287522869}, {'n_clusters': 152, 'algorithm': 'elkan', 'silhouette_score': 0.20130173480748503, 'training_time': 17.846718072891235, 'distortion': 4.185256562620854, 'inertia': 576374.6287522869}, {'n_clusters': 162, 'algorithm': 'full', 'silhouette_score': 0.20715341779301855, 'training_time': 18.79474425315857, 'distortion': 4.12098762323722, 'inertia': 564676.0737130768}, {'n_clusters': 162, 'algorithm': 'elkan', 'silhouette_score': 0.20715341779301855, 'training_time': 18.945455074310303, 'distortion': 4.12098762323722, 'inertia': 564676.0737130768}, {'n_clusters': 172, 'algorithm': 'full', 'silhouette_score': 0.2074136927276904, 'training_time': 24.223801136016846, 'distortion': 4.060438938947578, 'inertia': 553994.7052882843}, {'n_clusters': 172, 'algorithm': 'elkan', 'silhouette_score': 0.2074136927276904, 'training_time': 20.579617977142334, 'distortion': 4.060438938947578, 'inertia': 553994.7052882843}, {'n_clusters': 182, 'algorithm': 'full', 'silhouette_score': 0.214095765309617, 'training_time': 28.204750061035156, 'distortion': 4.0169757418034555, 'inertia': 542535.6231249071}, {'n_clusters': 182, 'algorithm': 'elkan', 'silhouette_score': 0.214095765309617, 'training_time': 26.204899072647095, 'distortion': 4.0169757418034555, 'inertia': 542535.6231249071}, {'n_clusters': 192, 'algorithm': 'full', 'silhouette_score': 0.2140452376589997, 'training_time': 31.414117097854614, 'distortion': 3.961401325541237, 'inertia': 533076.2334223664}, {'n_clusters': 192, 'algorithm': 'elkan', 'silhouette_score': 0.2140452376589997, 'training_time': 35.38739585876465, 'distortion': 3.961401325541237, 'inertia': 533076.2334223666}]
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
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.40146708488464355, 'bic': 6700629.992413718, 'aic': 6668657.371258575}, {'n_components': 2, 'covariance': 'full', 'training_time': 2.0735161304473877, 'bic': 2614753.82147744, 'aic': 2550800.4124695407}, {'n_components': 3, 'covariance': 'full', 'training_time': 3.016669988632202, 'bic': 1810043.7968503418, 'aic': 1714109.599989686}, {'n_components': 4, 'covariance': 'full', 'training_time': 2.5416979789733887, 'bic': 2723104.3263416984, 'aic': 2595189.341628286}, {'n_components': 5, 'covariance': 'full', 'training_time': 4.2595579624176025, 'bic': -4236391.5593683245, 'aic': -4396287.331934493}, {'n_components': 6, 'covariance': 'full', 'training_time': 6.794951915740967, 'bic': -4218803.752966363, 'aic': -4410680.313385288}, {'n_components': 7, 'covariance': 'full', 'training_time': 6.0338499546051025, 'bic': -7310039.703231066, 'aic': -7533897.051502747}, {'n_components': 8, 'covariance': 'full', 'training_time': 8.0400071144104, 'bic': -8559221.43453189, 'aic': -8815059.570656328}, {'n_components': 9, 'covariance': 'full', 'training_time': 6.1417200565338135, 'bic': -4744824.945035986, 'aic': -5032643.86901318}, {'n_components': 10, 'covariance': 'full', 'training_time': 9.007851123809814, 'bic': -8990192.19885553, 'aic': -9309991.910685482}, {'n_components': 11, 'covariance': 'full', 'training_time': 12.54810118675232, 'bic': -7859011.222677019, 'aic': -8210791.722359726}, {'n_components': 12, 'covariance': 'full', 'training_time': 7.808520078659058, 'bic': -8456649.605437541, 'aic': -8840410.892973004}, {'n_components': 13, 'covariance': 'full', 'training_time': 10.267759799957275, 'bic': -9015028.609648317, 'aic': -9430770.685036536}, {'n_components': 14, 'covariance': 'full', 'training_time': 12.384212017059326, 'bic': -10246982.318030218, 'aic': -10694705.181271194}, {'n_components': 15, 'covariance': 'full', 'training_time': 15.726126909255981, 'bic': -7866886.766137077, 'aic': -8346590.417230809}, {'n_components': 16, 'covariance': 'full', 'training_time': 18.52001404762268, 'bic': -7410716.45594083, 'aic': -7922400.894887318}, {'n_components': 17, 'covariance': 'full', 'training_time': 18.790757179260254, 'bic': -9687000.725683305, 'aic': -10230665.952482551}, {'n_components': 18, 'covariance': 'full', 'training_time': 20.170300006866455, 'bic': -5857242.121422078, 'aic': -6432888.13607408}, {'n_components': 19, 'covariance': 'full', 'training_time': 25.508992910385132, 'bic': -9731694.260732511, 'aic': -10339321.063237268}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.25072312355041504, 'bic': 6700629.992413719, 'aic': 6668657.3712585755}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.4076709747314453, 'bic': 6551998.810107939, 'aic': 6519307.519562846}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.7067902088165283, 'bic': 6522048.987782875, 'aic': 6488639.027847833}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.8942108154296875, 'bic': 6387859.862794078, 'aic': 6353731.233469086}, {'n_components': 5, 'covariance': 'tied', 'training_time': 1.0723528861999512, 'bic': 6290455.629827788, 'aic': 6255608.331112847}, {'n_components': 6, 'covariance': 'tied', 'training_time': 2.475890874862671, 'bic': 6449850.74813376, 'aic': 6414284.7800288685}, {'n_components': 7, 'covariance': 'tied', 'training_time': 1.654353141784668, 'bic': 6286278.671271236, 'aic': 6249994.033776395}, {'n_components': 8, 'covariance': 'tied', 'training_time': 4.642688035964966, 'bic': 6266274.416744567, 'aic': 6229271.109859777}, {'n_components': 9, 'covariance': 'tied', 'training_time': 6.559556007385254, 'bic': 6084463.942569252, 'aic': 6046741.966294512}, {'n_components': 10, 'covariance': 'tied', 'training_time': 7.181944131851196, 'bic': 5810623.00738379, 'aic': 5772182.361719101}, {'n_components': 11, 'covariance': 'tied', 'training_time': 2.94907808303833, 'bic': 6104820.876006191, 'aic': 6065661.560951551}, {'n_components': 12, 'covariance': 'tied', 'training_time': 3.615454912185669, 'bic': 5939957.798262961, 'aic': 5900079.813818373}, {'n_components': 13, 'covariance': 'tied', 'training_time': 3.956489086151123, 'bic': 6063003.116597864, 'aic': 6022406.462763325}, {'n_components': 14, 'covariance': 'tied', 'training_time': 3.6293230056762695, 'bic': 5769304.1662197, 'aic': 5727988.842995212}, {'n_components': 15, 'covariance': 'tied', 'training_time': 8.642136096954346, 'bic': 5316949.381819675, 'aic': 5274915.389205237}, {'n_components': 16, 'covariance': 'tied', 'training_time': 4.083477020263672, 'bic': 5542605.766648941, 'aic': 5499853.104644554}, {'n_components': 17, 'covariance': 'tied', 'training_time': 6.270098924636841, 'bic': 4911236.662375191, 'aic': 4867765.330980855}, {'n_components': 18, 'covariance': 'tied', 'training_time': 6.033170938491821, 'bic': 5259191.562094664, 'aic': 5215001.561310378}, {'n_components': 19, 'covariance': 'tied', 'training_time': 7.158530235290527, 'bic': 4250281.621671042, 'aic': 4205372.951496807}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.1378030776977539, 'bic': 6662596.376643247, 'aic': 6661175.371258574}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.5165209770202637, 'bic': 4514915.331901211, 'aic': 4512065.1544342525}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.5686731338500977, 'bic': 4449235.030661878, 'aic': 4444955.681112633}, {'n_components': 4, 'covariance': 'diag', 'training_time': 1.020371913909912, 'bic': 3910323.415824049, 'aic': 3904614.8941925177}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.8190450668334961, 'bic': 3865136.172242869, 'aic': 3857998.478529052}, {'n_components': 6, 'covariance': 'diag', 'training_time': 1.1707451343536377, 'bic': 3727925.391335895, 'aic': 3719358.525539791}, {'n_components': 7, 'covariance': 'diag', 'training_time': 1.0872540473937988, 'bic': 3850737.4315398256, 'aic': 3840741.393661436}, {'n_components': 8, 'covariance': 'diag', 'training_time': 1.8850088119506836, 'bic': 3666784.743886489, 'aic': 3655359.533925813}, {'n_components': 9, 'covariance': 'diag', 'training_time': 1.2984108924865723, 'bic': 3664703.2589593763, 'aic': 3651848.8769164146}, {'n_components': 10, 'covariance': 'diag', 'training_time': 1.258929967880249, 'bic': 3732922.8009819915, 'aic': 3718639.2468567435}, {'n_components': 11, 'covariance': 'diag', 'training_time': 1.6474230289459229, 'bic': 3629845.880125682, 'aic': 3614133.153918148}, {'n_components': 12, 'covariance': 'diag', 'training_time': 1.4780070781707764, 'bic': 3573559.004135525, 'aic': 3556417.1058457047}, {'n_components': 13, 'covariance': 'diag', 'training_time': 1.917952060699463, 'bic': 3534844.6826471905, 'aic': 3516273.6122750845}, {'n_components': 14, 'covariance': 'diag', 'training_time': 2.943586826324463, 'bic': 3533205.0586312786, 'aic': 3513204.816176886}, {'n_components': 15, 'covariance': 'diag', 'training_time': 2.930137872695923, 'bic': 3407051.1948726294, 'aic': 3385621.780335951}, {'n_components': 16, 'covariance': 'diag', 'training_time': 1.8165209293365479, 'bic': 3371870.595900289, 'aic': 3349012.009281324}, {'n_components': 17, 'covariance': 'diag', 'training_time': 3.7525949478149414, 'bic': 3341442.9227985167, 'aic': 3317155.1640972663}, {'n_components': 18, 'covariance': 'diag', 'training_time': 2.2993180751800537, 'bic': 3415962.035090576, 'aic': 3390245.104307039}, {'n_components': 19, 'covariance': 'diag', 'training_time': 2.620152235031128, 'bic': 3301225.390875423, 'aic': 3274079.2880096002}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.12374305725097656, 'bic': 6784436.317208571, 'aic': 6783717.647818622}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.2938532829284668, 'bic': 6759234.231010213, 'aic': 6757788.7255327}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.5239496231079102, 'bic': 5721515.828736799, 'aic': 5719343.4871717235}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.7905659675598145, 'bic': 5471031.47653944, 'aic': 5468132.298886803}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.8251681327819824, 'bic': 5370149.787622311, 'aic': 5366523.773882111}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 1.5691521167755127, 'bic': 5425904.819840125, 'aic': 5421551.970012362}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 1.0006279945373535, 'bic': 5234712.224643473, 'aic': 5229632.538728147}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.8913860321044922, 'bic': 5270397.379323673, 'aic': 5264590.8573207855}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.9793789386749268, 'bic': 5175641.394402308, 'aic': 5169108.036311857}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 1.1216182708740234, 'bic': 5120725.787980128, 'aic': 5113465.593802115}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 1.3276417255401611, 'bic': 5208661.947356895, 'aic': 5200674.917091318}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 2.725145101547241, 'bic': 5136811.693995147, 'aic': 5128097.827642009}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 1.0873479843139648, 'bic': 5180963.87698971, 'aic': 5171523.174549009}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 1.501767873764038, 'bic': 5178064.847868258, 'aic': 5167897.309339995}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 1.7424991130828857, 'bic': 5078898.983654761, 'aic': 5068004.609038934}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 6.400696277618408, 'bic': 5049148.682601962, 'aic': 5037527.471898573}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 1.2214479446411133, 'bic': 5040129.780690672, 'aic': 5027781.73389972}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 1.183185338973999, 'bic': 4903405.928224127, 'aic': 4890331.045345612}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 1.4604530334472656, 'bic': 5117530.10734697, 'aic': 5103728.388380893}]

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

	# scores = 

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
	# results = 

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

def kmeans_adult_ica():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.31593266831046496, 'training_time': 0.3208198547363281, 'distortion': 0.017405786781230018, 'inertia': 9.035986832941521}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.31593266831046496, 'training_time': 0.24564909934997559, 'distortion': 0.017405786781230018, 'inertia': 9.035986832941521}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.15018794408801445, 'training_time': 0.347487211227417, 'distortion': 0.016213373240923097, 'inertia': 8.125057041142348}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.15018794408801445, 'training_time': 0.3927791118621826, 'distortion': 0.016213373240923097, 'inertia': 8.125057041142348}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.15532435707824127, 'training_time': 0.34410524368286133, 'distortion': 0.015761661404913238, 'inertia': 7.504169634796823}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.15532435707824127, 'training_time': 0.4058413505554199, 'distortion': 0.015761661404913238, 'inertia': 7.504169634796823}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.17934421953825755, 'training_time': 0.4026498794555664, 'distortion': 0.014859541362147484, 'inertia': 6.9282481329668135}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.17934421953825755, 'training_time': 0.46625590324401855, 'distortion': 0.014859541362147484, 'inertia': 6.9282481329668135}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.19116664425806107, 'training_time': 0.4727349281311035, 'distortion': 0.01432949819715205, 'inertia': 6.163279930934397}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.19116664425806107, 'training_time': 0.5701990127563477, 'distortion': 0.01432949819715205, 'inertia': 6.163279930934397}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.21195307462262863, 'training_time': 0.6823630332946777, 'distortion': 0.013803632935277518, 'inertia': 5.733447017299721}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.21195307462262863, 'training_time': 0.845897912979126, 'distortion': 0.013803632935277518, 'inertia': 5.733447017299721}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.18374885945836916, 'training_time': 0.6562082767486572, 'distortion': 0.013250034661468648, 'inertia': 5.249162575288915}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.18374885945836916, 'training_time': 0.8329432010650635, 'distortion': 0.013250034661468648, 'inertia': 5.249162575288914}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.21052413101038844, 'training_time': 0.7545809745788574, 'distortion': 0.012693285868161831, 'inertia': 4.775593439151863}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.21052413101038844, 'training_time': 0.9612679481506348, 'distortion': 0.012693285868161831, 'inertia': 4.775593439151863}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.20961340822439858, 'training_time': 0.7854647636413574, 'distortion': 0.012224606291426614, 'inertia': 4.479418258190475}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.20961340822439858, 'training_time': 0.8960342407226562, 'distortion': 0.012224606291426614, 'inertia': 4.479418258190475}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.20884408323532358, 'training_time': 0.7562570571899414, 'distortion': 0.011686552319640792, 'inertia': 4.16917691239351}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.20884408323532358, 'training_time': 0.9502599239349365, 'distortion': 0.011686552319640792, 'inertia': 4.16917691239351}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.22070209632349702, 'training_time': 0.8314969539642334, 'distortion': 0.011336435252417358, 'inertia': 3.9642146692909956}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.22070209632349702, 'training_time': 1.0420799255371094, 'distortion': 0.011336435252417358, 'inertia': 3.964214669290996}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.22395214419569004, 'training_time': 0.7686781883239746, 'distortion': 0.011086598000170294, 'inertia': 3.8297536976995894}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.22395214419569004, 'training_time': 0.9892361164093018, 'distortion': 0.011086598000170294, 'inertia': 3.8297536976995894}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.22695732656742, 'training_time': 0.8517088890075684, 'distortion': 0.010904288019770007, 'inertia': 3.7279742622912053}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.22695732656742, 'training_time': 1.1091089248657227, 'distortion': 0.010904288019770007, 'inertia': 3.7279742622912053}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.22353014590102824, 'training_time': 0.9519829750061035, 'distortion': 0.010729466389117962, 'inertia': 3.6389608740251433}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.22353014590102824, 'training_time': 1.1607799530029297, 'distortion': 0.010729466389117962, 'inertia': 3.638960874025144}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.22822612891558725, 'training_time': 1.000399112701416, 'distortion': 0.010617969446784612, 'inertia': 3.5547483374517292}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.22822612891558725, 'training_time': 1.3468990325927734, 'distortion': 0.010617969446784612, 'inertia': 3.5547483374517297}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.22487048280880945, 'training_time': 1.1616010665893555, 'distortion': 0.010467084026414938, 'inertia': 3.4814238530642245}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.22487048280880945, 'training_time': 1.5171477794647217, 'distortion': 0.01046708402641494, 'inertia': 3.4814238530642245}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.22098897167704634, 'training_time': 1.094419002532959, 'distortion': 0.010348317752861965, 'inertia': 3.403802439138824}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.22098897167704634, 'training_time': 1.4901371002197266, 'distortion': 0.010348317752861965, 'inertia': 3.403802439138824}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.22247238262090882, 'training_time': 1.2047250270843506, 'distortion': 0.010267168734626981, 'inertia': 3.3477454809253384}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.22247238262090882, 'training_time': 1.6448850631713867, 'distortion': 0.010267168734626981, 'inertia': 3.3477454809253384}]
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
	
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.1341547966003418, 'bic': -1907359.0534609829, 'aic': -1907889.9187735596}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.3560020923614502, 'bic': -2012665.922137491, 'aic': -2013735.8199212993}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.7673132419586182, 'bic': -2090205.2175739366, 'aic': -2091814.1478289769}, {'n_components': 4, 'covariance': 'full', 'training_time': 1.2634871006011963, 'bic': -2137534.078532949, 'aic': -2139682.0412592213}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.862562894821167, 'bic': -2182286.0533152972, 'aic': -2184973.048512801}, {'n_components': 6, 'covariance': 'full', 'training_time': 1.102658987045288, 'bic': -2184867.989651254, 'aic': -2188094.0173199894}, {'n_components': 7, 'covariance': 'full', 'training_time': 1.3504128456115723, 'bic': -2207948.4477865966, 'aic': -2211713.5079265637}, {'n_components': 8, 'covariance': 'full', 'training_time': 3.1583518981933594, 'bic': -2203189.5160277816, 'aic': -2207493.6086389804}, {'n_components': 9, 'covariance': 'full', 'training_time': 2.2569501399993896, 'bic': -2239254.1318862033, 'aic': -2244097.2569686337}, {'n_components': 10, 'covariance': 'full', 'training_time': 2.37308406829834, 'bic': -2239498.996454, 'aic': -2244881.1540076626}, {'n_components': 11, 'covariance': 'full', 'training_time': 4.7211058139801025, 'bic': -2268970.70636635, 'aic': -2274891.896391244}, {'n_components': 12, 'covariance': 'full', 'training_time': 4.138175010681152, 'bic': -2267183.895842293, 'aic': -2273644.1183384187}, {'n_components': 13, 'covariance': 'full', 'training_time': 3.877997875213623, 'bic': -2276552.9999744105, 'aic': -2283552.254941768}, {'n_components': 14, 'covariance': 'full', 'training_time': 3.8746838569641113, 'bic': -2272318.759175079, 'aic': -2279857.046613668}, {'n_components': 15, 'covariance': 'full', 'training_time': 7.9809370040893555, 'bic': -2281111.3887345158, 'aic': -2289188.708644337}, {'n_components': 16, 'covariance': 'full', 'training_time': 5.368313789367676, 'bic': -2286054.058176574, 'aic': -2294670.4105576267}, {'n_components': 17, 'covariance': 'full', 'training_time': 4.902240037918091, 'bic': -2284307.7932766397, 'aic': -2293463.178128924}, {'n_components': 18, 'covariance': 'full', 'training_time': 7.985032796859741, 'bic': -2300688.8179800515, 'aic': -2310383.2353035677}, {'n_components': 19, 'covariance': 'full', 'training_time': 7.203398942947388, 'bic': -2296717.2250397895, 'aic': -2306950.6748345373}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.046814918518066406, 'bic': -1907359.0534609829, 'aic': -1907889.9187735596}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.13496708869934082, 'bic': -1913709.9708267183, 'aic': -1914330.6748845002}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.5031423568725586, 'bic': -1965714.606807874, 'aic': -1966425.1496108614}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.17500090599060059, 'bic': -1994587.843514689, 'aic': -1995388.2250628816}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.5660948753356934, 'bic': -2018708.9767829198, 'aic': -2019599.1970763176}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.4091620445251465, 'bic': -1995352.434477413, 'aic': -1996332.4935160163}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.815345048904419, 'bic': -2062232.1441016104, 'aic': -2063302.0418854188}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.8263938426971436, 'bic': -2051759.0827099683, 'aic': -2052918.8192389822}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.46741819381713867, 'bic': -2071239.1879130453, 'aic': -2072488.7631872643}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.6083300113677979, 'bic': -2072382.929800194, 'aic': -2073722.3438196182}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.8737399578094482, 'bic': -2079945.5490450286, 'aic': -2081374.8018096583}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.7790961265563965, 'bic': -2091716.7294001733, 'aic': -2093235.8209100082}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.8091940879821777, 'bic': -2090266.9266109727, 'aic': -2091875.856866013}, {'n_components': 14, 'covariance': 'tied', 'training_time': 1.1397969722747803, 'bic': -2093290.7776502473, 'aic': -2094989.5466504928}, {'n_components': 15, 'covariance': 'tied', 'training_time': 2.719762086868286, 'bic': -2095066.086750609, 'aic': -2096854.6944960598}, {'n_components': 16, 'covariance': 'tied', 'training_time': 1.9988369941711426, 'bic': -2116726.1041735616, 'aic': -2118604.5506642177}, {'n_components': 17, 'covariance': 'tied', 'training_time': 3.060802936553955, 'bic': -2107742.0325707975, 'aic': -2109710.317806659}, {'n_components': 18, 'covariance': 'tied', 'training_time': 3.3083670139312744, 'bic': -2108996.464692569, 'aic': -2111054.5886736354}, {'n_components': 19, 'covariance': 'tied', 'training_time': 1.7440009117126465, 'bic': -2112820.4713063757, 'aic': -2114968.434032648}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.036026954650878906, 'bic': -1907816.575600459, 'aic': -1907979.9187735596}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.08457827568054199, 'bic': -1949820.9195702646, 'aic': -1950155.7730751208}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.2759990692138672, 'bic': -2077888.1647496333, 'aic': -2078394.528586245}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.40138912200927734, 'bic': -2098228.2908982215, 'aic': -2098906.1650665887}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.33604884147644043, 'bic': -2135012.0829939265, 'aic': -2135861.467494049}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.4773752689361572, 'bic': -2152788.3770760293, 'aic': -2153809.2719079074}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.38150596618652344, 'bic': -2159957.759168192, 'aic': -2161150.1643318255}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.5041368007659912, 'bic': -2169655.4943248364, 'aic': -2171019.409820226}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.3865492343902588, 'bic': -2176179.563377523, 'aic': -2177714.989204668}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.7155680656433105, 'bic': -2189267.8265460543, 'aic': -2190974.762704955}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.952052116394043, 'bic': -2194471.876690258, 'aic': -2196350.323180914}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.5685920715332031, 'bic': -2189783.559405062, 'aic': -2191833.5162274735}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.9695088863372803, 'bic': -2201776.685248153, 'aic': -2203998.15240232}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.7319502830505371, 'bic': -2207869.315051648, 'aic': -2210262.2925375705}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.8094220161437988, 'bic': -2210870.4677728075, 'aic': -2213434.9555904856}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.9904937744140625, 'bic': -2214490.225931034, 'aic': -2217226.2240804676}, {'n_components': 17, 'covariance': 'diag', 'training_time': 1.2387120723724365, 'bic': -2213902.7675449164, 'aic': -2216810.276026106}, {'n_components': 18, 'covariance': 'diag', 'training_time': 1.168030023574829, 'bic': -2222147.4526627995, 'aic': -2225226.4714757446}, {'n_components': 19, 'covariance': 'diag', 'training_time': 1.2074737548828125, 'bic': -2222032.183181817, 'aic': -2225282.712326518}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.03647208213806152, 'bic': -1907908.0800283544, 'aic': -1907997.9187735596}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.3082082271575928, 'bic': -1940305.2495704682, 'aic': -1940493.0942195337}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.2810947895050049, 'bic': -1946795.6779243853, 'aic': -1947081.5284773111}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.363757848739624, 'bic': -1960243.2051448182, 'aic': -1960627.0616016043}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.34343504905700684, 'bic': -1963962.731143472, 'aic': -1964444.5935041185}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.37328100204467773, 'bic': -2009906.043581307, 'aic': -2010485.9118458137}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.38909101486206055, 'bic': -2009062.3977622401, 'aic': -2009740.2719306073}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.5266962051391602, 'bic': -2034003.3893765474, 'aic': -2034779.2694487749}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.43255019187927246, 'bic': -2018248.1575544209, 'aic': -2019122.0435305086}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 1.1200768947601318, 'bic': -2052546.1721279533, 'aic': -2053518.0640079014}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.4149508476257324, 'bic': -2067045.6410265449, 'aic': -2068115.5388103533}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.41121697425842285, 'bic': -2071113.3622736966, 'aic': -2072281.2659613653}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.7467689514160156, 'bic': -2083816.2425285047, 'aic': -2085082.1521200337}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.5127182006835938, 'bic': -2082118.0082225045, 'aic': -2083481.923717894}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.7908308506011963, 'bic': -2093837.2016866198, 'aic': -2095299.1230858695}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.5346522331237793, 'bic': -2087194.3429573374, 'aic': -2088754.2702604474}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.685147762298584, 'bic': -2095288.058655484, 'aic': -2096945.9918624545}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.6414089202880859, 'bic': -2102346.5598058985, 'aic': -2104102.4989167294}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.9765040874481201, 'bic': -2100748.0122024273, 'aic': -2102601.9572171182}]

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



if __name__ == '__main__':

	#### Adult Dataset
	# kmeans_adult()
	# em_adult()
	# kmeans_adult_pca()
	# em_adult_pca()
	# kmeans_adult_ica()
	# em_adult_ica()
	# kmeans_adult_rand()
	# em_adult_rand()




	#### Wine Dataset
	# kmeans_wine()
	# em_wine()
	# kmeans_wine_pca()
	# em_wine_pca()
	# kmeans_wine_ica()
	# em_wine_ica()
	# kmeans_wine_rand()
	# em_wine_rand()





