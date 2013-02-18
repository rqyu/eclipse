import sys
import _mysql as sql

con = None

try:
	con = sql.connect('199.195.141.236', 'Eclipse', 'hedgefund', 'Eclipse')

	con.query("SHOW TABLES")
	result = con.use_result()

	print 'All tables in Eclipse: ', result.fetch_row()
except sql.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:
	if con:
		con.close()
