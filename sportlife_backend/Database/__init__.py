import sqlite3



class Database:

    def __init__(self, db_path):
        self.db_path = db_path
        self.sub_types = {
            1: "1 месяц",
            3: "3 месяца",
            6: "6 месяцев",
            12: "1 год"
        }

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

    def addClient(self, name, phone, street, subscription_type, subscription_seller, birthday):
        with sqlite3.connect(self.db_path) as conn:
            conn.cursor().execute("INSERT INTO clients VALUES (?,?,?,?,?,?,?)", (name, phone, street, subscription_type, subscription_seller, 1, birthday))


    def getAllClients(self):
        with sqlite3.connect(self.db_path) as conn:
            return conn.cursor().execute("SELECT * FROM clients").fetchall()

    def sortByName(self, name):
        lst = []
        with sqlite3.connect(self.db_path) as conn:
            ex = conn.cursor().execute("SELECT * FROM clients").fetchall()
            for name_, phone, street, subscription_type, subscription_seller, page, birthday in ex:
                if name in name_:

                    lst.append({
                        "fio": name_,
                        "phone": phone,
                        "street": street,
                        "sub_type": self.sub_types[subscription_type],
                        "subscription_seller": subscription_seller,
                        "birthday": birthday
                    })
            return lst