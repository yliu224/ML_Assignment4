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
		result = []
		for i in range(0,len(self.X)):
			distance = 0
			for j in range(0,len(X)):
				X1 = int(self.X[i][j])
				X2 = int(X[j])
				distance += np.power(X1-X2,2)
			result.append([np.sqrt(distance),self.Y[i]])
		result.sort();
        classify = [0,0,0]
        for i in range(0,len(result)):
            if(result[i]==-1):
                classify[0]+=1
            if(result[i]==0):
                classify[1]+=1
            if(result[i]==1):
                classify[2]+=1
        return np.max(classify)

