from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), default="")
    status = db.Column(db.String(20), default="Pending", nullable=False)
    priority = db.Column(db.String(20), default="Medium", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description or "",
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at.isoformat() + "Z"
        }

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/tasks")
def get_tasks():
    status = request.args.get("status")
    query = Task.query
    if status and status != "All":
        query = query.filter_by(status=status)
    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks])

@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "Task title is required."}), 400
    priority = data.get("priority", "Medium")
    if priority not in ["Low", "Medium", "High"]:
        return jsonify({"error": "Priority must be Low, Medium, or High."}), 400
    task = Task(
        title=title,
        description=(data.get("description") or "").strip(),
        priority=priority,
        status="Pending"
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found."}), 404
    data = request.get_json(silent=True) or {}
    if "title" in data:
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify({"error": "Task title cannot be empty."}), 400
        task.title = title
    if "description" in data:
        task.description = (data.get("description") or "").strip()
    if "status" in data:
        if data["status"] not in ["Pending", "In Progress", "Completed"]:
            return jsonify({"error": "Invalid task status."}), 400
        task.status = data["status"]
    if "priority" in data:
        if data["priority"] not in ["Low", "Medium", "High"]:
            return jsonify({"error": "Invalid task priority."}), 400
        task.priority = data["priority"]
    db.session.commit()
    return jsonify(task.to_dict())

@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found."}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully."})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
