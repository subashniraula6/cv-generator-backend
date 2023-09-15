# db_controller.py
from models.kneg_models import db, UserRole, User, Language, Question, UserQuestion, MenuText
import json

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

# Function to modify user's role
def modify_user_roles(user_id, role_id):
    user = User.query.get(user_id)
    if user:
        user.user_role_id = role_id
        db.session.commit()
        return user  # Return the modified role object
    else:
        return None  # Role with the given ID not found



############################
# Function to add a new user
def add_user(email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts):
    new_user = User(email=email, user_fname=user_fname, user_lname=user_lname,
                    user_role_id=user_role_id, u_id=u_id, create_ts=create_ts, update_ts=update_ts)
    db.session.add(new_user)
    db.session.commit()
    return new_user  # Return the newly added user object

# Function to get all users
def get_all_users():
    return User.query.all()

# Function to get a user by ID
def get_user_by_id(user_id):
    return User.query.get(user_id)

# Function to get users by u_id
def get_users_by_u_id(u_id):
    return User.query.filter_by(u_id=u_id).first()

# Function to modify an existing user
def modify_user(user_id, email, user_fname, user_lname, user_role_id, u_id, update_ts):
    user = User.query.get(user_id)
    if user:
        user.email = email
        user.user_fname = user_fname
        user.user_lname = user_lname
        user.user_role_id = user_role_id
        user.u_id = u_id
        user.update_ts = update_ts
        db.session.commit()
        return user  # Return the modified user object
    else:
        return None  # User with the given ID not found

# Function to replace specific keys with empty strings
def replace_keys_with_empty_strings(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ["question", "title", "options", "hint"]:
                data[key] = ""
            elif isinstance(value, (dict, list)):
                replace_keys_with_empty_strings(value)
    elif isinstance(data, list):
        for item in data:
            replace_keys_with_empty_strings(item)

################################
# Function to add a new language
def add_language(lang_abb, language_full, create_ts, update_ts):
    new_language = Language(lang_abb=lang_abb, language_full=language_full,
                            create_ts=create_ts, update_ts=update_ts)
    db.session.add(new_language)
    db.session.commit()

    # Add application question for this language with empty values from existing english language question json
    english_json = Question.query.get(1).question_JSON
    
    # Convert to dictionary
    new_json = json.loads(english_json)

    # Apply the function to your existing JSON
    replace_keys_with_empty_strings(new_json)

    # Set language
    new_json['lang'] = lang_abb

    # Convert the new JSON to a string
    new_json_str = json.dumps(new_json, indent=2, ensure_ascii=False)

    # Print the modified JSON
    print(new_json_str)
    
    # save to application question
    new_question = Question(language_id=new_language.id, question_category="",
                            question_JSON=new_json_str, create_ts=create_ts, update_ts=update_ts)
    db.session.add(new_question)
    db.session.commit()
    return new_language  # Return the newly added language object

# Function to get all languages
def get_all_languages():
    return Language.query.all()

# Function to get a language by ID
def get_language_by_id(language_id):
    return Language.query.get(language_id)

# Function to modify an existing language
def modify_language(language_id, lang_abb, language_full, update_ts):
    language = Language.query.get(language_id)
    if language:
        language.lang_abb = lang_abb
        language.language_full = language_full
        language.update_ts = update_ts
        db.session.commit()
        return language  # Return the modified language object
    else:
        return None  # Language with the given ID not found
    

###############################
# Function to add a new question
def add_question(language_id, question_category, question_JSON, create_ts, update_ts):
    existing_question = Question.query.filter_by(language_id=language_id).first()
    if existing_question:
        existing_question.question_category = question_category
        existing_question.question_JSON = question_JSON
        db.session.commit()
        return existing_question
    else:
        new_question = Question(language_id=language_id, question_category=question_category,
                                question_JSON=question_JSON, create_ts=create_ts, update_ts=update_ts)
        db.session.add(new_question)
        db.session.commit()
        return new_question  # Return the newly added question object

# Function to get all questions
def get_all_questions():
    return Question.query.all()

# Function to get a question by ID
def get_question_by_id(question_id):
    return Question.query.get(question_id)

# Function to modify an existing question
def modify_question(question_id, question_JSON):
    question = Question.query.get(question_id)
    if question:
        question.question_JSON = question_JSON
        db.session.commit()
        return question  # Return the modified question object
    else:
        return None  # Question with the given ID not found
    

# Function to populate user questions with application questions
def pupulate_user_questions(user_id):
    app_questions = Question.query.all()
    user_questions = map(lambda question: UserQuestion(
        user_id=user_id,
        language_id=question.language_id,
        questions_category=question.question_category,
        question_JSON=question.question_JSON,
        create_ts=question.create_ts,
        update_ts=question.update_ts
    ), app_questions)
    return user_questions

####################################
# Function to add a new user question
def add_user_question(user_id, language_id, questions_category, question_JSON, create_ts, update_ts):
    try:
        new_user_question = UserQuestion(
            user_id=user_id,
            language_id=language_id,
            questions_category=questions_category,
            question_JSON=question_JSON,
            create_ts=create_ts,
            update_ts=update_ts
        )
        db.session.add(new_user_question)
        db.session.commit()
        return new_user_question  # Return the newly added user question object
    except Exception as e:
        print(e)
        
# Function to get all user questions
def get_all_user_questions():
    return UserQuestion.query.all()

# Function to get a user question by ID
def get_user_question_by_id(user_question_id):
    return UserQuestion.query.get(user_question_id)

# Function to modify an existing user question
def modify_user_question(user_question_id, question_JSON):
    user_question = UserQuestion.query.get(user_question_id)
    if user_question:
        user_question.question_JSON = question_JSON
        db.session.commit()
        return user_question  # Return the modified user question object
    else:
        return None  # User question with the given ID not found
    

#################################
# Function to add a new menu text
def add_menu_text(language_id, menu_text_JSON, create_ts, update_ts):
    new_menu_text = MenuText(
        language_id=language_id,
        menu_text_JSON=menu_text_JSON,
        create_ts=create_ts,
        update_ts=update_ts
    )
    db.session.add(new_menu_text)
    db.session.commit()
    return new_menu_text  # Return the newly added menu text object

# Function to get all menu texts
def get_all_menu_texts():
    return MenuText.query.all()

# Function to get a menu text by ID
def get_menu_text_by_id(menu_text_id):
    return MenuText.query.get(menu_text_id)

# Function to modify an existing menu text
def modify_menu_text(menu_text_id, language_id, menu_text_JSON, update_ts):
    menu_text = MenuText.query.get(menu_text_id)
    if menu_text:
        menu_text.language_id = language_id
        menu_text.menu_text_JSON = menu_text_JSON
        menu_text.update_ts = update_ts
        db.session.commit()
        return menu_text  # Return the modified menu text object
    else:
        return None  # Menu text with the given ID not found
    
##############################
# DELETE FUNCTIONS

# Function to delete a user role by ID
def delete_user_role_by_id(role_id):
    role = UserRole.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # Role with the given ID not found

# Function to delete a user by ID
def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # User with the given ID not found

# Function to delete a language by ID
def delete_language_by_id(language_id):
    language = Language.query.get(language_id)
    if language:
        db.session.delete(language)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # Language with the given ID not found

# Function to delete a question by ID
def delete_question_by_id(question_id):
    question = Question.query.get(question_id)
    if question:
        db.session.delete(question)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # Question with the given ID not found

# Function to delete a user question by ID
def delete_user_question_by_id(user_question_id):
    user_question = UserQuestion.query.get(user_question_id)
    if user_question:
        db.session.delete(user_question)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # User question with the given ID not found

# Function to delete a menu text by ID
def delete_menu_text_by_id(menu_text_id):
    menu_text = MenuText.query.get(menu_text_id)
    if menu_text:
        db.session.delete(menu_text)
        db.session.commit()
        return True  # Successfully deleted
    else:
        return False  # Menu text with the given ID not found
    

def filter_data(data, user_id, title=None, question=None, answer=None):
    filtered_data = {}

    for category, category_data in data.items():
        filtered_category = {"title": category_data["title"], "questions": []}
        for q in category_data["questions"]:
            if (
                (title is None or title.lower() in category_data["title"].lower())
                and (question is None or question.lower() in q["question"].lower())
                and (answer is None or answer.lower() in q["answer"].lower())
            ):
                filtered_category["questions"].append(q)

        if filtered_category["questions"]:
            filtered_data[category] = filtered_category

    user = User.query.get(user_id)
    user_email = user.email if user else None
    
    return {"user_id": user_id, "user_email": user_email, "filtered_data": filtered_data}
