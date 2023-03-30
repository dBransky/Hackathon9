from flask import Flask
import redis

r = redis.Redis(decode_responses=True)
r.set('key','test_val')
app = Flask(__name__)

@app.route("/")
def main():
    return f"<p>{r.get('key')}</p>"