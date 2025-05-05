from flask import Flask
from .config import Config  # Changed to relative import

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize components
    from .models.object_tracker import ObjectTracker
    app.tracker = ObjectTracker()
    
    # Register blueprints
    from .main import main_bp
    app.register_blueprint(main_bp)
    
    return app