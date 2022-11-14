# Task to calculate the lifetime of requests and delete or update them
from mysql.connector import connect, Error

MINUS_NUM = 60

def counter(cursor):
        
    cursor.execute('SELECT * FROM main_request')
    result = cursor.fetchall()
    print(result)
    for req in result:
        new_req = req[5] - MINUS_NUM
        
        if new_req <= 0 and req[-1] == None:
            cursor.execute(f'DELETE FROM main_request WHERE id = {req[0]}')
        else:
            cursor.execute(f'UPDATE main_request SET lifespan = {new_req} WHERE id = {req[0]}')
            
try:
    with connect(
        host="localhost",
        user='root',
        password='Neetqw2110',
        database="tgif",
    ) as connection:
        with connection.cursor() as cursor:
            counter(cursor)
            connection.commit()
except Error as e:
    print(e)