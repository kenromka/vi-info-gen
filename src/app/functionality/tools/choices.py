import sys, random

if sys.version >= '3.6':
	choices = random.choices
else:
	def choices(population, weights=None, *, cum_weights=None, k=1):
		if weights and cum_weights:
			raise TypeError('Cannot specify both weights and cumulative weights')
		if weights and len(population) != len(weights):
			raise ValueError('The number of weights does not match the population')
		if cum_weights and len(population) != len(weights):
			raise ValueError('The number of weights does not match the population')
		if cum_weights:
			weights = [cum_weights[0]]
			for w in cum_weights[1:]:
				weights.append(w - weights[-1])
		if weights:
			population = []
			for p, w in zip(population, weights):
				population += [p] * w
		res = []
		for _ in range(k):
			res.append(random.choice(population))
		return res
