import pandas as pd
import psycopg2
from mysql import connector as mc
from mysql.connector import errorcode as ec
from config import DB_DETAILS


def load_db_details(env):
    #print(env)
    return DB_DETAILS[env]

def get_mysql_connection(db_host, db_name, db_user, db_pass):
    # try:
    #     connection = mc.connect(user=db_user,
    #                             password=db_pass,
    #                             host=db_host,
    #                             database=db_name)
    #
    # except mc.Error as error:
    #     if error.errno == ec.ER_ACCESS_DENIED_ERROR:
    #         print('invalid db credentials')
    #     else:
    #         print(error)
    #
    # finally:
    #     return connection

    connection = mc.connect(user=db_user,
                            password=db_pass,
                            host=db_host,
                            database=db_name)
    return connection

def get_postgres_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} password ={db_pass}")

    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print('invalid credentials')
        else:
            print(error)
    return connection

def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name = db_name,
                                          db_user=db_user,
                                          db_pass=db_pass)
    elif db_type == 'postgres':
        connection = get_postgres_connection(db_host=db_host,
                                          db_name = db_name,
                                          db_user=db_user,
                                          db_pass=db_pass)
    # else:
    #     print('invalid entry')

    return connection

def get_tables(path, a_tables):
    tables =pd.read_csv(path, sep=':')
    if a_tables == 'all':
        return tables.query('to_be_loaded=="yes"')
    else:
        tables_df = pd.DataFrame(a_tables.split(","), columns=['table_name'])
        return tables.join(tables_df.set_index('table_name'), on = 'table_name'). \
            query('to_be_loaded=="yes"')
