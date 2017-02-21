from mysql.connector import MySQLConnection, Error
import numpy as np
import matplotlib.pyplot as plt

# Determine what to sort by
def get_key(my_tuple):
    return my_tuple[1]

def formatted_coefficients(coeff):

    current_power = len(coeff) - 1
    my_str = ''

    for curr in coeff:
        if current_power == 0:
            my_str = ''.join([my_str, str(curr)])
        else:
            my_str = ''.join([my_str, str(curr), 'x^', str(current_power), ' + '])

        current_power -= 1

    return my_str

def extrapolate(coeffs, x_value):
    x_values = []
    powers = []
    current_power = len(coeffs) - 1

    for coeff in coeffs:
        x_values.append(x_value)
        powers.append(current_power)
        current_power -= 1


    new_list = np.power(x_values, powers)
    final_answer = 0

    index = 0
    for item in new_list:
        final_answer += item * coeffs[index]
        index += 1

    return final_answer
 
# Connect to the database and pull the information that is important to us
def connect():

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
        year_container = []
        injury_container = []

        for(year, injuries) in cursor:
            year_container.append(year)
            injury_container.append(injuries)

        # Fit a 5th order polynomial to the data
        desired_order = 5
        x = np.asarray(year_container)
        print x
        print x.shape
        # print x
        y = np.asarray(injury_container)
        # print y
        z = np.polyfit(x, y, desired_order)
        print z

        print '\nBut we can print this out nicer...'
        print formatted_coefficients(z)

        print '\n We can also plot it...'
        print extrapolate(z, 2017)



    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   connect()

if __name__ == '__main__':
    main()