import math
import numpy as numpy
import scipy.stats

class poll:
	#start with poll name and data
	def __init__(self,name,df):
		self.outlet = name
		self.data = df.loc[df['Poll']==name]

	def getMostRecentPoll(self):
		return self.data.iloc[0]

	def countPoll(self):
		return len(self.data)

	def changeInPoll(self,candidate):
		candidateData = self.data[candidate]
		return candidateData.iloc[0] - candidateData.iloc[len(candidateData) - 1]



	def avgInPoll(self,candidate):
		return self.data[candidate].mean()

	def medianInPoll(self, candidate):
		return self.data[candidate].median()

	def correlatedPolls(self, candidate1, candidate2):
		if (self.countPoll() == 1):
			print("Not enough data")
			return 0
		else:
			return self.data[candidate1].corr(self.data[candidate2])


	def pollUncertainty(self, candidate):
		#standard deviation
		return self.data[candidate].std()
		#IQR
		upperQuantile = self.data[candidate].quantile(.75)
		lowerQuantile = self.data[candidate].quantile(.25)
		return upperQuantile - lowerQuantile
		#Margin of error
		n= self.countPoll
		sigma = self.data[candidate].std()
		z = 1.96
		return z * sigma / math.sqrt(n)

		#confidence interval
		npArray = 1.0 * np.array(self.data[candidate])
		stdErr = scipy.stats.sem(npArray)
		n = self.countPoll()
		return stdErr * scipy.stats.t.ppf((1+.95)/2.0, n - 1)
























































			