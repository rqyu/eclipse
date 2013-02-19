import sys
import MySQLdb as sql
import csv
import urllib2 as url
import datetime as d

con = None

try:
	con = sql.connect("localhost", "Eclipse", "hedgefund", "Eclipse")
	cur = con.cursor()

	prepare_deletion = []

	to_company = '''
	readin = 'NYSE_stock_info.csv'
	c = 1
	DNE = -999999
	with open(readin, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for i in reader:
			ticker = str(i[0])
			sector = str(i[1])
			industry = str(i[2])
			try:
				PE = float(i[3])
			except:
				PE = DNE
			try:
				EPS = float(i[3])
			except:
				EPS = DNE
			try:
				market_cap = float(i[3])
			except:
				market_cap = DNE
			insertion = "INSERT INTO Company (ticker, exchange, sector, industry, \
			                                  PE, EPS, market_cap, entry_time) \
				VALUES (\'%s\', \'%s\', \'%s\', \'%s\', %f, %f, %f, Now());" % \
				(ticker, 'NYSE', sector, industry, PE, EPS, market_cap)
			prepare_deletion.append('DELETE FROM Company WHERE ticker=\'%s\';' % ticker)
			con.query(insertion)
	'''

#	to_stock = '''
	cur.execute("""SELECT max(price_id),ticker FROM Stock;""")
	break_point = [[x[0], x[1]] for x in cur.fetchall()]
	cur.execute("""ALTER TABLE Stock AUTO_INCREMENT=%d;""" % break_point[0])
	cur.execute("""DELETE FROM Stock WHERE ticker=\'%s\'""" % break_point[1])
	cur.execute("""SELECT ticker,company_id FROM Company WHERE ticker>=\'%s\';""" % break_point[1])
	all_ticker = [x[0] for x in cur.fetchall()]
	#print 'got tickers']
	coun = 0
	for i in all_ticker[2:]:
		#print 'processing ', i
		today_year = d.date.today().year
		today_month = d.date.today().month
		today_day = d.date.today().day
		#print 'getting link for ', i
		try:
			link = 'http://ichart.yahoo.com/table.csv?s=%s&a=0&b=1&c=%d&d=%d&e=%d&f=%d&g=w&ignore=.csv' \
				% (i, today_year-3, today_month-1, today_day, today_year)
		#	print link
			page = url.urlopen(link)
			a = page.read()
		#	print 'page read'
			b = a.split('\n')
		except:
			continue

		cont = 0

		for j in b:
			if 'Date' not in j:
				#print 'getting day info'
			#	print i
				c = j.split(',')
				if len(c) < 7:
					break
				date = c[0]
				open_ = float(c[1])
				close = float(c[4])
				high = float(c[2])
				low = float(c[3])
				volume = int(c[5])
				adj_close = float(c[6])
				insertion = """INSERT INTO Stock (ticker, p_date, open, high, low, close, vol, adj_close) \
							VALUES (\'%s\', \'%s\', %f, %f, %f, %f, %d, %f)""" % \
							(i, date, open_, close, high, low, volume, adj_close)
				deletion = """DELETE FROM Stock WHERE ticker=\'%s\'""" % i
				prepare_deletion.append(deletion)
				cur.execute(insertion)

#	'''
except sql.Error, e:
	print 'DB connection error %d: %s' % (e.args[0], e.args[1])
	for i in prepare_deletion:
		cur.execute(i)
	sys.exit(0)
except csv.Error, csve:
	print 'CSV loading error: ', csve
except IOError, ioe:
	print 'I/O error({0}): {1}'.format(ioe.errno, ioe.strerror)
except ValueError, ve:
	print "file value exception"
except url.URLError, urle:
	print 'url error'

finally:
	if con:
		con.close()
