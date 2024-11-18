from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r"/*": {
            "origins": "http://localhost:5173",  # URL frontend Anda
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        # Import models
        from app.models.user import User
        from app.models.fasilitas import Fasilitas
        from app.models.peminjaman import Peminjaman
        from app.models.disposisi import Disposisi
        
        # Import blueprints
        from app.routes.auth import auth_bp
        from app.routes.fasilitas import fasilitas_bp
        from app.routes.peminjaman import peminjaman_bp
        from app.routes.disposisi import disposisi_bp
        
        # Register blueprints
        app.register_blueprint(auth_bp)
        app.register_blueprint(fasilitas_bp)
        app.register_blueprint(peminjaman_bp)
        app.register_blueprint(disposisi_bp)
        
        # Create tables
        db.create_all()
        
    return app 