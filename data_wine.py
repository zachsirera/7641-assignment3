# This is the reader for the csv to parse the dataset to be used for the analysis
# Zach Sirera - Fall 2020

# Dataset details: 
# Name: Wine Quality Dataset

import csv
import random

def main(filename):
	data = get_all_data(filename)
	training_data, testing_data = separate_data_fixed(0.8, data)
	train_x, train_y = parse(training_data)
	test_x, test_y = parse(testing_data)

	return train_x, train_y, test_x, test_y

def get_all_data(filename):
	''' This function simply reads the csv into a dictionary which will then be parsed by the various learners depending on what 
	their individual input rules are. '''

	all_data = []

	with open(filename, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		next(reader)
		for row in reader:
			all_data.append({
				"fixed acidity": row[0],
				"volatile acidity": row[1],
				"citric acid": row[2],
				"residual sugar": row[3],
				"chlorides": row[4],
				"free sulfur dioxide": row[5],
				"total sulfur dioxide": row[6],
				"density": row[7],
				"pH": row[8],
				"sulphates": row[9],
				"alcohol": row[10],
				"quality": row[11]
				})

	return all_data

def separate_data_rand(fraction, data):
	''' This is a function to generate a set of indices at random to serve as training data and the rest will be test data '''

	training_data = []
	testing_data = []

	for each in data:
		if random.random() <= fraction:
			training_data.append(each)
		else:
			testing_data.append(each)

	return training_data, testing_data

def separate_data_fixed(fraction, data):

	training_data = []
	testing_data = []

	for each in data:
		if len(training_data) / len(data) <= fraction:
			training_data.append(each)
		else:
			testing_data.append(each)

	return training_data, testing_data


def parse(dataset):
	''' This is a function to parse the dataset dictionary and format it properly for the decision tree algorithm implementation '''

	x = []
	y = []

	for row in dataset:
		x.append([
			float(row["fixed acidity"]), 
			float(row["volatile acidity"]),
			float(row["citric acid"]),
			float(row["residual sugar"]),
			float(row["chlorides"]),
			float(row["free sulfur dioxide"]),
			float(row["total sulfur dioxide"]),
			float(row["density"]),
			float(row["pH"]),
			float(row["sulphates"]),
			float(row["alcohol"])
		])
		y.append(int(row["quality"]))

	return x, y
