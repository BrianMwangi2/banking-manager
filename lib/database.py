import sqlite3

class BankDatabase:
    def __init__(self, db_name='bank.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                                 (id TEXT PRIMARY KEY, name TEXT, balance REAL)''')

    def load_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = {}
        for row in cursor.fetchall():
            users[row[0]] = {'id': row[0], 'name': row[1], 'balance': row[2]}
        return users

    def update_balance(self, user_id, balance):
        with self.conn:
            self.conn.execute("UPDATE users SET balance = ? WHERE id = ?", (balance, user_id))

    def create_user(self, user_id, name):
        with self.conn:
            self.conn.execute("INSERT INTO users (id, name, balance) VALUES (?, ?, 0)", (user_id, name))

    def get_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'name': row[1], 'balance': row[2]}
        return None

    def delete_user(self, user_id):
        with self.conn:
            self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
