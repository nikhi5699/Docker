import pymysql

# MySQL database configuration
host = "mysql"  # This should be the name of the MySQL container in the same network
user = "root"
password = "Password123"
database = "mydatabase"

# Connect to the MySQL database
connection = pymysql.connect(host=host, user=user, password=password, database="mydatabase")

# Create a cursor object
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM users")  

# Fetch all rows
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

