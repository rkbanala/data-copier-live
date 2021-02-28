import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '34.67.188.180',
            'DB_NAME':'retail_db',
            'DB_USER': os.environ.get('DB_USER_SRC'),
            'DB_PASS': os.environ.get('DB_PASS_SRC')
            },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '34.67.188.180',
            'DB_NAME': 'retail_dw',
            'DB_USER': os.environ.get('DB_USER_TGT'),
            'DB_PASS': os.environ.get('DB_PASS_TGT')
        }
    }
}

'''
env='dev'
db_details = DB_DETAILS[env]

from config import DB_DETAILS
db_details = DB_DETAILS[env]
db_details
conn = mc.connect(user=db_details['SOURCE_DB']['DB_USER'], password= ...
db_details['SOURCE_DB']

'''