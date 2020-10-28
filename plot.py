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

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.2150637021039633, 'training_time': 0.20894527435302734, 'distortion': 2.536971953548731, 'inertia': 30417.165774877933}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.2150637021039633, 'training_time': 0.08889389038085938, 'distortion': 2.536971953548731, 'inertia': 30417.165774877933}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.15233585049113688, 'training_time': 0.2186579704284668, 'distortion': 2.4045135645647444, 'inertia': 27537.900809502124}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.15233585049113688, 'training_time': 0.16074013710021973, 'distortion': 2.4045135645647444, 'inertia': 27537.900809502124}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.16566927043597687, 'training_time': 0.2114419937133789, 'distortion': 2.3386340689358605, 'inertia': 25075.233218521305}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.16566927043597687, 'training_time': 0.195814847946167, 'distortion': 2.3386340689358605, 'inertia': 25075.233218521305}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.16166053956288345, 'training_time': 0.20859599113464355, 'distortion': 2.2672100793310728, 'inertia': 23442.77455452207}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.16166053956288345, 'training_time': 0.2948648929595947, 'distortion': 2.2672100793310728, 'inertia': 23442.77455452207}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.1392759654976935, 'training_time': 0.2771279811859131, 'distortion': 2.203049806616115, 'inertia': 22188.319627094737}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.1392759654976935, 'training_time': 0.3423900604248047, 'distortion': 2.203049806616115, 'inertia': 22188.319627094737}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.12900221305180323, 'training_time': 0.29518795013427734, 'distortion': 2.1454704790879244, 'inertia': 21059.40087714219}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.12900221305180323, 'training_time': 0.398909330368042, 'distortion': 2.1454704790879244, 'inertia': 21059.40087714219}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.13497898610745016, 'training_time': 0.3308990001678467, 'distortion': 2.098410915540423, 'inertia': 20089.098573708012}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.13497898610745016, 'training_time': 0.43498706817626953, 'distortion': 2.098410915540423, 'inertia': 20089.098573708012}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.13090636420202306, 'training_time': 0.41535019874572754, 'distortion': 2.0575939110363244, 'inertia': 19326.626325861784}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.13090636420202306, 'training_time': 0.4608027935028076, 'distortion': 2.0575939110363244, 'inertia': 19326.626325861784}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.1339994451414881, 'training_time': 0.3594510555267334, 'distortion': 2.0257291683641565, 'inertia': 18717.04242529093}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.1339994451414881, 'training_time': 0.4331221580505371, 'distortion': 2.0257291683641565, 'inertia': 18717.04242529093}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.123713709650232, 'training_time': 0.4541192054748535, 'distortion': 1.9954452118855883, 'inertia': 18174.681274068284}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.123713709650232, 'training_time': 0.5317988395690918, 'distortion': 1.9954452118855883, 'inertia': 18174.681274068284}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.1184095263820918, 'training_time': 0.3607959747314453, 'distortion': 1.969420560969946, 'inertia': 17780.60397701587}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.1184095263820918, 'training_time': 0.45979976654052734, 'distortion': 1.969420560969946, 'inertia': 17780.60397701587}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.12063189414087663, 'training_time': 0.4080390930175781, 'distortion': 1.944149065401527, 'inertia': 17345.5810424145}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.12063189414087663, 'training_time': 0.5797381401062012, 'distortion': 1.944149065401527, 'inertia': 17345.5810424145}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.12411971786062512, 'training_time': 0.388660192489624, 'distortion': 1.9242675903039552, 'inertia': 16972.93175855701}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.12411971786062512, 'training_time': 0.49643421173095703, 'distortion': 1.9242675903039552, 'inertia': 16972.93175855701}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.11974862893127397, 'training_time': 0.39152002334594727, 'distortion': 1.900842743652157, 'inertia': 16599.5370892463}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.11974862893127397, 'training_time': 0.5048501491546631, 'distortion': 1.900842743652157, 'inertia': 16599.5370892463}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.1182238891746427, 'training_time': 0.43999505043029785, 'distortion': 1.8802702468433108, 'inertia': 16300.631356295413}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.1182238891746427, 'training_time': 0.5622851848602295, 'distortion': 1.8802702468433108, 'inertia': 16300.631356295416}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.11744516148591136, 'training_time': 0.5223443508148193, 'distortion': 1.8771098345681099, 'inertia': 16033.71725368301}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.11744516148591136, 'training_time': 0.7593889236450195, 'distortion': 1.8771098345681099, 'inertia': 16033.717253683011}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.11889237231271652, 'training_time': 0.5497081279754639, 'distortion': 1.8572619931574792, 'inertia': 15735.25659459248}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.11889237231271652, 'training_time': 0.7884328365325928, 'distortion': 1.8572619931574792, 'inertia': 15735.25659459248}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.12177157689873506, 'training_time': 0.6317529678344727, 'distortion': 1.841165768750384, 'inertia': 15529.376016573822}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.12177157689873506, 'training_time': 0.8432509899139404, 'distortion': 1.841165768750384, 'inertia': 15529.376016573822}, {'n_clusters': 20, 'algorithm': 'full', 'silhouette_score': 0.12249616221658889, 'training_time': 0.6375541687011719, 'distortion': 1.8369181833205241, 'inertia': 15201.991175818006}, {'n_clusters': 20, 'algorithm': 'elkan', 'silhouette_score': 0.12249616221658889, 'training_time': 0.965726375579834, 'distortion': 1.8369181833205241, 'inertia': 15201.991175818006}, {'n_clusters': 21, 'algorithm': 'full', 'silhouette_score': 0.11747684056552482, 'training_time': 0.6670000553131104, 'distortion': 1.8130367248905184, 'inertia': 15024.721604198136}, {'n_clusters': 21, 'algorithm': 'elkan', 'silhouette_score': 0.11747684056552482, 'training_time': 1.033374309539795, 'distortion': 1.8130367248905184, 'inertia': 15024.721604198134}, {'n_clusters': 22, 'algorithm': 'full', 'silhouette_score': 0.114633639902673, 'training_time': 0.6984050273895264, 'distortion': 1.8019081971590556, 'inertia': 14819.21049297137}, {'n_clusters': 22, 'algorithm': 'elkan', 'silhouette_score': 0.114633639902673, 'training_time': 1.270310878753662, 'distortion': 1.8019081971590556, 'inertia': 14819.21049297137}, {'n_clusters': 23, 'algorithm': 'full', 'silhouette_score': 0.11448029411461494, 'training_time': 0.6989779472351074, 'distortion': 1.7925913313297328, 'inertia': 14578.78607897536}, {'n_clusters': 23, 'algorithm': 'elkan', 'silhouette_score': 0.11448029411461494, 'training_time': 1.2976329326629639, 'distortion': 1.7925913313297328, 'inertia': 14578.78607897536}, {'n_clusters': 24, 'algorithm': 'full', 'silhouette_score': 0.1164498222744498, 'training_time': 0.741569995880127, 'distortion': 1.7728276416115405, 'inertia': 14374.485845341791}, {'n_clusters': 24, 'algorithm': 'elkan', 'silhouette_score': 0.1164498222744498, 'training_time': 1.4136979579925537, 'distortion': 1.7728276416115405, 'inertia': 14374.485845341791}]

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
	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.09469914436340332, 'bic': 92494.28314711632, 'aic': 92217.78717772939}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.11732983589172363, 'bic': 86762.14667026815, 'aic': 86202.87073219003}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.15928888320922852, 'bic': 84869.01740267308, 'aic': 84026.96149590379}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.15767884254455566, 'bic': 84324.57048324744, 'aic': 83199.73460778696}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.23659300804138184, 'bic': 83928.41236662635, 'aic': 82520.79652247467}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.262923002243042, 'bic': 83864.99643399818, 'aic': 82174.60062115533}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.24696803092956543, 'bic': 83481.14293855165, 'aic': 81507.96715701761}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.2863891124725342, 'bic': 83429.46985804196, 'aic': 81173.51410781674}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.4311981201171875, 'bic': 83417.89382992397, 'aic': 80879.15811100756}, {'n_components': 10, 'covariance': 'full', 'training_time': 0.3060019016265869, 'bic': 83745.15513316121, 'aic': 80923.63944555362}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.36690306663513184, 'bic': 83747.81560506254, 'aic': 80643.51994876377}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.591576099395752, 'bic': 83718.46176336637, 'aic': 80331.38613837642}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.7471952438354492, 'bic': 83535.28154591577, 'aic': 79865.42595223463}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.5305719375610352, 'bic': 84032.43699609659, 'aic': 80079.80143372426}, {'n_components': 15, 'covariance': 'full', 'training_time': 0.5784618854522705, 'bic': 84128.00889807538, 'aic': 79892.59336701187}, {'n_components': 16, 'covariance': 'full', 'training_time': 1.0062320232391357, 'bic': 83973.555872898, 'aic': 79455.36037314331}, {'n_components': 17, 'covariance': 'full', 'training_time': 0.695080041885376, 'bic': 84171.72876053097, 'aic': 79370.7532920851}, {'n_components': 18, 'covariance': 'full', 'training_time': 0.7173929214477539, 'bic': 84461.73397782158, 'aic': 79377.97854068452}, {'n_components': 19, 'covariance': 'full', 'training_time': 0.8009369373321533, 'bic': 84499.84582175562, 'aic': 79133.31041592738}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.014565229415893555, 'bic': 92494.28314711632, 'aic': 92217.78717772939}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.038336992263793945, 'bic': 91693.82153610907, 'aic': 91360.7695729839}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.06336498260498047, 'bic': 88272.49010016333, 'aic': 87882.88214329991}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.15000700950622559, 'bic': 88207.0008103734, 'aic': 87760.83685977175}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.10244321823120117, 'bic': 87631.39960344428, 'aic': 87128.6796591044}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.13010883331298828, 'bic': 87248.22124160017, 'aic': 86688.94530352205}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.21553587913513184, 'bic': 86821.29596216188, 'aic': 86205.46403034552}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.23352909088134766, 'bic': 86618.5662553148, 'aic': 85946.17832976021}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.20770001411437988, 'bic': 86401.04386501497, 'aic': 85672.09994572215}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.15385198593139648, 'bic': 86343.56950738144, 'aic': 85558.06959435038}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.21319007873535156, 'bic': 86310.76449549448, 'aic': 85468.70858872519}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.19731616973876953, 'bic': 86556.98757988279, 'aic': 85658.37567937524}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.15798497200012207, 'bic': 86467.7928145904, 'aic': 85512.62492034462}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.18618488311767578, 'bic': 86415.65305443836, 'aic': 85403.92916645434}, {'n_components': 15, 'covariance': 'tied', 'training_time': 0.23292803764343262, 'bic': 86418.13639181874, 'aic': 85349.85651009649}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.251633882522583, 'bic': 85556.43300727071, 'aic': 84431.59713181022}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.3085513114929199, 'bic': 85650.6553090979, 'aic': 84469.26343989918}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.2902538776397705, 'bic': 85832.22490210127, 'aic': 84594.27703916431}, {'n_components': 19, 'covariance': 'tied', 'training_time': 0.27250099182128906, 'bic': 85677.85283477558, 'aic': 84383.34897810039}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.03341865539550781, 'bic': 92262.33116659737, 'aic': 92161.78717772939}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.059275150299072266, 'bic': 88947.5846437444, 'aic': 88740.2126667042}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.07323217391967773, 'bic': 87993.74100879738, 'aic': 87679.54104358496}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.07643795013427734, 'bic': 87300.70193168125, 'aic': 86879.6739782966}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.08115100860595703, 'bic': 87117.18041708691, 'aic': 86589.32447553004}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.13220787048339844, 'bic': 86566.90705822018, 'aic': 85932.22312849108}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.1776120662689209, 'bic': 86411.07795427601, 'aic': 85669.56603637469}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.09589004516601562, 'bic': 86226.17674196813, 'aic': 85377.83683589457}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.11591410636901855, 'bic': 86019.55879228021, 'aic': 85064.39089803443}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.14848685264587402, 'bic': 85858.62965943693, 'aic': 84796.63377701893}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.10702395439147949, 'bic': 86074.51509176957, 'aic': 84905.69122117935}, {'n_components': 12, 'covariance': 'diag', 'training_time': 0.11616992950439453, 'bic': 85833.57773177729, 'aic': 84557.92587301484}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.15315008163452148, 'bic': 85528.90700843334, 'aic': 84146.42716149866}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.2364978790283203, 'bic': 85437.27181200888, 'aic': 83947.96397690199}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.18488717079162598, 'bic': 85560.95041274502, 'aic': 83964.8145894659}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.2369999885559082, 'bic': 85373.68332546159, 'aic': 83670.71951401024}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.1982729434967041, 'bic': 85597.39775696203, 'aic': 83787.60595733846}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.2130727767944336, 'bic': 85400.47373506929, 'aic': 83483.85394727348}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.21783709526062012, 'bic': 85571.8535136342, 'aic': 83548.40573766617}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.023814916610717773, 'bic': 95761.9270658733, 'aic': 95705.37107213507}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.03525209426879883, 'bic': 92405.93955061704, 'aic': 92286.54356383631}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.0720210075378418, 'bic': 91626.86839994072, 'aic': 91444.63242011752}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.046878814697265625, 'bic': 89100.28703028071, 'aic': 88855.21105741501}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.0771939754486084, 'bic': 88679.87610318525, 'aic': 88371.96013727707}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.0748448371887207, 'bic': 88501.82559578815, 'aic': 88131.06963683749}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.08033609390258789, 'bic': 87966.58208325465, 'aic': 87532.9861312615}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.07017183303833008, 'bic': 87686.5294344908, 'aic': 87190.09348945518}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.09947896003723145, 'bic': 87301.58134632283, 'aic': 86742.3054082447}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 0.0856468677520752, 'bic': 87183.77696318674, 'aic': 86561.66103206614}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.1170198917388916, 'bic': 87066.540916732, 'aic': 86381.58499256891}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.10957622528076172, 'bic': 86835.46736613188, 'aic': 86087.67144892631}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.10770010948181152, 'bic': 86849.47356220044, 'aic': 86038.83765195237}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.10228300094604492, 'bic': 86824.97189658115, 'aic': 85951.4959932906}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.20948410034179688, 'bic': 86469.3304894042, 'aic': 85533.01459307116}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.1722862720489502, 'bic': 86320.36180548444, 'aic': 85321.20591610893}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.1403331756591797, 'bic': 86358.0157506367, 'aic': 85296.01986821869}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.19645094871520996, 'bic': 86026.19824004186, 'aic': 84901.36236458138}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.16737580299377441, 'bic': 86171.94134926038, 'aic': 84984.2654807574}]

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

	results = [{'n_components': 1, 'covariance': 'full', 'training_time': 0.08223080635070801, 'bic': -214354.5191969054, 'aic': -214762.78188294137}, {'n_components': 2, 'covariance': 'full', 'training_time': 0.14357829093933105, 'bic': -220559.2169164728, 'aic': -221382.02325294528}, {'n_components': 3, 'covariance': 'full', 'training_time': 0.13801288604736328, 'bic': -223053.12152080098, 'aic': -224290.47150771}, {'n_components': 4, 'covariance': 'full', 'training_time': 0.22015905380249023, 'bic': -225040.59290561985, 'aic': -226692.4865429654}, {'n_components': 5, 'covariance': 'full', 'training_time': 0.37624621391296387, 'bic': -225484.33232570466, 'aic': -227550.76961348671}, {'n_components': 6, 'covariance': 'full', 'training_time': 0.4203450679779053, 'bic': -226088.65227428655, 'aic': -228569.63321250514}, {'n_components': 7, 'covariance': 'full', 'training_time': 0.38785409927368164, 'bic': -226016.44447696893, 'aic': -228911.96906562403}, {'n_components': 8, 'covariance': 'full', 'training_time': 0.6181690692901611, 'bic': -226599.51978120554, 'aic': -229909.58802029717}, {'n_components': 9, 'covariance': 'full', 'training_time': 0.7945940494537354, 'bic': -226440.67212013327, 'aic': -230165.2840096614}, {'n_components': 10, 'covariance': 'full', 'training_time': 1.0400428771972656, 'bic': -226550.04190993478, 'aic': -230689.19744989945}, {'n_components': 11, 'covariance': 'full', 'training_time': 0.5357601642608643, 'bic': -226098.3676602206, 'aic': -230652.06685062178}, {'n_components': 12, 'covariance': 'full', 'training_time': 0.5986452102661133, 'bic': -226409.78679964322, 'aic': -231378.02964048093}, {'n_components': 13, 'covariance': 'full', 'training_time': 0.8855888843536377, 'bic': -226249.49540425895, 'aic': -231632.2818955332}, {'n_components': 14, 'covariance': 'full', 'training_time': 0.7461159229278564, 'bic': -225640.32315402784, 'aic': -231437.6532957386}, {'n_components': 15, 'covariance': 'full', 'training_time': 0.9565680027008057, 'bic': -225734.04262450637, 'aic': -231945.91641665366}, {'n_components': 16, 'covariance': 'full', 'training_time': 0.6628930568695068, 'bic': -224951.19675638204, 'aic': -231577.61419896584}, {'n_components': 17, 'covariance': 'full', 'training_time': 1.2401762008666992, 'bic': -224719.56845011478, 'aic': -231760.5295431351}, {'n_components': 18, 'covariance': 'full', 'training_time': 1.8094372749328613, 'bic': -225223.47403872994, 'aic': -232678.97878218678}, {'n_components': 19, 'covariance': 'full', 'training_time': 1.5013360977172852, 'bic': -224984.62690006846, 'aic': -232854.67529396183}, {'n_components': 1, 'covariance': 'tied', 'training_time': 0.0197451114654541, 'bic': -214354.51919690543, 'aic': -214762.7818829414}, {'n_components': 2, 'covariance': 'tied', 'training_time': 0.050988197326660156, 'bic': -214923.80301704278, 'aic': -215401.15631148484}, {'n_components': 3, 'covariance': 'tied', 'training_time': 0.04684591293334961, 'bic': -215307.53113831792, 'aic': -215853.97504116606}, {'n_components': 4, 'covariance': 'tied', 'training_time': 0.0633699893951416, 'bic': -219153.6310593618, 'aic': -219769.16557061602}, {'n_components': 5, 'covariance': 'tied', 'training_time': 0.13454294204711914, 'bic': -219509.4053047096, 'aic': -220194.0304243699}, {'n_components': 6, 'covariance': 'tied', 'training_time': 0.24039602279663086, 'bic': -220423.24648910333, 'aic': -221176.96221716973}, {'n_components': 7, 'covariance': 'tied', 'training_time': 0.16599106788635254, 'bic': -220399.4338195224, 'aic': -221222.2401559949}, {'n_components': 8, 'covariance': 'tied', 'training_time': 0.33941125869750977, 'bic': -220901.03027156967, 'aic': -221792.92721644824}, {'n_components': 9, 'covariance': 'tied', 'training_time': 0.1447439193725586, 'bic': -220809.8427722192, 'aic': -221770.8303255039}, {'n_components': 10, 'covariance': 'tied', 'training_time': 0.23585891723632812, 'bic': -221107.88764197702, 'aic': -222137.9658036678}, {'n_components': 11, 'covariance': 'tied', 'training_time': 0.21603178977966309, 'bic': -221689.9794814653, 'aic': -222789.14825156215}, {'n_components': 12, 'covariance': 'tied', 'training_time': 0.32500720024108887, 'bic': -221449.81105867785, 'aic': -222618.07043718078}, {'n_components': 13, 'covariance': 'tied', 'training_time': 0.5960156917572021, 'bic': -221642.64861861395, 'aic': -222879.99860552297}, {'n_components': 14, 'covariance': 'tied', 'training_time': 0.3682527542114258, 'bic': -221483.73698451102, 'aic': -222790.17757982612}, {'n_components': 15, 'covariance': 'tied', 'training_time': 0.41823482513427734, 'bic': -221591.93560541398, 'aic': -222967.46680913516}, {'n_components': 16, 'covariance': 'tied', 'training_time': 0.4120609760284424, 'bic': -222059.27418638254, 'aic': -223503.8959985098}, {'n_components': 17, 'covariance': 'tied', 'training_time': 0.490009069442749, 'bic': -222328.69871356722, 'aic': -223842.41113410058}, {'n_components': 18, 'covariance': 'tied', 'training_time': 0.6412880420684814, 'bic': -223119.20899591735, 'aic': -224702.01202485678}, {'n_components': 19, 'covariance': 'tied', 'training_time': 0.4284780025482178, 'bic': -222113.53523944796, 'aic': -223765.4288767935}, {'n_components': 1, 'covariance': 'diag', 'training_time': 0.01765298843383789, 'bic': -214727.1625949303, 'aic': -214852.78188294137}, {'n_components': 2, 'covariance': 'diag', 'training_time': 0.03344321250915527, 'bic': -221300.65242401016, 'aic': -221558.17196443284}, {'n_components': 3, 'covariance': 'diag', 'training_time': 0.05535602569580078, 'bic': -222362.4585926252, 'aic': -222751.8783854595}, {'n_components': 4, 'covariance': 'diag', 'training_time': 0.16776013374328613, 'bic': -222955.8489801284, 'aic': -223477.1690253743}, {'n_components': 5, 'covariance': 'diag', 'training_time': 0.11683177947998047, 'bic': -223436.68490695115, 'aic': -224089.90520460872}, {'n_components': 6, 'covariance': 'diag', 'training_time': 0.16058087348937988, 'bic': -223932.94456624045, 'aic': -224718.06511630962}, {'n_components': 7, 'covariance': 'diag', 'training_time': 0.19151806831359863, 'bic': -224090.05873486577, 'aic': -225007.07953734655}, {'n_components': 8, 'covariance': 'diag', 'training_time': 0.10960197448730469, 'bic': -224349.72780047386, 'aic': -225398.64885536628}, {'n_components': 9, 'covariance': 'diag', 'training_time': 0.15369081497192383, 'bic': -224605.27580855566, 'aic': -225786.09711585968}, {'n_components': 10, 'covariance': 'diag', 'training_time': 0.44869017601013184, 'bic': -224608.0854302013, 'aic': -225920.80698991695}, {'n_components': 11, 'covariance': 'diag', 'training_time': 0.5401310920715332, 'bic': -224889.917398945, 'aic': -226334.53921107226}, {'n_components': 12, 'covariance': 'diag', 'training_time': 1.383984088897705, 'bic': -224993.298752324, 'aic': -226569.8208168629}, {'n_components': 13, 'covariance': 'diag', 'training_time': 0.30257320404052734, 'bic': -225001.6818426065, 'aic': -226710.104159557}, {'n_components': 14, 'covariance': 'diag', 'training_time': 0.46319580078125, 'bic': -225007.67018288633, 'aic': -226847.99275224848}, {'n_components': 15, 'covariance': 'diag', 'training_time': 0.4393279552459717, 'bic': -224932.33011762626, 'aic': -226904.55293940002}, {'n_components': 16, 'covariance': 'diag', 'training_time': 0.3201711177825928, 'bic': -225183.6807352858, 'aic': -227287.8038094712}, {'n_components': 17, 'covariance': 'diag', 'training_time': 0.23603510856628418, 'bic': -225434.8808932658, 'aic': -227670.9042198628}, {'n_components': 18, 'covariance': 'diag', 'training_time': 0.47362613677978516, 'bic': -225296.09230820817, 'aic': -227664.01588721678}, {'n_components': 19, 'covariance': 'diag', 'training_time': 0.2901430130004883, 'bic': -225346.78705187546, 'aic': -227846.6108832957}, {'n_components': 1, 'covariance': 'spherical', 'training_time': 0.013477802276611328, 'bic': -214801.69127453535, 'aic': -214870.78188294143}, {'n_components': 2, 'covariance': 'spherical', 'training_time': 0.04814291000366211, 'bic': -217907.44150685018, 'aic': -218051.9036880629}, {'n_components': 3, 'covariance': 'spherical', 'training_time': 0.15097689628601074, 'bic': -218307.38009426012, 'aic': -218527.2138482795}, {'n_components': 4, 'covariance': 'spherical', 'training_time': 0.17149782180786133, 'bic': -218896.42014047998, 'aic': -219191.625467306}, {'n_components': 5, 'covariance': 'spherical', 'training_time': 0.09247112274169922, 'bic': -218961.60673247272, 'aic': -219332.18363210536}, {'n_components': 6, 'covariance': 'spherical', 'training_time': 0.0874948501586914, 'bic': -219626.57479364678, 'aic': -220072.52326608606}, {'n_components': 7, 'covariance': 'spherical', 'training_time': 0.15088176727294922, 'bic': -220083.01489739932, 'aic': -220604.33494264525}, {'n_components': 8, 'covariance': 'spherical', 'training_time': 0.1728661060333252, 'bic': -220439.25052834777, 'aic': -221035.94214640034}, {'n_components': 9, 'covariance': 'spherical', 'training_time': 0.1331958770751953, 'bic': -220817.26699420396, 'aic': -221489.33018506318}, {'n_components': 10, 'covariance': 'spherical', 'training_time': 0.08987188339233398, 'bic': -221382.4729491891, 'aic': -222129.90771285497}, {'n_components': 11, 'covariance': 'spherical', 'training_time': 0.09302830696105957, 'bic': -221518.55949829376, 'aic': -222341.36583476624}, {'n_components': 12, 'covariance': 'spherical', 'training_time': 0.0995020866394043, 'bic': -221731.9306800536, 'aic': -222630.10858933273}, {'n_components': 13, 'covariance': 'spherical', 'training_time': 0.11352682113647461, 'bic': -222119.09448782704, 'aic': -223092.6439699128}, {'n_components': 14, 'covariance': 'spherical', 'training_time': 0.11353015899658203, 'bic': -222158.81367803694, 'aic': -223207.73473292936}, {'n_components': 15, 'covariance': 'spherical', 'training_time': 0.1017920970916748, 'bic': -222413.50549758246, 'aic': -223537.79812528152}, {'n_components': 16, 'covariance': 'spherical', 'training_time': 0.13906407356262207, 'bic': -222235.6931278144, 'aic': -223435.3573283201}, {'n_components': 17, 'covariance': 'spherical', 'training_time': 0.22281193733215332, 'bic': -222704.83277283498, 'aic': -223979.8685461473}, {'n_components': 18, 'covariance': 'spherical', 'training_time': 0.191817045211792, 'bic': -222853.88728298523, 'aic': -224204.2946291042}, {'n_components': 19, 'covariance': 'spherical', 'training_time': 0.2955951690673828, 'bic': -222922.6197179866, 'aic': -224348.39863691223}]

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

def kmeans_wine_ica():
	''' '''

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.09057311310854359, 'training_time': 0.29575514793395996, 'distortion': 0.045467307586602446, 'inertia': 9.242857564584904}, {'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.09057311310854359, 'training_time': 0.26241087913513184, 'distortion': 0.045467307586602446, 'inertia': 9.242857564584904}, {'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.09130044047082903, 'training_time': 0.28083205223083496, 'distortion': 0.043783392634359104, 'inertia': 8.63795599250589}, {'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.09130044047082903, 'training_time': 0.3233518600463867, 'distortion': 0.043783392634359104, 'inertia': 8.63795599250589}, {'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.1015099223406001, 'training_time': 0.24179720878601074, 'distortion': 0.042711323261746766, 'inertia': 7.965331352777578}, {'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.1015099223406001, 'training_time': 0.4976491928100586, 'distortion': 0.042711323261746766, 'inertia': 7.965331352777578}, {'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.1072891627874353, 'training_time': 0.27227306365966797, 'distortion': 0.041443112346914356, 'inertia': 7.515374969379658}, {'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.1072891627874353, 'training_time': 0.3963298797607422, 'distortion': 0.041443112346914356, 'inertia': 7.515374969379658}, {'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.11142745751167217, 'training_time': 0.3681330680847168, 'distortion': 0.04037769896297354, 'inertia': 7.123700799809569}, {'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.11142745751167217, 'training_time': 0.46759605407714844, 'distortion': 0.04037769896297354, 'inertia': 7.12370079980957}, {'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.11270108763418168, 'training_time': 0.35155415534973145, 'distortion': 0.03940988272019087, 'inertia': 6.759229728862173}, {'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.11270108763418168, 'training_time': 0.4012489318847656, 'distortion': 0.03940988272019087, 'inertia': 6.759229728862173}, {'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.11405367608125687, 'training_time': 0.31046223640441895, 'distortion': 0.038538443665491695, 'inertia': 6.452510479416043}, {'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.11405367608125687, 'training_time': 0.5007529258728027, 'distortion': 0.038538443665491695, 'inertia': 6.452510479416044}, {'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.11662019797162648, 'training_time': 0.37425899505615234, 'distortion': 0.03770634378854598, 'inertia': 6.170838350934316}, {'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.11662019797162648, 'training_time': 0.6893277168273926, 'distortion': 0.03770634378854598, 'inertia': 6.170838350934316}, {'n_clusters': 10, 'algorithm': 'full', 'silhouette_score': 0.11425577525167686, 'training_time': 0.3740999698638916, 'distortion': 0.03708219225978869, 'inertia': 5.959854092185724}, {'n_clusters': 10, 'algorithm': 'elkan', 'silhouette_score': 0.11425577525167686, 'training_time': 0.4201638698577881, 'distortion': 0.03708219225978869, 'inertia': 5.959854092185724}, {'n_clusters': 11, 'algorithm': 'full', 'silhouette_score': 0.11535176291150462, 'training_time': 0.3693821430206299, 'distortion': 0.036554092028589905, 'inertia': 5.757312302609758}, {'n_clusters': 11, 'algorithm': 'elkan', 'silhouette_score': 0.11535176291150462, 'training_time': 0.5749261379241943, 'distortion': 0.03655409202858992, 'inertia': 5.757312302609759}, {'n_clusters': 12, 'algorithm': 'full', 'silhouette_score': 0.10769437620623484, 'training_time': 0.44562196731567383, 'distortion': 0.036121207637955725, 'inertia': 5.635874233060249}, {'n_clusters': 12, 'algorithm': 'elkan', 'silhouette_score': 0.10769437620623484, 'training_time': 0.49500489234924316, 'distortion': 0.036121207637955725, 'inertia': 5.635874233060249}, {'n_clusters': 13, 'algorithm': 'full', 'silhouette_score': 0.1075000483983887, 'training_time': 0.48114991188049316, 'distortion': 0.0357049192572271, 'inertia': 5.528651785591641}, {'n_clusters': 13, 'algorithm': 'elkan', 'silhouette_score': 0.1075000483983887, 'training_time': 0.5225048065185547, 'distortion': 0.0357049192572271, 'inertia': 5.5286517855916415}, {'n_clusters': 14, 'algorithm': 'full', 'silhouette_score': 0.10637576451011296, 'training_time': 0.42496585845947266, 'distortion': 0.03533774076716913, 'inertia': 5.424758211189582}, {'n_clusters': 14, 'algorithm': 'elkan', 'silhouette_score': 0.10637576451011296, 'training_time': 0.5877640247344971, 'distortion': 0.03533774076716913, 'inertia': 5.424758211189582}, {'n_clusters': 15, 'algorithm': 'full', 'silhouette_score': 0.10672241827157024, 'training_time': 0.47919607162475586, 'distortion': 0.034992247033670015, 'inertia': 5.321406898099715}, {'n_clusters': 15, 'algorithm': 'elkan', 'silhouette_score': 0.10672241827157024, 'training_time': 0.7027280330657959, 'distortion': 0.034992247033670015, 'inertia': 5.321406898099715}, {'n_clusters': 16, 'algorithm': 'full', 'silhouette_score': 0.10377523177243818, 'training_time': 0.470045804977417, 'distortion': 0.03464901217846406, 'inertia': 5.22846029869299}, {'n_clusters': 16, 'algorithm': 'elkan', 'silhouette_score': 0.10377523177243818, 'training_time': 0.6191329956054688, 'distortion': 0.03464901217846406, 'inertia': 5.22846029869299}, {'n_clusters': 17, 'algorithm': 'full', 'silhouette_score': 0.10772140600163736, 'training_time': 0.49074530601501465, 'distortion': 0.034406812312058735, 'inertia': 5.146692548246002}, {'n_clusters': 17, 'algorithm': 'elkan', 'silhouette_score': 0.10772140600163736, 'training_time': 0.6877350807189941, 'distortion': 0.034406812312058735, 'inertia': 5.146692548246002}, {'n_clusters': 18, 'algorithm': 'full', 'silhouette_score': 0.11064506166860277, 'training_time': 0.47413015365600586, 'distortion': 0.03411843915686349, 'inertia': 5.070419908049813}, {'n_clusters': 18, 'algorithm': 'elkan', 'silhouette_score': 0.11064506166860277, 'training_time': 0.6407709121704102, 'distortion': 0.03411843915686349, 'inertia': 5.070419908049813}, {'n_clusters': 19, 'algorithm': 'full', 'silhouette_score': 0.10924074453447752, 'training_time': 0.472074031829834, 'distortion': 0.033863516901215814, 'inertia': 4.995928228502471}, {'n_clusters': 19, 'algorithm': 'elkan', 'silhouette_score': 0.10924074453447752, 'training_time': 0.575927734375, 'distortion': 0.033863516901215814, 'inertia': 4.995928228502472}]

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

	results = [{'n_components': 1, 'reconstruction_error': 100473429.53834943}, {'n_components': 2, 'reconstruction_error': 17623449.405405868}, {'n_components': 3, 'reconstruction_error': 21591523.78576281}, {'n_components': 4, 'reconstruction_error': 26596144.34903057}, {'n_components': 5, 'reconstruction_error': 16356962.77910273}, {'n_components': 6, 'reconstruction_error': 23176237.509543948}, {'n_components': 7, 'reconstruction_error': 11375251.252586138}, {'n_components': 8, 'reconstruction_error': 10947078.023808429}, {'n_components': 9, 'reconstruction_error': 22290597.04923112}, {'n_components': 10, 'reconstruction_error': 44705925.28239508}, {'n_components': 11, 'reconstruction_error': 71584241.26271145}, {'n_components': 12, 'reconstruction_error': 42543452.47638469}, {'n_components': 13, 'reconstruction_error': 29162941.571314916}, {'n_components': 14, 'reconstruction_error': 46262331.64163633}, {'n_components': 15, 'reconstruction_error': 21705213.764183264}, {'n_components': 16, 'reconstruction_error': 32459474.36997147}, {'n_components': 17, 'reconstruction_error': 22097745.48591609}, {'n_components': 18, 'reconstruction_error': 27995014.300517615}, {'n_components': 19, 'reconstruction_error': 15861676.425773608}, {'n_components': 20, 'reconstruction_error': 40247706.09586157}, {'n_components': 21, 'reconstruction_error': 51425632.7363778}, {'n_components': 22, 'reconstruction_error': 56317482.72965463}, {'n_components': 23, 'reconstruction_error': 8851753.672714634}, {'n_components': 24, 'reconstruction_error': 16598177.469997112}, {'n_components': 25, 'reconstruction_error': 29697390.531267617}, {'n_components': 26, 'reconstruction_error': 34282540.07828557}, {'n_components': 27, 'reconstruction_error': 27454327.937977847}, {'n_components': 28, 'reconstruction_error': 21444788.991912942}, {'n_components': 29, 'reconstruction_error': 28423548.083028514}, {'n_components': 30, 'reconstruction_error': 22550671.845011093}, {'n_components': 31, 'reconstruction_error': 16672711.352677759}, {'n_components': 32, 'reconstruction_error': 46663217.3711332}, {'n_components': 33, 'reconstruction_error': 39059319.57881969}, {'n_components': 34, 'reconstruction_error': 13159486.264916483}, {'n_components': 35, 'reconstruction_error': 34525913.63307098}, {'n_components': 36, 'reconstruction_error': 36633201.035651095}, {'n_components': 37, 'reconstruction_error': 25366792.71254824}, {'n_components': 38, 'reconstruction_error': 14260839.263438595}, {'n_components': 39, 'reconstruction_error': 13154653.633163922}, {'n_components': 40, 'reconstruction_error': 12636367.896508457}, {'n_components': 41, 'reconstruction_error': 34351369.07365988}, {'n_components': 42, 'reconstruction_error': 21596571.79827928}, {'n_components': 43, 'reconstruction_error': 46985940.72787806}, {'n_components': 44, 'reconstruction_error': 59288646.66941428}, {'n_components': 45, 'reconstruction_error': 18053260.442172255}, {'n_components': 46, 'reconstruction_error': 16694559.12756854}, {'n_components': 47, 'reconstruction_error': 28700529.854595732}, {'n_components': 48, 'reconstruction_error': 42281231.26012908}, {'n_components': 49, 'reconstruction_error': 44212270.388917245}, {'n_components': 50, 'reconstruction_error': 12811417.396683881}, {'n_components': 51, 'reconstruction_error': 42773889.879836045}, {'n_components': 52, 'reconstruction_error': 25046116.111364182}, {'n_components': 53, 'reconstruction_error': 21673770.572826773}, {'n_components': 54, 'reconstruction_error': 52080385.37850941}, {'n_components': 55, 'reconstruction_error': 46732360.5501821}, {'n_components': 56, 'reconstruction_error': 22341353.747407082}, {'n_components': 57, 'reconstruction_error': 26045627.320403885}, {'n_components': 58, 'reconstruction_error': 26555647.235836346}, {'n_components': 59, 'reconstruction_error': 19449761.0197313}, {'n_components': 60, 'reconstruction_error': 6549954.397139458}, {'n_components': 61, 'reconstruction_error': 16366895.237205004}, {'n_components': 62, 'reconstruction_error': 48958383.096775405}, {'n_components': 63, 'reconstruction_error': 50198323.19501473}, {'n_components': 64, 'reconstruction_error': 33138223.44447365}, {'n_components': 65, 'reconstruction_error': 23446015.88006789}, {'n_components': 66, 'reconstruction_error': 19182682.417969067}, {'n_components': 67, 'reconstruction_error': 28760423.225900434}, {'n_components': 68, 'reconstruction_error': 34551905.9829732}, {'n_components': 69, 'reconstruction_error': 26665709.14156936}, {'n_components': 70, 'reconstruction_error': 8001938.452425927}, {'n_components': 71, 'reconstruction_error': 35459904.94332186}, {'n_components': 72, 'reconstruction_error': 72693019.65857518}, {'n_components': 73, 'reconstruction_error': 67128613.2708954}, {'n_components': 74, 'reconstruction_error': 31644738.497691035}, {'n_components': 75, 'reconstruction_error': 33109059.907722432}, {'n_components': 76, 'reconstruction_error': 14019695.155458272}, {'n_components': 77, 'reconstruction_error': 7602735.530113142}, {'n_components': 78, 'reconstruction_error': 30300997.362656858}, {'n_components': 79, 'reconstruction_error': 19713445.11440673}, {'n_components': 80, 'reconstruction_error': 21126703.034003716}, {'n_components': 81, 'reconstruction_error': 28005526.674738746}, {'n_components': 82, 'reconstruction_error': 39486064.005931094}, {'n_components': 83, 'reconstruction_error': 20703783.253523596}, {'n_components': 84, 'reconstruction_error': 34807182.15940111}, {'n_components': 85, 'reconstruction_error': 17422213.27359551}, {'n_components': 86, 'reconstruction_error': 51273285.9663983}, {'n_components': 87, 'reconstruction_error': 22883554.01251864}, {'n_components': 88, 'reconstruction_error': 36979241.8382533}, {'n_components': 89, 'reconstruction_error': 20127739.323683742}, {'n_components': 90, 'reconstruction_error': 27641508.20856473}, {'n_components': 91, 'reconstruction_error': 3948843.730505711}, {'n_components': 92, 'reconstruction_error': 18699669.838682357}, {'n_components': 93, 'reconstruction_error': 30316817.04877514}, {'n_components': 94, 'reconstruction_error': 29152889.48678713}, {'n_components': 95, 'reconstruction_error': 31189331.377470613}, {'n_components': 96, 'reconstruction_error': 8653620.648475295}, {'n_components': 97, 'reconstruction_error': 37826260.66039956}, {'n_components': 98, 'reconstruction_error': 51118180.84926803}, {'n_components': 99, 'reconstruction_error': 27655987.895807188}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.xlabel("No. of Components")
	plt.ylabel("Reconstruction Error")
	plt.title("Randomized Projection \n Adult")
	plt.tight_layout()
	plt.savefig("figures/adult_rp")
	plt.cla()

def wine_reconstruction_error():

	results = [{'n_components': 1, 'reconstruction_error': 3.498320367612651e-25}, {'n_components': 2, 'reconstruction_error': 5.285873095594323e-26}, {'n_components': 3, 'reconstruction_error': 2.325242871233319e-26}, {'n_components': 4, 'reconstruction_error': 7.251885232378767e-27}, {'n_components': 5, 'reconstruction_error': 1.8224986965661424e-26}, {'n_components': 6, 'reconstruction_error': 5.37605548539828e-26}, {'n_components': 7, 'reconstruction_error': 1.8346815509978844e-26}, {'n_components': 8, 'reconstruction_error': 3.1374401911060968e-27}, {'n_components': 9, 'reconstruction_error': 3.7040840156381375e-27}]
	# results = [{'n_components': 1, 'reconstruction_error': 2.2216110737269734e-26}, {'n_components': 2, 'reconstruction_error': 1.3458390708156127e-23}, {'n_components': 3, 'reconstruction_error': 2.2724764619583465e-24}, {'n_components': 4, 'reconstruction_error': 7.993529909504242e-26}, {'n_components': 5, 'reconstruction_error': 3.615473332834437e-25}, {'n_components': 6, 'reconstruction_error': 5.502599021463136e-25}, {'n_components': 7, 'reconstruction_error': 1.5887668746795741e-24}, {'n_components': 8, 'reconstruction_error': 1.9382919228920747e-26}, {'n_components': 9, 'reconstruction_error': 2.78446125017654e-25}]

	x = [x['n_components'] for x in results]
	y = [y['reconstruction_error'] for y in results]

	plt.plot(x, y)
	plt.xlabel("No. of Components")
	plt.ylabel("Reconstruction Error")
	plt.title("Randomized Projection \n Wine")
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
	# adult_reconstruction_error()




	#### Wine Dataset
	# kmeans_wine()
	# em_wine()
	# kmeans_wine_pca()
	# em_wine_pca()
	# kmeans_wine_ica()
	# em_wine_ica()
	kmeans_wine_rand()
	em_wine_rand()
	# wine_reconstruction_error()


	pass


