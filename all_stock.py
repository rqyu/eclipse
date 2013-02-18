import urllib2 as url
import sys
import csv

def getPage(exchange, initial, store_crude=0, store_processed=1,debug=0):
	initial = '/%s.htm' % initial
	baseURL = "http://eoddata.com/stockquote/"
	URL = baseURL + exchange + subpage
	if debug == 1:
		print URL
	page = url.urlopen(URL)
	a = page.read()

	store = store_crude
	if (store == 1):
		f = file(exchange+'_'+initial+'.txt', 'w')
		f.write(a)
		f.close()

	process = store_processed
	rlt = []
	if (process == 1):
		frag = a.split('"ro"')[1:]
		if debug == 1:
			print len(frag)
		for i in frag:
			if debug == 1:
				print 'the i: ', i
			if '"ro"' in i and '"re"' not in i:
				if debug == 1:
					print 'name: ', name
					print 'first ticker: ', name.split('.htm')[0].split('/')[-1]
				name = i.split('"re"')[0]
				rlt.append(name.split('.htm')[0].split('/')[-1])
			elif '"re"' in i:
				name = i.split('"re"')[0]
				name2 = i.split('"re"')[1]
				if debug == 1:
					print 'name: ', name
					print 'name2:', name2
					print 'first ticker: ', name.split('.htm')[0].split('/')[-1]
					print 'second ticker: ', name2.split('.htm')[0].split('/')[-1]
				rlt.append(name.split('.htm')[0].split('/')[-1])
				rlt.append(name2.split('.htm')[0].split('/')[-1])
			elif 'script' in i:
				name = i.split('script')[0]
				ignore = i.split('script')[1]
				if debug == 1:
					print 'name: ', name
					print 'ignore: ', ignore
				rlt.append(name.split('.htm')[0].split('/')[-1])
				if '"re"' in ignore:
					if debug == 1:
						print 'Last ticker hit'
					name2 = ignore.split('"re"')
					rlt.append(name2.split('.htm')[0].split('/')[-1])
	if debug == 1:
		print rlt
	return rlt

def debug(de):
	print '-- debugging --'
	#getPage('NASDAQ','B', debug=int(de))
	f = file('all_NASDAQ','r')
	lines = []
	lines.extend([x.rstrip('\r\n') for x in f.readlines()])
	getStockInfo(lines, debug=1)

def getStockInfo(stocklist, debug=0):
	exchange = stocklist[0]
	filename = '%s_stock_info.csv' % exchange
	if debug == 1:
		print 'The exchange: ', exchange

	rlt = [['Name', 'Sector', 'Industry', 'P/E ratio', 'PEG ratio', 'EPS', 'DivYield', 'PtB', 'PtS', 'EBITDA', 'Shares', 'Market Cap', '52wk range']]
	if debug == 1:
		print 'first line: ', rlt
	sub = []
	for i in stocklist[1:]:
		print 'Going through stock: ', i
		subpage = '/%s.htm' % i
		baseURL = "http://eoddata.com/stockquote/"
		URL = baseURL + exchange + subpage
		print URL
		page = url.urlopen(URL)
		pageContent = page.read()
		pageContent = pageContent.split('>FUNDAMENTALS</')[1]
		pageContent = pageContent.split('table')[2]
		pageContent = pageContent.split('</td></tr>')
		sub.append(i)
		for i in pageContent:
			sub.append(i.split('</td><td>')[-1])
		rlt.append(sub)
		sub = []
	
	try:
		with open(filename, 'wb') as csvfile:
			writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
			for i in rlt:
				writer.writerow(i)
	except:
		print csv.Error

	
def verification(csvFileName):
	try:
		with open(csvFileName, 'rb') as csvfile
			reader = csv.reader(csvfile)
			

def main():
	try:
		de = sys.argv[1]
	except:
		de = 0
	if int(de)==0:

		
		a = []
		alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
		for i in alpha:
			rlt = getPage(ex, i)
			a.extend(rlt)

		f = file('all_%s' % ex, 'w')
		f.write('%s\n', ex)
		for i in a:
			f.write('%s\n' % i)
		f.close()
		'''
		f = file('all_NYSE','r')
		lines = []
		lines.extend([x.rstrip('\r\n') for x in f.readlines()])
		getStockInfo(lines)
		'''

	else:
		debug(de)

main()