from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
MONGO_URI = 'mongodb://localhost:27017/'
client = MongoClient(MONGO_URI)
db = client.celebratemate
reminders_collection = db.reminders

# Route to serve index.html from the static directory
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Route to handle POST requests for adding reminders
@app.route('/api/reminders', methods=['POST'])
def add_reminder():
    data = request.get_json()
    result = reminders_collection.insert_one(data)
    return jsonify({"message": "Reminder added successfully", "id": str(result.inserted_id)})

# Route to handle GET requests for retrieving reminders
@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    reminders = reminders_collection.find()
    reminders_list = list(reminders)
    for reminder in reminders_list:
        reminder['_id'] = str(reminder['_id'])  # Convert ObjectId to string
    return jsonify(reminders_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

