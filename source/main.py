
import tvar
import describe


config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "tvar",
    }
    # ,
    # "database_type" : "mysql",
    # "fingerprint_limit": 15
}
TVar= tvar(config)

""" Create a descriptors"""
# djv.fingerprint_directory("/Users/macbookpro/dejavu/mp3", [".mp3"], 3)
TVar.describe_directory("../advertisements", [".mp4"], 3)

"""Print the descriptors"""
#print(djv.db.get_num_fingerprints())
print(TVar.db.get_num_descriptors())

"""Recognizing from a file """
#song = djv.recognize(FileRecognizer,"/Users/macbookpro/dejavu/mp3/AMOUR_1.mp3")
#print(song)
ads = TVar.recognize("PATH OF THE FILE THAT SHOULD BE RECOGNIZED")
print(ads)