# Technical Lesson: Building a Full CRUD REST API with Flask

## Overview

This project is the completed implementation of the technical lesson on building
a **Full CRUD REST API** with Flask. It demonstrates how to expose Create, Read,
Update, and Delete operations over HTTP using RESTful route conventions, JSON
request/response handling, and appropriate status codes — all backed by an
in-memory data store (no database required).

The API models a simple **event management** resource:

- `GET /events/<id>` — Retrieve a single event by ID
- `POST /events` — Create a new event
- `PATCH /events/<id>` — Update an existing event's title
- `DELETE /events/<id>` — Delete an event

## Learning Goals

- ✅ Understand how HTTP methods map to CRUD operations in REST.
- ✅ Build Flask routes that handle POST, GET, PATCH, and DELETE requests.
- ✅ Work with structured JSON input and output.
- ✅ Use in-memory Python objects to simulate persistent data.
- ✅ Follow RESTful conventions in route naming, structure, and response codes.

## Project Structure

```
.
├── app.py            # Flask application with all CRUD routes
├── Pipfile            # Project dependencies (Flask)
├── Pipfile.lock
└── README.md
```

## How It Works

The app defines a simple `Event` class and stores instances in an in-memory
list, standing in for a database:

```python
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
```

Each CRUD operation is implemented as its own route:

| Method | Route | Description | Success Status |
| --- | --- | --- | --- |
| `GET` | `/events/<int:id>` | Fetch a single event by ID | `200` |
| `POST` | `/events` | Create a new event | `201` |
| `PATCH` | `/events/<int:id>` | Update an event's title | `200` |
| `DELETE` | `/events/<int:id>` | Delete an event | `204` |

Requests for a non-existent event ID return `404 Event not found` on `GET`,
`PATCH`, and `DELETE`.

## Setup

Clone the repo and install dependencies.

**Using `pipenv`:**

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-technical-lesson
pipenv install
pipenv shell
```

**Using `pip`:**

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-technical-lesson
pip install flask
```

## Running the App

```bash
python app.py
```

The server starts at `http://127.0.0.1:5000` with debug mode enabled.

## Testing the Endpoints

Use `curl`, Postman, or your browser to try the following:

**Get an event**

```bash
curl http://127.0.0.1:5000/events/1
```

**Create an event**

```bash
curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title": "AI Conference"}'
```

**Update an event**

```bash
curl -X PATCH http://127.0.0.1:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Event Title"}'
```

**Delete an event**

```bash
curl -X DELETE http://127.0.0.1:5000/events/2
```

## Best Practices Demonstrated

- RESTful resource routing (`/events`, `/events/<id>`).
- JSON in, JSON out via `request.get_json()` and `jsonify()`.
- Correct status codes for each operation: `201` created, `200` OK, `204` no
  content on delete, `404` not found.
- No server-state mutation on `GET` requests.
- Consistent response shape via `Event.to_dict()`.

## Conclusion

This lesson takes a read-only API and extends it into a fully functional CRUD
backend. The patterns here — resource-based routing, JSON handling, and status
code conventions — carry directly into building APIs backed by a real database
and more advanced validation.