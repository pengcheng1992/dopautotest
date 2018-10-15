# -*- coding:utf8 -*-
# create by pengcheng
import pymysql.cursors
from conf import ApiSetting


def execute(sql, params=None, db='', is_fetchone=True):
    # Connect to the database
    connection = pymysql.connect(host=ApiSetting.DB_HOST,
                                 port=ApiSetting.DB_PORT,
                                 user=ApiSetting.DB_USER,
                                 password=ApiSetting.DB_PASSWORD,
                                 db=db,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    finally:
        connection.close()