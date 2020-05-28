### USED TO TEST DATABASE CONNECTION.

# ENSURE basesecrets HAS THE CORRECT CREDENTIALS


import psycopg2

import immortality.immortality.basesecrets as basesecrets

try:
    connection = psycopg2.connect(user=basesecrets.POSTGRES_USER,
                                  password=basesecrets.POSTGRES_USER_PASSWORD,
                                  host=basesecrets.POSTGRES_IP,
                                  port=basesecrets.POSTGRES_PORT,
                                  database=basesecrets.POSTGRES_DB_NAME)

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT * FROM testtable;")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
