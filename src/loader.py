import pandas as pd
import matplotlib as plt
from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv


def dataLoder():
  load_dotenv()
  password = os.getenv("pgPassword")
  database_name = 'week01_telecom'
  table_name= 'xdr_data'

  connection_params = {"host": "localhost",
                       "user": "postgres", 
                        "password": password,
                        "port": "5432", 
                        "database": database_name}

  engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

  # str or SQLAlchemy Selectable (select or text object)
  sql_query = 'SELECT * FROM xdr_data'
  telecom_df = pd.read_sql(sql_query, con= engine)
  return telecom_df

# print (dataLoder().head(5))