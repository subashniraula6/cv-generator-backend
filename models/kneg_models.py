from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the UserRole model
class UserRole(db.Model):
    __tablename__ = 'application_user_roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)

# Define the User model
class User(db.Model):
    __tablename__ = 'application_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_lname = db.Column(db.String(255))
    user_role_id = db.Column(db.Integer, db.ForeignKey('application_user_roles.id'))
    u_id = db.Column(db.String(255))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)
    user_role = db.relationship('UserRole', foreign_keys=[user_role_id])

# Define the Language model
class Language(db.Model):
    __tablename__ = 'application_languages'

    id = db.Column(db.Integer, primary_key=True)
    lang_abb = db.Column(db.String(3))
    language_full = db.Column(db.String(15))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)

# Define the Question model
class Question(db.Model):
    __tablename__ = 'application_questions'

    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('application_languages.id'))
    question_category = db.Column(db.String(255))
    question_JSON = db.Column(db.String(10000))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)
    language = db.relationship('Language', foreign_keys=[language_id])

# Define the UserSession model
# class UserSession(db.Model):
#     __tablename__ = 'user_sessions'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('application_users.id'))
#     create_ts = db.Column(db.DateTime)
#     update_ts = db.Column(db.DateTime)
#     user = db.relationship('User', foreign_keys=[user_id])

# Define the UserQuestion model
class UserQuestion(db.Model):
    __tablename__ = 'user_questions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('application_users.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('application_languages.id'))
    questions_category = db.Column(db.String(20))
    question_JSON = db.Column(db.String(10000))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)
    user = db.relationship('User', foreign_keys=[user_id])
    language = db.relationship('Language', foreign_keys=[language_id])

# Define the MenuText model
class MenuText(db.Model):
    __tablename__ = 'application_menu_text'

    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('application_languages.id'))
    menu_text_JSON = db.Column(db.String(10000))
    create_ts = db.Column(db.DateTime)
    update_ts = db.Column(db.DateTime)
    language = db.relationship('Language', foreign_keys=[language_id])
