import sqlite3

# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory:')

curs = conn.cursor()
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
# conn.commit()
# curs.execute(
#     'INSERT INTO persons(name) values("satoru")'
# )

# curs.execute('INSERT INTO persons(name) values("SATORU")')
# curs.execute('INSERT INTO persons(name) values("OK@")')

# curs.execute('UPDATE persons set name = "satoru oka" WHERE name = "SATORU"')
curs.execute('DELETE FROM persons WHERE name = "satoru oka"')

conn.commit()
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()
conn.close()
