import sqlite3

conn = sqlite3.connect("Dashboard.db")
c =conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Logs (
        server_id NCHAR NOT NULL PRIMARY KEY,
        server_ip TEXT NOT NULL,
        os NCHAR NOT NULL,
        total_cpu INT NOT NULL,
        total_ram INT NOT NULL
    )""")
    print("Table has been created")

