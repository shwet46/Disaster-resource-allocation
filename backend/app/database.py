import psycopg2
from psycopg2 import sql

def init_db():
    conn = psycopg2.connect(dbname="disaster_db", user="user", password="password", host="db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS resource_allocation (id SERIAL PRIMARY KEY, zone TEXT, resources JSONB);")
    conn.commit()
    cur.close()
    conn.close()
