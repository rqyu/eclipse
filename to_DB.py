import sys
import _mysql as sql

def test(con):
	con.query("DELETE FROM Company where company_id=1;")
	con.query("INSERT INTO Company (company_id, ticker, company_name) VALUES (1, \"AAPL\", \"Apple Inc.\");")
	con.query("SELECT * FROM Company;")
	print "Test row entered: %s" % con.use_result().fetch_row()
	con.query("DELETE FROM Company where company_id=1;")

con = None

try:
	con = sql.connect(host='localhost', user='Eclipse', passwd='hedgefund', db='Eclipse')

	test(con)
	comm = '''
	con.query("show tables")
	result = con.use_result()

	while 1:
		r = result.fetch_row()
		print 'All tables in Eclipse: ', r
		if not r:
			break
'''
except sql.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:
	if con:
		con.close()
