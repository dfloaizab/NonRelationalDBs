import couchdb
#conexión a la BD:

user = "admin"
pwd = "admin"
host = "127.0.0.1"
port = "5984"

#couch_server  = couchdb.Server("http://admin:admin@127.0.0.1:5984/")
couch_server = couchdb.Server(f"http://{user}:{pwd}@{host}:{port}/")

db_name = "refugio_animales"

#ejemplo de creación de un store que no aún no existe
#couch_server.create(db_name)

#selección de un store existente:
db = couch_server[db_name]

#Operaciones del crud:
# (1) Insert: creación de un documento
#información de dos refugios:
db.save({"_id":"1","nit":"98989898","rep_legal":"Diego L","fondos":0.0})
db.save({"_id":"2","nit":"50505050","rep_legal":"Diana L","fondos":0.0})

# (2)  Select: selección de un documento por un determinado valor de llave ("_id")
doc_creado = db["1"]
print(doc_creado)
#  Otra forma de ejecutar queries usando el lenguaje "mango" de consultas de CocuhDB (notación JSON)
#  referencia de queries más complejos en:
#  https://docs.couchdb.org/en/stable/api/database/find.html
query = {"selector":{"rep_legal": "Diana L"}}
docs = db.find(query)
result = [] 
# docs es un objeto iterable:
for i in docs:
  print(dict(i)) #i es un documento de couchdb que puede convertirse a diccionario...
  result.append(dict(i)) #...y adicionarse a una lista

# (3) Update: Modificación de un documento previamente consultado:
doc_creado["fondos"] = 1000000.0
db.save(doc_creado)
print(doc_creado)

# (4) Delete:Borrado de un documento existente
doc_borrar = db["2"]
db.delete(doc_borrar)
