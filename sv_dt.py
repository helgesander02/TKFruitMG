import psycopg2
import os

def sv():
    if not os.path.exists("./save_data"):
        os.mkdir("save_data")

    path = os.getcwd()
    pg_dump = "C:\\Program Files\\PostgreSQL\\15\\bin"
    os.chdir(pg_dump)
    #os.system(f"export PGPASSWORD='$admin'")
    os.system(f"pg_dump -U postgres -f {path}\\save_data\\copy.sql postgres")       
    os.chdir(path)