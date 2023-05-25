import psycopg2

con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')

with con:
    cur = con.cursor()
    cur.execute(f"SELECT * FROM customer")