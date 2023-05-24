import psycopg2
import sys

con =  psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "admin",
    port = "5432"
)
cur = con.cursor()


query = '''CREATE TABLE customer1(
	ID CHAR(50) NOT NULL PRIMARY KEY,
	CUSTOMER_NAME CHAR(50) NOT NULL,
	PHONE_NUMBER CHAR (50) NOT NULL,
	ADDRESS CHAR (50) NOT NULL,
	REMARK CHAR (50)
);'''

cur.execute(query=query)
