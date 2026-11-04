from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            print("Connection established")

            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != '' ORDER BY genere"
            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                result.append(row[0])

            cursor.close()
            cnx.close()

        return result

    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            print("Connection established")


            query = """
                    SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca
                    FROM libro
                    WHERE (%s IS NULL OR id_biblioteca = %s)
                      AND (%s IS NULL OR genere = %s)
                    ORDER BY titolo
            """

            cursor = cnx.cursor(dictionary=True)

            # Passiamo 4 parametri poiché ogni condizione richiede (%s IS NULL OR colonna = %s)
            cursor.execute(query, (id_biblioteca, id_biblioteca, genere, genere))

            for row in cursor:
                # Se la classe Libro accetta un dizionario o i campi unpackati
                libro = Libro(
                    id=row['id'],
                    titolo=row['titolo'],
                    autore=row['autore'],
                    genere=row['genere'],
                    anno_pubblicazione=row['anno_pubblicazione'],
                    id_biblioteca=row.get('id_biblioteca')
                )
                result.append(libro)

            cursor.close()
            cnx.close()

        return result