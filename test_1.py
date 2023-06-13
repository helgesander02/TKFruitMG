import psycopg2
import sys


con = None

try:

    con = psycopg2.connect(database='postgres', user='postgres', password='admin')
    cur = con.cursor()
    cur.execute('SELECT * FROM customer')
    f = open('test.sql', 'w')
    for row in cur:
        f.write("insert into t values (" + str(row) + ");")
except psycopg2.DatabaseError as e:
    print('Error %s',e)
    sys.exit(1)
finally:
    if con:
        con.close()