import matplotlib.lines as mlines
import matplotlib.pyplot as plt

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

	scores = [{'n_clusters': 2, 'algorithm': 'full', 'silhouette_score': 0.5856371816421606, 'training_time': 0.94765305519104, 'distortion': 52610.00872775964, 'inertia': 120393454055628.36}, 
	{'n_clusters': 2, 'algorithm': 'elkan', 'silhouette_score': 0.5856371816421606, 'training_time': 0.6895678043365479, 'distortion': 52610.00872775964, 'inertia': 120393454055628.36}, 
	{'n_clusters': 3, 'algorithm': 'full', 'silhouette_score': 0.5525996096803132, 'training_time': 1.2591049671173096, 'distortion': 35916.6536859063, 'inertia': 64961089375380.945}, 
	{'n_clusters': 3, 'algorithm': 'elkan', 'silhouette_score': 0.5525996096803132, 'training_time': 0.8816578388214111, 'distortion': 35916.6536859063, 'inertia': 64961089375380.945}, 
	{'n_clusters': 4, 'algorithm': 'full', 'silhouette_score': 0.5552929658224097, 'training_time': 2.5451600551605225, 'distortion': 30512.49191353255, 'inertia': 43296744763739.016}, 
	{'n_clusters': 4, 'algorithm': 'elkan', 'silhouette_score': 0.5552929658224097, 'training_time': 1.7493979930877686, 'distortion': 30512.49191353255, 'inertia': 43296744763739.016}, 
	{'n_clusters': 5, 'algorithm': 'full', 'silhouette_score': 0.5302510027248235, 'training_time': 2.0035319328308105, 'distortion': 26520.990860823127, 'inertia': 31585717988549.703}, 
	{'n_clusters': 5, 'algorithm': 'elkan', 'silhouette_score': 0.5302510027248235, 'training_time': 1.5972778797149658, 'distortion': 26520.990860823127, 'inertia': 31585717988549.707}, 
	{'n_clusters': 6, 'algorithm': 'full', 'silhouette_score': 0.5439099077169363, 'training_time': 2.347353935241699, 'distortion': 20992.019000450637, 'inertia': 22885639861681.27}, 
	{'n_clusters': 6, 'algorithm': 'elkan', 'silhouette_score': 0.5439099077169363, 'training_time': 1.7137877941131592, 'distortion': 20992.019000450637, 'inertia': 22885639861681.26}, 
	{'n_clusters': 7, 'algorithm': 'full', 'silhouette_score': 0.5446942715818206, 'training_time': 2.4474611282348633, 'distortion': 19070.227553720084, 'inertia': 17266636881699.031}, 
	{'n_clusters': 7, 'algorithm': 'elkan', 'silhouette_score': 0.5446942715818206, 'training_time': 1.7167353630065918, 'distortion': 19070.227553720084, 'inertia': 17266636881699.031}, 
	{'n_clusters': 8, 'algorithm': 'full', 'silhouette_score': 0.5378195482341589, 'training_time': 2.63596510887146, 'distortion': 17726.96936222812, 'inertia': 13759472000825.178}, 
	{'n_clusters': 8, 'algorithm': 'elkan', 'silhouette_score': 0.5378195482341589, 'training_time': 1.9648501873016357, 'distortion': 17726.96936222812, 'inertia': 13759472000825.178}, 
	{'n_clusters': 9, 'algorithm': 'full', 'silhouette_score': 0.5308852827604604, 'training_time': 4.249449014663696, 'distortion': 15509.61111347089, 'inertia': 11006177022549.21}, 
	{'n_clusters': 9, 'algorithm': 'elkan', 'silhouette_score': 0.5308852827604604, 'training_time': 2.8348679542541504, 'distortion': 15509.61111347089, 'inertia': 11006177022549.21}]

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



if __name__ == '__main__':

	kmeans_adult()
	kmeans_wine()





