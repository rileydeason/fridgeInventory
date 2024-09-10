'''

Project one Fridge inventory system

'''

import sqlite3
'''
class Item:
    def __init__(self):
        self.__quantity = 0
        self.__name = ""
        self.__expiration = ""

    def add_item(self, quantity, name, expiration):
        self.__quantity = quantity
        self.__name = name
        self.__expiration = expiration

    def get_item(self):
        return self.__name
'''
class Database:
    def __init__(self):
        self.items = sqlite3.connect("items.db")
        self.cur = self.items.cursor()

        if not self.table_exists("fridge_contents"):
            self.cur.execute('''CREATE TABLE IF NOT EXISTS fridge_contents
                            (name TEXT PRIMARY KEY,
                            quantity INTEGER,
                            expiration TEXT)''')

        if not self.table_exists("volumes"):
            self.cur.execute('''CREATE TABLE IF NOT EXISTS volumes
                            (name TEXT PRIMARY KEY,
                            volume INTEGER)''')

        self.items.commit()

    def table_exists(self, table_name):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = self.cur.fetchone()
        return result is not None

    def insert_into_fridge_contents(self, name, quantity, expiration):
        self.cur.execute("INSERT OR REPLACE INTO fridge_contents (name, quantity, expiration) VALUES (?, ?, ?)", (name, quantity, expiration))
        self.items.commit()

    def update_fridge_contents(self, name, quantity, expiration):
        self.cur.execute("UPDATE fridge_contents SET quantity = ? WHERE name = ? AND expiration = ?",(quantity, name, expiration))
        self.items.commit()

    def delete_fridge_contents(self, name, expiration):
        self.cur.execute("DELETE FROM fridge_contents WHERE name = ? AND expiration = ?",(name, expiration))
        self.items.commit()

    def show_fridge_contents(self):
        self.cur.execute("SELECT * FROM fridge_contents")

        self.rows = self.cur.fetchall()

        print(f"{'NAME':<10}{'QUANTITY':<10}{'EXPIRATION':<10}")
        print("-" * 30)

        for row in self.rows:
            print(f"{row[0]:<10}{row[1]:<10}{row[2]:<10}")

    def insert_into_volumes(self, name, volume):
        self.cur.execute("INSERT OR REPLACE INTO volumes (name, volume) VALUES (?, ?)", (name, volume))
        self.items.commit()

    def update_volumes(self, name, volume):
        self.cur.execute("UPDATE fridge_contents SET volume = ? WHERE name = ? AND expiration = ?",(volume, name))
        self.items.commit()

    def delete_volumes(self, name, volume):
        self.cur.execute("DELETE FROM volumes WHERE name = ? AND volume = ?",(name, volume))
        self.items.commit()

    def show_volumes(self):
        self.cur.execute("SELECT * FROM volumes")

        self.rows = self.cur.fetchall()

        print(f"{'NAME':<10}{'VOLUME':<10}")
        print("-" * 20)

        for row in self.rows:
            print(f"{row[0]:<10}{row[1]:<10}")

def main():
    db = Database()

    db.insert_into_fridge_contents("Nathan", 2, "09/09/2024")
    db.insert_into_fridge_contents("Riley", 3, "09/09/2024")

    db.show_fridge_contents()

main()