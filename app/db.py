import psycopg2

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        dbname="metrics-api",
        user="postgres",
        password="Vishi"
    )                  

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a sample query
    cursor.execute("SELECT version();")

    # Fetch and print the result
    print("PostgreSQL database version:", cursor.fetchone())

    # Close the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
