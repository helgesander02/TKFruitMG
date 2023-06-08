import psycopg2
import pandas as pd
from collections import defaultdict
better_dict = defaultdict(list)
con = psycopg2.connect(database='postgres', user='postgres',
                       password='admin')
con.autocommit = True

cur = con.cursor()
cur.execute(f"select * from order_it where c_id='001' and date='2023-06-05'")
field_name = [des[0] for des in cur.description]
result = cur.fetchall()
test = []
for i in result:
    temp = []
    for j in i:
        temp.append(str(j).rstrip())
    test.append(temp)
# print(test)
for count in range(len(test)):
    for i in range(len(test[count])):
        better_dict[field_name[i]].append(test[count][i])

print(pd.DataFrame(better_dict).to_csv("20230609.csv",encoding="utf_8_sig"))