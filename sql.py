import psycopg2
import sys

con =  psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "admin"
)
cur = con.cursor()

cur.execute("SELECT * from customer")
rows = cur.fetchall()

for row in rows:
    print(f"id:{row[0]}\nname:{row[1]}\nphone:{row[2]}\naddress:{row[3]}\nremark:{row[4]}")
