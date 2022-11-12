from sqlite3 import connect, Error

class Connect():
    def get_connect(self, db_file):
        conn = None
        try:
            conn = connect(db_file)
            return conn
        except Error as err:
            print(err)
        
        return conn