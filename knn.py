from classifier import classifier
import numpy as np

class knn(classifier):
	"""docstring for knn"""
	def __init__(self,k=3):
		self.k = k
		self.X = []
		self.Y = []

	def fit(self,X,Y):
		self.X = X
		self.Y = Y

	def predict(self,X):
		print(self.X)
		# result = []
		# for i in range(0,len(self.X)):
		# 	distance = 0
		# 	for j in range(0,len(X[i])):
		# 		print(type(self.X[i][j]))
		# 		X1 = int(self.X[i][j])
		# 		X2 = int(X[j])
		# 		print(type(X1))
		# 		distance += np.power(X1-X2)
		# 	result.append([np.sqrt(distance),self.Y[i]])
		# return result

