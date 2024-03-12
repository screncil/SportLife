import sqlite3



class Database:

    def __init__(self, db_path):
        self.db_path = db_path

    def userExists(self, username: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            return bool(conn.cursor().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall())

    def checkPassword(self, username, password) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            if self.userExists(username):
                ex = conn.cursor().execute("SELECT password FROM users WHERE username = ?", (username,)).fetchall()
                if ex[0][0] == password:
                    return True
                return False

    def getCookie(self, username):
        with sqlite3.connect(self.db_path) as conn:
            return conn.cursor().execute("SELECT user_hash FROM users WHERE username = ?", (username,)).fetchone()[0]

    def getUserByHash(self, hash):
        with sqlite3.connect(self.db_path) as conn:
            return conn.cursor().execute("SELECT * FROM users WHERE user_hash = ?", (hash,)).fetchall()
