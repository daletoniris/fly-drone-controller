import mysql.connector
import csv
Archi = raw_input("input archive name ex: test.csv: ")

filename=open(Archi,'wb')
c=csv.writer(filename)

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='temperatura2')


cursor = cnx.cursor()

query = ("SELECT fecha, temp  from temps")

cursor.execute(query)

for fecha, temp  in cursor:
    c.writerow([fecha,temp] )
    
    

cursor.close()
filename.close()
cnx.close()
