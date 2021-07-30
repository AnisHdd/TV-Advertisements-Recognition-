""" """


class tvar():
    def __init__(self, config):
        self.config = config

       # initialize db
        db_cls = get_database(config.get("database_type", 'None'))

        self.db = db_cls(**config.get("database", {}))
        self.db.setup()