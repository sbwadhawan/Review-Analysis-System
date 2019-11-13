import pandas as pd
import pymysql

connection=pymysql.connect(host='localhost',user='root',port=3306,database='lms',autocommit=True)
