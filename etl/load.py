import mysql.connector

def load_to_mysql(data, host='localhost', user='root', password='root', database='chicken_database'):

    conn = None  # initialize to avoid UnboundLocalError
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO products (chicken_name, breed, age, birthday)
        VALUES (%s, %s, %s, %s)
        """
    
        for row in data:
            cursor.execute(insert_query, (
                row['chicken_name'],
                row['breed'],
                row['age'],
                row['birthday']
                
            ))

        conn.commit()
        print(f"✅ Loaded {cursor.rowcount} rows into the database.")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
