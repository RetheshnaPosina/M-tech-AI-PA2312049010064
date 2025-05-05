from flask import Blueprint, render_template, Response
import cv2
from . import create_app

main_bp = Blueprint('main', __name__)
app = create_app()

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/video_feed')
def video_feed():
    def generate():
        # Implement your video feed logic here
        pass
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')