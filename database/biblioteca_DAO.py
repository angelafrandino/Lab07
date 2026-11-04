from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            print("Connection established")

            query = "SELECT id, nome, indirizzo FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()

        return result
