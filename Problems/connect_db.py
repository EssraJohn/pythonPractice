import mysql.connector
conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="")
# Get a Cursor

cur = conn.cursor()
cur.execute("SELECT CURDATE()")
# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
conn.close()