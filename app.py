import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    visits = cache.incr("visits")
    return f"<h1>Hello from my containerised app</h1><p>This page has been visited {visits} times.</p>"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
