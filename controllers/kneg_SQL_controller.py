# db_controller.py
from models.kneg_models import db, UserRole

# Function to add a new user role
def add_user_role(role_name, create_ts, update_ts):
    new_role = UserRole(role_name=role_name, create_ts=create_ts, update_ts=update_ts)
    db.session.add(new_role)
    db.session.commit()
    return new_role  # Return the newly added role object

# Function to get all user roles
def get_all_user_roles():
    return UserRole.query.all()

# Function to get a user role by ID
def get_user_role_by_id(role_id):
    return UserRole.query.get(role_id)

# Function to modify an existing user role
def modify_user_role(role_id, role_name, update_ts):
    role = UserRole.query.get(role_id)
    if role:
        role.role_name = role_name
        role.update_ts = update_ts
        db.session.commit()
        return role  # Return the modified role object
    else:
        return None  # Role with the given ID not found
