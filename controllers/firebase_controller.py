import firebase_admin
from firebase_admin import credentials, auth
from flask import jsonify
from models.kneg_models import db, User

from config import Config
from controllers.kneg_ORM_controller import pupulate_user_questions


class Firebase_Controller:
    def __init__(self):
        self.email = ''
        self.password = ''
        firebase_private_key = Config.firebase_private_key_file('knegg_firebase_p_key.json')
        cred = credentials.Certificate(firebase_private_key)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)    
    
    # Function to verify the ID token sent by the client
    @staticmethod
    def verify_id_token( id_token):
        try:
            decoded_token = auth.verify_id_token(id_token)
            return {
                "status": "Success",
                "message": "ID Token Verified",
                "user_id": decoded_token['uid']
            }
        except auth.InvalidIdTokenError:
            return {
                "status": "Error",
                "message": "Invalid ID Token"
            }
        
    # Function to create a new user
   
    @staticmethod
    def create_user(email, password):
        try:
            user = auth.create_user(email=email, password=password)
            print(auth.generate_email_verification_link(email))

            # Create a new user in your database with the provided email
            new_user = User(email=email, user_fname=None, user_lname=None, user_role_id=None, u_id=user.uid, create_ts=None, update_ts=None)
            db.session.add(new_user)
            db.session.commit()

            # populate user question from application question
            user_questions = pupulate_user_questions(new_user.id)
            db.session.add_all(user_questions)
            db.session.commit()

            return {
                "status": 'Success',
                "message": "New Account Created. Please verify your email address",
                "uid": user.uid
            }
        except auth.EmailAlreadyExistsError:
            return {
                "status": 'Error',
                "message": "User Email already exists. Try logging in instead",
            }
    
    # Function to log in a user
    @staticmethod
    def login_user(email, password):
        try:
            user = auth.get_user_by_email(email)
            auth.get_user(user.uid)  # Verifies the user exists and their email is verified
            user = auth.sign_in_with_email_and_password(email, password)
            return {
                "status": 'Success',
                "message": "User Logged In Successfully",
                "uid": user['localId'],
                "id_token": user['idToken']
            }
        except auth.UserNotFoundError:
            return {
                "status": 'Error',
                "message": "User not found. Please check your credentials or sign up"
            }
        except auth.WrongPasswordError:
            return {
                "status": 'Error',
                "message": "Invalid password. Please check your credentials"
            }
        except auth.EmailNotVerifiedError:
            return {
                "status": 'Error',
                "message": "Email not verified. Please verify your email address"
            }
        
    # Delete User
    @staticmethod
    def delete_user(u_id, token):
        token_verification = Firebase_Controller.verify_id_token(token)
        print(f'here is u_id {u_id}')
        if token_verification['status'] == 'Error':
            return False

        try:
            auth.delete_user(u_id)
            # Get data form u_id
            user = User.query.filter_by(u_id=u_id).all()
            # Get user_id from the user
            user_id = user['data']['id']
            db.session.delete(user_id)
            db.session.commit()
            return True
        except auth.AuthError as e:
            return False
