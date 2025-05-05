import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'inputs')
    OUTPUT_FOLDER = os.path.join(BASE_DIR, 'data', 'outputs')
    MODEL_PATH = 'yolov8n.pt'
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}