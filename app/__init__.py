from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Database.

db = SQLAlchemy() 

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Your_Secret_Key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    
    db.__init__(app)
    
    from .auth import auth
    from .views import views
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    

    
    with app.app_context():
        from app.models import Task
        db.create_all()
    
    return app