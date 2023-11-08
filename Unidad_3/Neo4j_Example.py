#FECHAS IMPORTANTES 3ER CORTE:
# ÚLTIMA CLASE: NOVIEMBRE 15
# SEGUNDA ENTREGA: NOVIEMBRE 14
# ULTIMA EVALUACIÓN/ENTREGA: NOVIEMBRE 22

from neo4j import GraphDatabase

#conectarse a la bd de grafo
url = "neo4j+s://0db30fd9.databases.neo4j.io"
#url1 = "0db30fd9.databases.neo4j.io:7687"
username ="neo4j"
pwd="Zo3oZFFmGXvZ3sHMqnNOUr7TG_3nya5kpnnZ0UAgXoQ"

#recomendar cursos a usuario de acuerdo a historial, calificaciones y cursos
#similares

#esta función devuelve los cursos que toma un usuario:
def recomendar(id_u):

    #retornar cursos que toma un usuario con id = id_usuario
    conn = GraphDatabase.driver(url, auth=(username,pwd))
    with conn.session() as session:
        #print(f"Session: {session._connection}")
        query = f"MATCH (a:Aprendiz)-[r:Asiste]->(c:Curso) WHERE a.Id = {id_u} RETURN a "
        result = session.run(query,id_u = id_u)
        cursos = [record["a"] for record in result]
        return cursos

if __name__ == "__main__":

    usr_id = input("Ingrese el id del usuario para el cual va a generar las recomendaciones: ")
    print(recomendar(usr_id) )
