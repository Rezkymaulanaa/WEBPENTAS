from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r"/*": {
            "origins": "http://localhost:5173",  # URL frontend Anda
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
            "expose_headers": ["Content-Disposition"]
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
        
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        
    @app.route('/uploads/fasilitas/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
        
    return app 