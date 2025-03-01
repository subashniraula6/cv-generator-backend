from app import app
from models.kneg_models import db

with app.app_context():
    db.create_all()
    print("Database schema created successfully!")

