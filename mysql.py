# Importing MySQL connector library
import mysql.connector

# Step 1: Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",        # Your host (usually localhost)
    user="root",             # MySQL username
    password="your_password" # Replace with your MySQL password
)

# Step 2: Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Step 3: Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
print("Database created successfully!")

# Step 4: Connect to the created database
connection.database = "school"

# Step 5: Create a new table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
)
""")
print("Table created successfully!")

# Step 6: Insert data into the table
insert_query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
data = [
    ("John", 20, "Python"),
    ("Alice", 22, "Data Science"),
    ("Bob", 19, "AI")
]
cursor.executemany(insert_query, data)
connection.commit()
print("Data inserted successfully!")

# Step 7: Retrieve data (SELECT)
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()
print("\nAll Students:")
for row in records:
    print(row)

# Step 8: Update data
update_query = "UPDATE students SET course = 'Machine Learning' WHERE name = 'Alice'"
cursor.execute(update_query)
connection.commit()
print("\nRecord updated successfully!")

# Step 9: Delete data
delete_query = "DELETE FROM students WHERE name = 'Bob'"
cursor.execute(delete_query)
connection.commit()
print("Record deleted successfully!")

# Step 10: Display final table data
cursor.execute("SELECT * FROM students")
final_records = cursor.fetchall()
print("\nFinal Students Data:")
for row in final_records:
    print(row)

# Step 11: Close connection
cursor.close()
connection.close()
print("\nMySQL connection closed.")
