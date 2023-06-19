import psycopg2
import pandas as pd
from collections import defaultdict
from datetime import date
import os
import shutil
table = ["customer","item","order_form","goods","accounting","receipt"]
td = date.today()
if not os.path.exists("./save_data"):
    os.mkdir("save_data")
else:
    shutil.rmtree("./save_data")


