# import the necessary external libraries
from sklearn.neural_network import MLPClassifier

import data
import analyze

def train(train_x, train_y):
	''' this is function to train a neural network '''

	classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 6, 5), random_state=1)
	classifier.fit(train_x, train_y)

	return classifier	



def tune(train_x, train_y, test_x, test_y, min_layer, max_layer):
	''' this is a function to tune the neural network by adjusting the size of the hidden layers '''
	
	results = []

	for i in range(min_layer, max_layer):
		for j in range(min_layer, max_layer):
			for k in range(min_layer, max_layer):
				classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(i, j, k), random_state=1)
				classifier.fit(train_x, train_y)

				total = 0
				correct = 0

				for index, each in enumerate(test_x):
					total += 1
					result = classifier.predict([each])
					if result == test_y[index]:
						correct += 1

				results.append({'layers': (i, j, k), 'success': round(correct / total, 3)})

	return results