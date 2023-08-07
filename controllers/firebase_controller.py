import firebase_admin
from firebase_admin import credentials, auth

from config import Config

class Firebase_Controller:
    def __init__(self):
        self.email = ''
        self.password = ''
        firebase_private_key = Config.firebase_private_key_file('knegg_firebase_p_key.json')
        cred = credentials.Certificate(firebase_private_key)
        firebase_admin.initialize_app(cred)    
    
    # Function to verify the ID token sent by the client
    @staticmethod
    def verify_id_token(self, id_token):
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
            return ({
                "status": 'Success',
                "message": "New Account Created. Please verify your email address",
                "uid": user.uid
            })
        except auth.EmailAlreadyExistsError:
            return ({
                "status": 'Errorr',
                "message": "User Email already exists. Try loggin in instead",
            })

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