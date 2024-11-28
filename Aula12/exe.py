import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# Obter dados
try:
    print('Obtendo dados...')
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    # Obtendo as variáveis de ambiente
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    df_base = pd.read_sql('basedp', engine)
    df_roubo_celular = pd.read_sql('basedp_roubo_celular', engine)
    # print(df_base.head())
    # print(df_roubo_celular.head())

except

