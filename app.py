from loguru import logger
import sys
from config import DB_DETAILS
from util import get_tables, load_db_details
from read import read_table
from write import build_insert_query, load_table


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    a_tables = sys.argv[2]
    #logging.basicConfig(filename='data-copier.info', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
    #logging.basicConfig(filename='data-copier.err', encoding='utf-8', level=logging.error())
    logger.add("data-copier.info", format="{time} {level} [{message}]", rotation="1 MB", retention="10 days", level="INFO")
    db_details = load_db_details(env)
    tables = get_tables('tables', a_tables)
    #table_name= 'departments'
    for table_name in tables['table_name']:
        #print(f'reading data for {table_name}')
        #logging.info(f'reading data for {table_name}')
        logger.info(f'reading data for {table_name}')
        data,column_names = read_table(db_details,table_name,1000)

        #print(data)
        #print(f'loading data for {table_name}')
        #ogging.info('loading data for {table_name}')
        logger.error(f'loading data for {table_name}')
        load_table(db_details,data,column_names,table_name)

    # for rec in data:
    #     print(rec)



if __name__ == '__main__':
    main()

'''
set environment variables for environment variables and pass argument using parameter

using CLI:
export DB_USER_SRC=retail_user
export DB_PASS_SRC=itversity
.....
python app.py dev

GIT:
git init --intialize new git repository
    ls -ltr (.git) -- should only have source code related files (.py)
    Ignore (vi .gitignore):
        .idea -- keep track of preferences in pycharm
        __pycache__ --byte code of our source code
        data-copier-live-env  
git add . (pwd) [.gitignore, .py files and requirements.txt file]
git commit
git remote add origin <>
git push -u origin master

'''