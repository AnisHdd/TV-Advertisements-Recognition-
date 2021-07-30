""" """
from database_sql import database


class tvar(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")

        """ add a new ads in channels"""

    def insert_advertisements(self,name,path,ff_descriptor,lf_descriptor,duration):
        self.db.mycursor.execute("INSERT INTO advertisements (name,path,ff_descriptor,lf_descriptor,duration) VALUES (%s, %s, %s, %s, %s)"
                                 ,(name,path,ff_descriptor,lf_descriptor,duration))
        self.db.commit()
        print(self.db.mycursor.rowcount, "record inserted.")



     def describe(self):
        """ entree: path vers le videos --- > remplir la base de donnee advertisements """
        self.db.mycursor.execute("SHOW TABLES")
        for x in self.db.mycursor:
            print(x)
        pass

    def recognize(self):
        """entree video --- > chercher dans la bdd avdertisement la publicite et remplir la table apparitions """
        pass







#
# detecteur = tvar()
# detecteur.db.mycursor.execute("SHOW TABLES")
# for x in detecteur.db.mycursor:
#     print(x)
