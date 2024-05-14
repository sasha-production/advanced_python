import json
from flask import Flask, request, Response, jsonify
from models import get_rooms_from_db, create_dbs, get_rooms, Room, add_room_to_db
from datetime import datetime

app = Flask(__name__)


@app.route('/add-room', methods=['POST'])
def add_room():
    if request.method == "POST":
        data = request.get_json()
        room = Room(
            floor=data["floor"],
            beds=data["beds"],
            guestNum=data["guestNum"],
            price=data["price"]
        )
        add_room_to_db(room)
        return Response('ok', status=201)

@app.route('/get-room', methods=['GET'])
def get_room():
    if request.method == 'GET':
        checkInDate, checkOutDate, guestsNum = request.args.get('checkIn'), request.args.get('checkOut'),\
            request.args.get('guestsNum')

        # rooms = get_rooms_from_db(checkInDate, checkOutDate, guestsNum)
        return get_rooms()
if __name__ == '__main__':
    create_dbs()
    app.run(host='127.0.0.1', port=5000, debug=True)
