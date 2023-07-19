import psycopg2

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