import pandas as pd
import mysql.connector

#connect to db

connection = mysql.connector.connect(

    host = "[enter_host]",
    user = '[enter_user]',
    password = ["Password"],
    database = ["DB_Name"],

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
