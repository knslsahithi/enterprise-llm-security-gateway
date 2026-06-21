from database.db_connection import engine

try:
    connection = engine.connect()

    print("Database Connected Successfully")

    connection.close()

except Exception as e:
    print(e)