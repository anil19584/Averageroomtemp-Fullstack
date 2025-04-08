# Averageroomtemp-Fullstack

## Endpoints

### POST /api/room
This endpoint will let clients send us the room name, and we will create a room in the database against which we can store temperatures.

### POST /api/temperature
This endpoint will let clients send us the room and the temperature, and we'll store it in the database after doing some formatting.

### GET /api/room/<int:room_id>
This endpoint will let clients send us a room identifier, and we'll return the average temperature for a room since the room was created. Alternatively, clients will be able to specify a term (in days) and we'll respond appropriately.

### GET /api/average
This endpoint will let clients request the average temperature across all rooms, since we started gathering data.

## Running the Application
To run the application, use: Flask Run
