# db_controller.py
from models.user_model import db, User

def add_user_to_db(username, email):
    try:
        # Create a new User object
        new_user = User(username=username, email=email)

        # Add the new_user object to the session
        db.session.add(new_user)

        # Commit the session to persist the data to the database
        db.session.commit()

        return True, "User data inserted successfully"
    except Exception as e:
        return False, str(e)
