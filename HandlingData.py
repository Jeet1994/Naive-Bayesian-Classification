Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import csv
>>> def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

>>> filename = 'G:/CODEWORK/bayes_classification.csv'
>>> dataset = loadCsv(filename)
>>> print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
Loaded data file G:/CODEWORK/bayes_classification.csv with 768 rows
>>> 
