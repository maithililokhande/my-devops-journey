from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    redis_client.incr("visits")
    visits = redis_client.get("visits").decode("utf-8")
    return f"Welcome! Total visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
