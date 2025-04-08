import os
from flask import Flask, request, jsonify
from datetime import datetime, timezone
from database import create_room, insert_temperature, get_global_avg

app = Flask(__name__)  #to create a Flask app instance


@app.post("/api/room")
def create_room_endpoint():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    room_id = create_room(name)
    return {"id": room_id, "message": f"Room: {name} created successfully"}, 201

@app.post("/api/temperature")
def insert_temperature_endpoint():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room_id"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    insert_temperature(room_id, temperature, date)
    return {"message": "Temperature added."}, 201

@app.get("/api/average")
def get_global_avg_endpoint():
    average, days = get_global_avg()
    return {"average": round(average, 2), "days": days}

if __name__ == "__main__":
    app.run(debug=True)

