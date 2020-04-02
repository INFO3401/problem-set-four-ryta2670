from utils import *
import pandas as pd
import math
import numpy as np
import scipy.stats
import statsmodels.api as sem
from statsmodels.formula.api import ols

df = loadAndCleanData("creditData.csv")

def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	print(data)
	return data

def computeProbability(feature, bin, data):
	#count the number of datapoints in the bin
	count = 0.0
	for i,datapoint in data.iterrows():
		#see if the data is in the right bin
		if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
			count += 1
	#count the total number of datapoints
	totalData = len(data)
	#divide the number of people in the bin by the total number of people
	probability = count / totalData
	#return the results
	return probability

def computeConfidenceInterval(data):

	#confidence interval
	npArray = 1.0 * np.array(data)
	stdErr = scipy.stats.sem(npArray)
	n = len(data)
	return stdErr * scipy.stats.t.ppf((1+.95)/2.0, n - 1)



def getEffectSize(d1,d2):
	m1 = d1.mean()
	m2 = d2.mean()
	s1 = d1.std()
	s2 = d2.std()

	return (m1 - m2) / math.sqrt((math.pow(s1, 3) + math.pow(s2,3)) / 2.0)

def runTTest(d1,d2):
	return scipy.stats.ttest_ind(d1,d2)



#pip install statsmodels

#vars is a string with our independent and dependent variables
# "dvs ~ ivs"
def runANOVA(dataframe, vars):
	model = ols(vars, data=dataframe).fit()
	aov_table = sm.stats.anova_lm(model, typ=2)
	return aov_table





























