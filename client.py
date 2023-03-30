from flask import Flask, render_template, request, Response
import redis
# import cv2

app = Flask(__name__)

# Login page with interactive buttons
@app.route('/', methods=['GET', 'POST'])
def index():
    r=redis.Redis(decode_responses=True)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        r.set(username,password)
        # do something with the username and password
        return render_template('camera.html')
    return render_template('index.html')

# # Camera page with image taker
@app.route('/camera', methods=['GET', 'POST'])
def camera():
    if request.method == 'POST':
        # Get the image from the camera
        ret, frame = cap.read()
        cap.release()
        # Convert the image to PNG format and store it in memory
        _, img_encoded = cv2.imencode('.png', frame)
        response = Response(img_encoded.tobytes(), mimetype='image/png')
        # Render the image on the page
        return render_template('camera.html', image_data=response)
    return render_template('camera.html')
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            return "Username already taken"
        else:
            users[username] = password
            return redirect(url_for("login"))
    else:
        return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)