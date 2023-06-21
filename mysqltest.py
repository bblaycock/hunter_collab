import mysql.connector

cnx = mysql.connector.connect(user='PythonSQL', password='password',
                              host='127.0.0.1',
                              database='sql_hr')
#cursor = cnx.cursor()
cursor = cnx.cursor(dictionary=True) 

query = ("SELECT * FROM sql_hr.employees")


cursor.execute(query)


#for x in cursor:
  #print(x) 


#cursor.execute(query)
#for x in cursor:
  #print(x["job_title"],x["last_name"]) 
  #print(x["last_name"]) 
print(type(cursor))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict)) 
print(len(thisdict))