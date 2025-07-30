import mysql.connector
import time

# Wait for MySQL container to be ready
time.sleep(10)

try:
    conn = mysql.connector.connect(
        host='my-mysql',
        user='user',
        password='pass',
        database='mydb'
    )
    cursor = conn.cursor()

    # Drop table if it exists
    cursor.execute("DROP TABLE IF EXISTS people")

    # Create table
    cursor.execute("CREATE TABLE IF NOT EXISTS people (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

    # Insert one row
    cursor.execute("INSERT INTO people (name) VALUES ('Surya')")
    cursor.execute("INSERT INTO people (name) VALUES ('Pruthvi')")
    cursor.execute("INSERT INTO people (name) VALUES ('Siddharth')")    
    conn.commit()

    # Read and print rows
    cursor.execute("SELECT * FROM people")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print("Error:", err)

 