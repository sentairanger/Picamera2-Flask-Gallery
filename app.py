# import libraries
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from picamera2 import Picamera2
from time import sleep
from datetime import datetime
import os

# define the Pi Camera and timestamp
picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
timestamp = datetime.now().isoformat()

# define the app
app = Flask(__name__)

# define the upload folder for our images
upload_folder = 'static/images'
app.config['UPLOAD'] = upload_folder

# define the function to capture images
def capture():
    image = "flask_%s.jpg" % timestamp
    image_path = os.path.join(upload_folder, image)
    picam2.start()
    sleep(3)
    picam2.capture_file(image_path)
    picam2.stop()

# define the function to upload images from our directory and then render the image to our page
@app.route("/", methods = ['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template('index.html')

# Define the function that will capture our images and upload to our directory
@app.route("/capture", methods=["POST"])
def take_picture():
    capture()
    return render_template('index.html')

# Run the app 
if __name__ == "__main__":
    app.run(host="0.0.0.0")