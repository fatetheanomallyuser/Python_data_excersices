import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


connection_string = 'mysql+pymysql://root:[password]@localhost/[table_name]'
engine = create_engine(connection_string)

query = '''SELECT * FROM aqi_data'''


df = pd.read_sql_query(query, engine)

highest_aqi = df.groupby(['id','city_name'])['aqi'].mean().sort_values(ascending=True)

data = df.describe()

print(highest_aqi)

print(data)


