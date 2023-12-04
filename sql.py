import os
import psycopg2
import time
import customtkinter as ctk
import tkinter as tk

def back_up():
    path = os.getcwd()
    restore_PATH = ctk.filedialog.askopenfilename()
    if restore_PATH != "":
        delete_database()
        pg_dump = "C://Program Files//PostgreSQL//15//bin"
        os.chdir(pg_dump)
        restore_CMD=f'psql --dbname=postgresql://postgres:admin@localhost:5432/postgres -f {restore_PATH}'
        os.system(restore_CMD)
        tk.messagebox.showinfo(title='成功', message="恢復成功", )
        os.chdir(path)

def delete_database():
    try:
        conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
        cursor = conn.cursor()

        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_names = [row[0] for row in cursor.fetchall()]

        for table_name in table_names:
            delete_query = f"DELETE FROM {table_name}"
            cursor.execute(delete_query)
            conn.commit()

    except Exception as e:
        tk.messagebox.showinfo(title='失敗', message="需要呼叫工程師!!", )

    finally:
        if conn:
            cursor.close()
            conn.close()

def sv():
    if not os.path.exists("./save_sql"):
        os.mkdir("save_sql")

    path = os.getcwd()
    TIMESTAMP = time.strftime('%Y-%m-%d-%H-%M-%S')
    BACKUP_FILE = f'{TIMESTAMP}.sql'
    BACKUP_PATH = f"{path}//save_sql"
    os.chdir(BACKUP_PATH)
    
    pg_dump = "C://Program Files//PostgreSQL//15//bin"
    os.chdir(pg_dump)
    BACKUP_CMD = f"pg_dump --dbname=postgresql://postgres:admin@localhost:5432/postgres > {BACKUP_PATH}//{BACKUP_FILE} "
    os.system(BACKUP_CMD)
    os.chdir(path)
    tk.messagebox.showinfo(title='成功', message="備份成功", )

def createdatatable():
    con = psycopg2.connect(database="postgres", user="postgres", password="admin", host="localhost")
    #con = psycopg2.connect("postgres://su:fJoZOP7gLXHK1MYxH8iy3MtUPg1pYxAZ@dpg-cif2ddl9aq09mhg7f8i0-a.singapore-postgres.render.com/fruit_cpr4")
    cur = con.cursor()

    with con:
        cur.execute('''CREATE TABLE customer \
        (c_id CHAR(20) PRIMARY KEY NOT NULL, \
            name CHAR(20) NOT NULL, \
            phone CHAR(20), \
            address CHAR(100), \
            remark CHAR(100));''') 

        cur.execute('''CREATE TABLE item \
        (item_id CHAR(20) PRIMARY KEY NOT NULL, \
            item_name CHAR(20) NOT NULL);''') 

        cur.execute('''CREATE TABLE order_form \
        (o_id CHAR(20) PRIMARY KEY NOT NULL, \
            c_id CHAR(20) NOT NULL);''') 

        cur.execute('''CREATE TABLE goods \
        (o_id CHAR(20) NOT NULL, \
            item_id CHAR(20) NOT NULL, \
            item_name CHAR(20) NOT NULL, \
            date CHAR(20) NOT NULL, \
            specification CHAR(20) NOT NULL, \
            size CHAR(20) NOT NULL, \
            price int NOT NULL, \
            quantity  int NOT NULL, \
            sub_total int NOT NULL, \
            Remark CHAR(100));''') 

        cur.execute('''CREATE TABLE accounting \
        (ac_id CHAR(20) PRIMARY KEY NOT NULL, \
            o_id CHAR(20) NOT NULL);''') 
        
        cur.execute('''CREATE TABLE receipt \
        (ac_id CHAR(20) NOT NULL, \
            date CHAR(20) NOT NULL, \
            m_way CHAR(20) NOT NULL, \
            money int NOT NULL, \
            discount int NOT NULL, \
            remark CHAR(100));''') 