import sqlite3

class Room():
    def __init__(self, floor, beds, guestNum, price):
        self.id = None
        self.floor = floor
        self.beds = beds
        self.guestNum = guestNum
        self.price = price


def add_room_to_db(room):
    with sqlite3.connect('hotel.db') as conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO rooms (floor, guestNum, price, beds) VALUES (?, ?, ?, ?)", (room.floor,
                                                                                              room.guestNum,
                                                                                              room.price,
                                                                                              room.beds))
def get_rooms_from_db(dateIn, dateOut, guestsCount):
    ...


def create_dbs() -> None:
    with sqlite3.connect('hotel.db') as conn:
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS rooms "
                    f"( "
                    f"  id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    f"  floor INTEGER, "
                    f"  guestNum INTEGER, "
                    f"  price INTEGER, "
                    f"  beds INTEGER "
                    f")")
        rooms = [(1, 12, 100500, 1), (2, 5, 100501, 23)]


def get_rooms():

    with sqlite3.connect('hotel.db') as conn:
        cur = conn.cursor()
        rooms = cur.execute(f"SELECT * FROM rooms ").fetchall()
        return rooms