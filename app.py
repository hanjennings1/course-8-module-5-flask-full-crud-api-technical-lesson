from flask import Flask, jsonify, request

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# Mock event data
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# READ: Get event by ID
@app.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    event = next((e for e in events if e.id == id), None)
    return jsonify(event.to_dict()) if event else ("Event not found", 404)

# CREATE: Add new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# UPDATE: Modify event title
@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())

# DELETE: Remove an event
@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    global events
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    events = [e for e in events if e.id != id]
    return ("Event deleted", 204)

if __name__ == "__main__":
    app.run(debug=True)