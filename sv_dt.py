import psycopg2
import pandas as pd
from collections import defaultdict
from datetime import date
import os

def sv():
    if not os.path.exists("./save_data"):
        os.mkdir("save_data")
    os.chdir("./save_data")
    con = psycopg2.connect("postgres://fruitshop_user:wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1@dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com/fruitshop")
    con.autocommit = True

    table = ["customer","item","order_form","goods","accounting","receipt"]
    td = date.today()
    for tb in table:
        better_dict = defaultdict(list)
        cur = con.cursor()
        cur.execute(f"select * from {tb}")
        field_name = [des[0] for des in cur.description]
        result = cur.fetchall()
        test = []
        # df = pd.DataFrame()
        for i in result:
            temp = []
            for j in i:
                temp.append(str(j).rstrip())
            test.append(temp)
        for count in range(len(test)):
            for i in range(len(test[count])):
                better_dict[field_name[i]].append(test[count][i])
        pd.DataFrame(better_dict).to_csv(f"{td.year}{td.month}{td.day}-{tb}.csv",encoding="utf_8_sig")

    os.chdir("../")