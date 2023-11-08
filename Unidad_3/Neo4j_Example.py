#FECHAS IMPORTANTES 3ER CORTE:
# ÚLTIMA CLASE: NOVIEMBRE 15
# SEGUNDA ENTREGA: NOVIEMBRE 14
# ULTIMA EVALUACIÓN/ENTREGA: NOVIEMBRE 22

from neo4j import GraphDatabase

#conectarse a la bd de grafo
url = "neo4j+s://0db30fd9.databases.neo4j.io"
username ="neo4j"
pwd="Zo3oZFFmGXvZ3sHMqnNOUr7TG_3nya5kpnnZ0UAgXoQ"



def connect():
    global conn
    conn = GraphDatabase.driver(url, auth=(username,pwd))


#recomendar cursos a usuario de acuerdo a historial, calificaciones y cursos
#similares

#esta función devuelve la información de un usuario:
def usuarios(id_u):

    conn = GraphDatabase.driver(url, auth=(username,pwd))
    #retornar cursos que toma un usuario con id = id_usuario    
    with conn.session() as session:
        #print(f"Session: {session._connection}")
        query = f"MATCH (a:Aprendiz) WHERE a.Id = {id_u} RETURN a "
        result = session.run(query,id_u = id_u)
        data = [record["a"] for record in result]
        return data

#esta función devuelve los cursos que toma un usuario:
def cursos(id_usuario):
    with conn.session as session:
        query = f""

#esta función devuelve los usuarios que toman un curso dado:
def usuarios_curso(id_curso):
    pass

#esta función devuelve los cursos calificados con nota > 4.0 por un usuario:
def cursos_calificados(id_usuario):
    pass

if __name__ == "__main__":

    usr_id = input("Ingrese el id del usuario para el cual va a generar las recomendaciones: ")
    print(usuarios(usr_id) )
