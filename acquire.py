import os
import pandas as pd
from env import username, host, password 

def get_connection(db, username=username, host=host, password=password):
    '''
    Creates a connection URL
    '''
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'


def new_curriculum_logs_data():
    '''
    Returns curriculum logs into a dataframe
    '''
    sql_query = '''select * from logs join cohorts on cohorts.id=logs.cohort_id'''
    df = pd.read_sql(sql_query, get_connection('curriculum_logs'))
    return df 

def get_curriculum_logs_data():
    '''get connection, returns curriculum log's logs table into a dataframe and creates a csv for us'''
    if os.path.isfile('curriculum-access.csv'):
        df = pd.read_csv('curriculum-access.csv')
    else:
        df = new_curriculum_logs_data()
        df.to_csv('curriculum-access.csv', index=False)
    return df

def new_grocery_data():
    '''
    Returns curriculum logs into a dataframe
    '''
    sql_query = '''select * from grocery_customers'''
    df = pd.read_sql(sql_query, get_connection('grocery_db'))
    return df    

def get_grocery_data():
    '''get connection, returns grocery_customers into a dataframe and creates a csv for us'''
    if os.path.isfile('grocery_db.csv'):
        df = pd.read_csv('grocery_db.csv')
    else:
        df = new_grocery_data()
        df.to_csv('grocery_db.csv', index=False)
    return df