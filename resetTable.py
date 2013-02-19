import sys
import _mysql as sql

try:
	con = sql.connection("localhost", "Eclipse", "hedgefund", "Eclipse")

	all_tables = ['Company', 'Document', 'Employee', 'Scripts', 'Stock']

	for i in sys.argv:
		if i in all_tables:
			print 'Resetting %s' % i
			table_del = "DELETE FROM %s;" % i
			con.query(table_del)
		if i == 'Company':
			con.query("ALTER TABLE Company AUTO_INCREMENT = 1;")
			con.query("INSERT INTO Company (ticker) VALUES (\'Dummy\');")
		elif i == 'Document':
			con.query("ALTER TABLE Document AUTO_INCREMENT = 1;")
			con.query("INSERT INTO Document (doc_name) VALUES (\'Dummy Doc\');")
		elif i == 'Employee':
			con.query("ALTER TABLE Employee AUTO_INCREMENT = 1;")
			con.query("INSERT INTO Employee (first_name, last_name) VALUES (\'Ruiqi\', \'Yu\');")
		elif i == 'Scripts':
			con.query("ALTER TABLE Scripts AUTO_INCREMENT = 1;")
			con.query("INSERT INTO Scripts (eid) VALUES (1);")
		elif i == 'Stock':
			con.query("ALTER TABLE Stock AUTO_INCREMENT = 1;")
			con.query("INSERT INTO Stock (ticker) VALUES (\'Dummy\');")
except sql.Error, e:
	print 'DB error %d: %s' % (e.args[0], e.args[1])
	sys.exit(0)

finally:
	if con:
		con.close()
