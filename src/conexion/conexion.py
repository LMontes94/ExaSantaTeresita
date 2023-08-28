import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'l.montes94',
        password = '',
        database = 'db_exa',
        port = '5432'
    )
    print("conexion exitosa!!")
except Exception as e:
    print(e)
