import psycopg2
from datetime import date
con = psycopg2.connect('postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop')

with con:
    cur = con.cursor()
    #cur.execute("SELECT goods FROM goods")
    cur.execute("SELECT goods.o_id, goods.date, goods.remark, SUM(goods.sub_total)  \
                FROM order_form JOIN goods \
                ON order_form.o_id = goods.o_id \
                WHERE order_form.c_id = '001' and date='2023-06-10' \
                GROUP BY goods.o_id, goods.date, goods.remark \
                Order BY goods.date")

    result = cur.fetchall()
    print(result)