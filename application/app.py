from flask import Flask, jsonify, render_template
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "CloudOps Employee Service",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/info")
def info():
    return jsonify({
        "service": "CloudOps Employee Service",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "message": "Enterprise Cloud-Native DevOps Automation Platform"
    })


@app.route("/api/employees")
def employees():
    return jsonify({
        "employees": [
            {
                "id": 101,
                "name": "Ananya Sharma",
                "role": "DevOps Engineer",
                "department": "Cloud Engineering"
            },
            {
                "id": 102,
                "name": "Rahul Verma",
                "role": "Software Engineer",
                "department": "Application Development"
            },
            {
                "id": 103,
                "name": "Priya Nair",
                "role": "Cloud Engineer",
                "department": "Platform Engineering"
            }
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000"))
    )
