# Picamera2-Flask-Gallery
A Flask application that takes pictures and displays a chosen picture on the page. This is used to test the Pi Camera modules.

## Getting started

This project works on Raspberry Pi OS Bullseye and Bookworm. In Bookworm be sure to use a virtual environment first. The `flask` and `Picamera2` libraries should be installed. If not, be sure to install them first. Run the main code with `python3 app.py`. Go to `localhost:5000` and then take the picture with your camera. Be sure you created an `images` directory under the `static` directory. You can also use your phone and tablet to take a picture. However, you will only be able to access the images through the Pi so it's best to access the app from your Pi. This should work with any Raspberry Pi and any Camera Module should work including third party modules.
