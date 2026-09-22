import sqlite3

conn = sqlite3.connect('mydatabase.db')

cur = conn.cursor()

cur.execute("""
    create table if not exists users (
        id integer primary key autoincrement,
        name text not null,
        age intiger not null,
        city text not null
    )
""")

cur.execute("INSERT INTO users (name, age, city) VALUES ('alice',25,'new york')")
cur.execute("INSERT INTO users (name, age, city) VALUES ('bob',30,'los angiles')")
cur.execute("INSERT INTO users (name, age, city) VALUES ('charlie',35,'chicago')")

conn.commit()

cur.execute("SELECT * FROM users WHERE age < 28")
rows = cur.fetchall()

print("user older than 28:")
for row in rows:
    print(f"id: {row[0]}, name: {row[1]}, age: {row[2]}, city: {row[3]}")

conn.close()