from mysql.connector import MySQLConnection, Error
 
def insert_values(year, injuries):
    query = "INSERT INTO fourth_table(year, injuries) " \
            "VALUES(%s, %s)"
    args = (year, injuries)
 
    try:
        config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'bootcamp'
        }
        conn = MySQLConnection(**config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        # Commit changes to the db
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   # execute one
   insert_values('2017','11111')

if __name__ == '__main__':
    main()