import json
import requests
import mysql.connector
from time import gmtime, strftime

#acceso al servicio web del bicing
r = requests.get('http://pokeapi.co/api/v2/pokemon/clefairy')
bicingJson = r.json()

#conexión a la base de datos
try:
    conn = mysql.connector.connect (host='localhost',
                                         database='db11mayo',
                                         user='root',
                                         password='1234')
except:  
    print ("I am unable to connect to the database")

cursor = conn.cursor()
cursor.executemany("INSERT into pokemon35(id,nombre,base_experience,height,is_default,orden,weight) VALUES (%(id)s, %(name)s,%(base_experience)s,%(height)s,%(is_default)s,%(order)s,%(weight)s)",bicingJson['v2/pokemon/clefairy'])
conn.commit()
cursor.close()  