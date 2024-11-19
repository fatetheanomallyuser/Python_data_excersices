import pandas as pd
import mysql.connector

#connect to db

connection = mysql.connector.connect(

    host = "127.0.0.1",
    user = 'root',
    password = "Brazuka17!",
    database = "aqi_epa_gov",

)

cursor = connection.cursor() 


query = '''SELECT * FROM aqi_data'''

cursor.execute(query)

results = []
for i, data in enumerate(cursor):
    results.append(data)

cursor.close()
connection.close()

df = pd.DataFrame(results)

print(df)