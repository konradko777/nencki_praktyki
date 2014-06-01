import sqlite3
conn = sqlite3.connect('dataSimilarity.db')
c = conn.cursor()

c.execute('''CREATE TABLE dataSimilarity 
	(caseID text, iteration int, msq real, ncorr real , nmi real , mmi real)''')

conn.commit()
conn.close()
