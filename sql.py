import psycopg2
from datetime import date
con = psycopg2.connect('postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop')

with con:
    cur = con.cursor()
    cur.execute("select * from goods")
    result = cur.fetchall()
    print(result)