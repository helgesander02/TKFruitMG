import psycopg2
from datetime import date
con = psycopg2.connect('postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop')

with con:
    cur = con.cursor()
    
    #cur.execute(f"DELETE FROM accounting")
    #cur.execute(f"DELETE FROM receipt")

    """cur.execute(f"SELECT goods.o_id, goods.remark, SUM(goods.sub_total) \
                            FROM order_form JOIN goods \
                            ON order_form.o_id = goods.o_id \
                            WHERE order_form.c_id = '001' AND (goods.date BETWEEN SYMMETRIC '2023-06-10' AND '2023-06-13') \
                            GROUP BY goods.o_id, goods.remark")"""

    cur.execute(f"SELECT receipt.ac_id, receipt.date, receipt.m_way, SUM(receipt.money), SUM(receipt.discount), receipt.remark \
                            FROM accounting JOIN receipt \
                            ON accounting.ac_id = receipt.ac_id \
                            WHERE accounting.o_id = '20236130001' \
                            GROUP BY receipt.ac_id")

    #column_names = [desc[0] for desc in cur.description]
    #for i in column_names:
        #print(i)
    
    #cur.execute(f"SELECT * FROM goods")
    result = cur.fetchall()
    print(result)

    """cur.execute(f"SELECT accounting.o_id, SUM(receipt.money-receipt.discount) \
                            FROM accounting JOIN receipt \
                            ON accounting.ac_id = receipt.ac_id \
                            WHERE accounting.o_id IN \
                            ( \
                            SELECT goods.o_id \
                            FROM order_form JOIN goods \
                            ON order_form.o_id = goods.o_id \
                            WHERE order_form.c_id = '001' AND (goods.date BETWEEN SYMMETRIC '2023-06-10' AND '2023-06-13') \
                            GROUP BY goods.o_id \
                            ) \
                            GROUP BY accounting.o_id")
    result2 = cur.fetchall()"""
    
    """for i in range(len(result1)):
            al = 0
            overage = result1[i][2]
            for j in range(len(result2)):
                if result2[j][0] == result1[i][0]:
                    al = result2[j][1]
                    overage -= result2[j][1]

            print(al, overage)"""
