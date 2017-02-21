from mysql.connector import MySQLConnection, Error

def get_key(my_tuple):
    return my_tuple[1]
 
def get_values():

    query = "SELECT year, injuries FROM fourth_table"
 
    try:
        config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'bootcamp'
        }
        conn = MySQLConnection(**config)
 
        cursor = conn.cursor()
        cursor.execute(query)

        # Create a container to hold these values
        tuple_container = []

        for(year, injuries) in cursor:
            tuple_container.append( (year, injuries) )

        print 'Original Container'
        print tuple_container

        print '\nSorter Container'
        new_container = sorted(tuple_container, key = get_key, reverse=True)
        print new_container

        # Now just find the first year
        print 'The year with the most injuries is: ', new_container[0][0]

    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   # execute one
   get_values()

if __name__ == '__main__':
    main()