class Candidate:
	def __util__(self, name, data):
		self.candidate = name
		self.data = data.loc[data['endoresee'] == name]

	def countEndoresments(self):
		return len(self.data)

	def getScores(self):
		return self.data["points"]

	