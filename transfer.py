import sqlite3
import json
import uuid

conn = sqlite3.connect('instance/development.db')
cursor = conn.cursor()


with open('countries.json', 'r') as file:
    countries = json.load(file)

for country in countries:
    cursor.execute("SELECT * FROM country WHERE code=?", (country['code'],))
    data = cursor.fetchone()
    if data is None:
        countries_id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO country (id, name, code) VALUES (?, ?, ?);",
            (countries_id, country['name'], country['code'])
        )

conn.commit()
cursor.close()
conn.close()
