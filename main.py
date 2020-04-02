from utils import *
from poll import poll

df = loadAndCleanData("2020_democratic_presidential_nomination-6730.csv")

#create a list of poll objects from my dataframe
pollNames = pd.unique(df["Poll"])
print (pollNames)

polls = []
for name in pollNames:
	poll = Poll(name,df)
	polls.append(poll)
	pollCOunt = poll.countPoll()
	print("Number of Polls: " + str(pollCount))

	print(polls.outlet)
	print(poll.getMostRecentPoll())
	print("number of polls: " + str(poll.countPoll()))
	print("change in poll for Sanders " + str(poll.changeInPoll("Sanders")))
	print("average in poll for Sanders " + str(poll.avgInPoll("Sanders")))
	print("Median in poll for sanders " + str(poll.medianInPoll("Sanders")))
	print("correlation between Sanders and Buttigieg " + str(poll.correlatedPolls("Sanders","Buttigieg")))
	if (pollCount > 1):
		print("Biden's Polling numbers: " + str(poll.avgInPoll("Biden")) + "+/- " str(poll.pollUncertainty()))
		print("Sander's Polling numbers: " + str(poll.avgInPoll("Sanders")) + "+/- " str(poll.pollUncertainty()))