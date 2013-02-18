import random as rand
import math as m

class Monte_carlo:
	'''
	Two usage of monte_carlo function:
	first	S0, round, t, miu, sigma				5 parameters
	second	S0, round, t, alpha, theta, sigma		6 parameters
	
	S0: starting price of stock
	round: number of runs for monte carlo
	t: depth of forecasting
	miu: mean of lognormal distribution
	sigma: standard deviation of lognormal distribution
	
	alpha: the stock's continuously annual compounded rate of return
	theta: the stock's continuous annual divident rate
	
	there are two methods to do calculation
	
	'''
	S0 = 40
	round = 1000
	t = 1
	miu = 3
	sigma = 4
	
	alpha = 0.2
	theta = 0.02
	def __init__(self, *args, **kwargs):
		if len(args) == 5:
			self.S0 = args[0]
			self.round = args[1]
			self.t = args[2]
			self.miu = args[3]
			self.sigma = args[4]
			
		if len(args) == 6:
			self.S0 = args[0]
			self.round = args[1]
			self.t = args[2]
			self.alpha = args[3]
			self.theta = args[4]
			self.sigma = args[5]
			self.miu = self.alpha - self.theta - self.sigma**2 * 0.5
			
	def __repr__(self):
		return 'S0: %s; R: %s; t: %s; miu: %s; sigma: %s; alpha: %s; theta: %s;' % (self.S0, self.round, self.t, self.miu, self.sigma, self.alpha, self.theta)
		
	def __str__(self):
		return 'S0: %s; R: %s; t: %s; miu: %s; sigma: %s; alpha: %s; theta: %s;' % (self.S0, self.round, self.t, self.miu, self.sigma, self.alpha, self.theta)
			
	def rand_lognormal_gen(self):
		z = 0
		for i in range(12):
			z = z + rand.uniform(0,1)
		z = z - 6
		n = self.miu + self.sigma*z
		x = m.exp(n)
		return x
		
	def simulate_once(self):
		
		rlt = []
		s = self.S0
		for i in range(self.t):
			s = s * self.rand_lognormal_gen()
			rlt.append(s)
		
		return rlt
	
	def simulate_complete(self):
		rlt = []
		s = []
		for i in range(self.round):
			s = self.simulate_once()
			rlt.append(s)
			
		return rlt