import sys
from monte_carlo import Monte_carlo

f = open(sys.argv[1], 'r')

d = [x.rstrip('\n') for x in f.readlines()]
print(d)
print(1)
dic = {}

for i in d:
	print i
	if len(i.split(': '))>1:
		s = i.split(': ')[0]
		a = i.split(': ')[1]
		print(s,a)
		if (a != '') or (a != ' '):
			if dic.has_key(s):
				dic[s].extend(a.split(','))
			else:
				dic[s] = a.split(',')

for i in range(len(dic['Name'])):
	name = dic['Name'][i]
	s0 = float(dic['S0'][i])
	r = float(dic['R'][i])
	t = float(dic['t'][i])
	miu = -23.4
	alpha = -23.4
	theta = -23.4
	try:
		miu = float(dic['miu'][i])
	except:
		alpha = float(dic['alpha'][i])
		theta = float(dic['theta'][i])
	sd = float(dic['sd'][i])
	
	if miu == -23.4:
		mc = Monte_carlo(s0, r, t, miu, sd)
	else:
		mc = Monte_carlo(s0, r, t, alpha, theta, sd)
		
rlt = mc.simulate_complete()

fw = open(sys.argv[2], 'w')
summ = 0
leng = 0
max_ = -999999999
min_ = 999999999
for i in rlt:
	for j in i:
		summ += i[0]
		leng += 1
		max_ = max(max_, i[0])
		min_ = min(min_, i[0])

fw.write('<table>')

fw.write('<tr>')
fw.write('<td>')
fw.write('Stock')
fw.write('</td>')
fw.write('<td>')
fw.write(str(name))
fw.write('</td>')
fw.write('</tr>')

fw.write('<tr>')
fw.write('<td>')
fw.write('Number of run')
fw.write('</td>')
fw.write('<td>')
fw.write(str(leng))
fw.write('</td>')
fw.write('</tr>')

fw.write('<tr>')
fw.write('<td>')
fw.write('Average')
fw.write('</td>')
fw.write('<td>')
fw.write(str(summ/leng))
fw.write('</td>')
fw.write('</tr>')

fw.write('<tr>')
fw.write('<td>')
fw.write('Max')
fw.write('</td>')
fw.write('<td>')
fw.write(str(max_))
fw.write('</td>')
fw.write('</tr>')

fw.write('<tr>')
fw.write('<td>')
fw.write('Min')
fw.write('</td>')
fw.write('<td>')
fw.write(str(min_))
fw.write('</td>')
fw.write('</tr>')

fw.write('</table>')
fw.close()
