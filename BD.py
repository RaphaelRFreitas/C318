import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="ag002")

mycursor = mydb.cursor()

# Select all records and headers from the "breast-cancer" table, and return the result:
mycursor.execute("SELECT * FROM ag002.`breast-cancer`")
headers = [column[0] for column in mycursor.description]
result = mycursor.fetchall()
print(result)

# Create a Pandas DataFrame from the result:
df = pd.DataFrame(result, columns=headers)
print(df.head())


mycursor.close()
mydb.close()