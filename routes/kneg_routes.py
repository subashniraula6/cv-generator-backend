import os
import json
from flask import request, jsonify, Blueprint, send_from_directory
from controllers.kneg_ORM_controller import *

UPLOAD_FOLDER = 'public/user_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Configure
kneg_bp = Blueprint('kneg', __name__)

##############################
# Route to add a new user role
@kneg_bp.route('/kneg/user-role', methods=['POST'])
def add_user_role_route():
    # try:
        data = request.json
        role_name = data.get('role_name')
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if role_name and create_ts and update_ts:
            new_role = add_user_role(role_name, create_ts, update_ts)
            print(new_role)
            return jsonify({"message": "User role added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

# Route to get all user roles
@kneg_bp.route('/kneg/user-roles', methods=['GET'])
def get_all_user_roles_route():
    user_roles = get_all_user_roles()
    user_roles_data = [{"id": role.id, "role_name": role.role_name} for role in user_roles]
    return jsonify({"data": user_roles_data}), 200

# Route to get a user role by ID
@kneg_bp.route('/kneg/user-role/<int:role_id>', methods=['GET'])
def get_user_role_by_id_route(role_id):
    role = get_user_role_by_id(role_id)
    if role:
        role_data = {"id": role.id, "role_name": role.role_name}
        return jsonify({"data": role_data}), 200
    else:
        return jsonify({"error": "User role not found"}), 404

# Route to modify an existing user role
@kneg_bp.route('/kneg/user-role/<int:role_id>', methods=['PUT'])
def modify_user_role_route(role_id):
    try:
        data = request.json
        role_name = data.get('role_name')
        update_ts = data.get('update_ts')  # You can format this as needed

        role = modify_user_role(role_id, role_name, update_ts)
        if role:
            role_data = {"id": role.id, "role_name": role.role_name}
            return jsonify({"message": "User role modified successfully", "data": role_data}), 200
        else:
            return jsonify({"error": "User role not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a user role by ID
@kneg_bp.route('/kneg/user-role/<int:role_id>', methods=['DELETE'])
def delete_user_role_by_id_route(role_id):
    if delete_user_role_by_id(role_id):
        return jsonify({"message": "User role deleted successfully"}), 200
    else:
        return jsonify({"error": "User role not found"}), 404


##########################
# Route to add a new user
@kneg_bp.route('/kneg/user', methods=['POST'])
def add_user_route():
    try:
        data = request.json
        email = data.get('email')
        user_fname = data.get('user_fname')
        user_lname = data.get('user_lname')
        user_role_id = data.get('user_role_id')
        u_id = data.get('u_id')
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if email and user_fname and user_lname and user_role_id and u_id and create_ts and update_ts:
            new_user = add_user(email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts)
            return jsonify({"message": "User added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all users
@kneg_bp.route('/kneg/users', methods=['GET'])
def get_all_users_route():
    users = get_all_users()
    users_data = [{"id": user.id, "email": user.email} for user in users]
    return jsonify({"data": users_data}), 200

# Route to get a user by FIREBASE ID
@kneg_bp.route('/kneg/fbuser/<string:u_id>', methods=['GET'])
def get_user_by_firebase_id_route(u_id):
    user = get_users_by_u_id(u_id)
    if user:
        user_data = {
            "id": user.id,
            "email": user.email,
            "user_fname": user.user_fname,
            "user_lname": user.user_lname,
            "user_role": UserRole.query.get(user.user_role_id).role_name,
            "u_id": user.u_id,
            "create_ts": user.create_ts,
            "update_ts": user.update_ts
        }
        return jsonify({"data": user_data}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Route to get a user by ID
@kneg_bp.route('/kneg/user/<int:user_id>', methods=['GET'])
def get_user_by_id_route(user_id):
    user = get_user_by_id(user_id)
    if user:
        user_data = {
            "id": user.id,
            "email": user.email,
            "user_fname": user.user_fname,
            "user_lname": user.user_lname,
            "user_role_id": user.user_role_id,
            "u_id": user.u_id,
            "create_ts": user.create_ts,
            "update_ts": user.update_ts
        }
        return jsonify({"data": user_data}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Route to modify an existing user
@kneg_bp.route('/kneg/user/<int:user_id>', methods=['PUT'])
def modify_user_route(user_id):
    try:
        data = request.json
        email = data.get('email')
        user_fname = data.get('user_fname')
        user_lname = data.get('user_lname')
        user_role_id = data.get('user_role_id')
        u_id = data.get('u_id')
        update_ts = data.get('update_ts')  # You can format this as needed

        user = modify_user(user_id, email, user_fname, user_lname, user_role_id, u_id, update_ts)
        if user:
            user_data = {
                "id": user.id,
                "email": user.email,
                "user_fname": user.user_fname,
                "user_lname": user.user_lname,
                "user_role_id": user.user_role_id,
                "u_id": user.u_id,
                "create_ts": user.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                "update_ts": user.update_ts.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify({"message": "User modified successfully", "data": user_data}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a user by ID
@kneg_bp.route('/kneg/user/<int:user_id>', methods=['DELETE'])
def delete_user_by_id_route(user_id):
    if delete_user_by_id(user_id):
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404


##############################
# Route to add a new language
@kneg_bp.route('/kneg/language', methods=['POST'])
def add_language_route():
    try:
        data = request.json
        lang_abb = data.get('lang_abb')
        language_full = data.get('language_full')
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if lang_abb and language_full and create_ts and update_ts:
            new_language = add_language(lang_abb, language_full, create_ts, update_ts)
            return jsonify({"message": "Language added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all languages
@kneg_bp.route('/kneg/languages', methods=['GET'])
def get_all_languages_route():
    languages = get_all_languages()
    languages_data = [{"id": language.id, "lang_abb": language.lang_abb, "language_full": language.language_full}
                      for language in languages]
    return jsonify({"data": languages_data}), 200

# Route to get a language by ID
@kneg_bp.route('/kneg/language/<int:language_id>', methods=['GET'])
def get_language_by_id_route(language_id):
    language = get_language_by_id(language_id)
    if language:
        language_data = {
            "id": language.id,
            "lang_abb": language.lang_abb,
            "language_full": language.language_full,
            "create_ts": language.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
            "update_ts": language.update_ts.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify({"data": language_data}), 200
    else:
        return jsonify({"error": "Language not found"}), 404

# Route to modify an existing language
@kneg_bp.route('/kneg/language/<int:language_id>', methods=['PUT'])
def modify_language_route(language_id):
    try:
        data = request.json
        lang_abb = data.get('lang_abb')
        language_full = data.get('language_full')
        update_ts = data.get('update_ts')  # You can format this as needed

        language = modify_language(language_id, lang_abb, language_full, update_ts)
        if language:
            language_data = {
                "id": language.id,
                "lang_abb": language.lang_abb,
                "language_full": language.language_full,
                "create_ts": language.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                "update_ts": language.update_ts.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify({"message": "Language modified successfully", "data": language_data}), 200
        else:
            return jsonify({"error": "Language not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a language by ID
@kneg_bp.route('/kneg/language/<int:language_id>', methods=['DELETE'])
def delete_language_by_id_route(language_id):
    if delete_language_by_id(language_id):
        return jsonify({"message": "Language deleted successfully"}), 200
    else:
        return jsonify({"error": "Language not found"}), 404


#############################
# Route to add a new question
@kneg_bp.route('/kneg/question', methods=['POST'])
def add_question_route():
    try:
        data = request.json
        language_id = data.get('language_id')
        question_category = data.get('question_category')
        question_JSON = json.dumps(data.get('question_JSON'))
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if language_id and question_category and question_JSON and create_ts and update_ts:
            new_question = add_question(language_id, question_category, question_JSON, create_ts, update_ts)
            return jsonify({"message": "Question added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all questions
@kneg_bp.route('/kneg/questions', methods=['GET'])
def get_all_questions_route():
    questions = get_all_questions()
    questions_data = [{"id": question.id, "language_id": question.language_id, "question_category": question.question_category, "question_JSON": question.question_JSON}
                      for question in questions]
    return jsonify({"data": questions_data}), 200

# Route to get a question by ID
@kneg_bp.route('/kneg/question/<int:question_id>', methods=['GET'])
def get_question_by_id_route(question_id):
    question = get_question_by_id(question_id)
    if question:
        question_data = {
            "id": question.id,
            "language_id": question.language_id,
            "question_category": question.question_category,
            "question_JSON": question.question_JSON,
            "create_ts": question.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
            "update_ts": question.update_ts.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify({"data": question_data}), 200
    else:
        return jsonify({"error": "Question not found"}), 404


@kneg_bp.route('/kneg/questions_per_user/<string:user_id>', methods=['GET'])
def get_questions_by_user_id_route(user_id):
    user = User.query.filter_by(u_id=user_id).first()
    try:
        # Fetch questions by user_id
        questions = UserQuestion.query.filter_by(user_id=user.id).all()
        if questions:
            question_data = []
            for question in questions:
                language = Language.query.filter_by(id=question.language_id).first().lang_abb
                question_data.append({
                    "id": question.id,
                    "language": language,
                    "question_category": question.questions_category,
                    "question_JSON": question.question_JSON,
                    "create_ts": question.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                    "update_ts": question.update_ts.strftime('%Y-%m-%d %H:%M:%S')
                })
            return jsonify({"data": question_data}), 200
        else:
            return jsonify({"error": "No questions found for the user"}), 404
    except Exception as e:
        return jsonify({"error": e}), 500
# Route to modify an existing question
@kneg_bp.route('/kneg/question/<int:question_id>', methods=['PUT'])
def modify_question_route(question_id):
    try:
        data = request.json
        language_id = data.get('language_id')
        question_category = data.get('question_category')
        question_JSON = data.get('question_JSON')
        update_ts = data.get('update_ts')  # You can format this as needed

        question = modify_question(question_id, language_id, question_category, question_JSON, update_ts)
        if question:
            question_data = {
                "id": question.id,
                "language_id": question.language_id,
                "question_category": question.question_category,
                "question_JSON": question.question_JSON,
                "create_ts": question.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                "update_ts": question.update_ts.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify({"message": "Question modified successfully", "data": question_data}), 200
        else:
            return jsonify({"error": "Question not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to delete a question by ID
@kneg_bp.route('/kneg/question/<int:question_id>', methods=['DELETE'])
def delete_question_by_id_route(question_id):
    if delete_question_by_id(question_id):
        return jsonify({"message": "Question deleted successfully"}), 200
    else:
        return jsonify({"error": "Question not found"}), 404


##################################
# Route to add a new user question
@kneg_bp.route('/kneg/user_question', methods=['POST'])
def add_user_question_route():
    try:
        data = request.json
        user_id = data.get('user_id')
        language_id = data.get('language_id')
        questions_category = data.get('questions_category')
        question_JSON = json.dumps(data.get('question_JSON'))
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if user_id and language_id and questions_category and question_JSON and create_ts and update_ts:
            new_user_question = add_user_question(user_id, language_id, questions_category, question_JSON, create_ts, update_ts)
            return jsonify({"message": "User Question added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all user questions
@kneg_bp.route('/kneg/user_questions', methods=['GET'])
def get_all_user_questions_route():
    user_questions = get_all_user_questions()
    user_questions_data = [{"id": user_question.id, "user_sessions": user_question.user_sessions, "language_id": user_question.language_id,
                            "questions_category": user_question.questions_category}
                            for user_question in user_questions]
    return jsonify({"data": user_questions_data}), 200

# Route to get a user question by ID
@kneg_bp.route('/kneg/user_question/<int:user_question_id>', methods=['GET'])
def get_user_question_by_id_route(user_question_id):
    user_question = get_user_question_by_id(user_question_id)
    if user_question:
        user_question_data = {
            "id": user_question.id,
            "user_id": user_question.user_id,
            "language_id": user_question.language_id,
            "questions_category": user_question.questions_category,
            "question_JSON": user_question.question_JSON,
            "create_ts": user_question.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
            "update_ts": user_question.update_ts.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify({"data": user_question_data}), 200
    else:
        return jsonify({"error": "User Question not found"}), 404

# Route to modify an existing user question
@kneg_bp.route('/kneg/user_question/<int:user_question_id>', methods=['PUT'])
def modify_user_question_route(user_question_id):
    try:
        data = request.json
        question_JSON = json.dumps(data.get('question_JSON'))

        user_question = modify_user_question(user_question_id, question_JSON)
        if user_question:
            user_question_data = {
                "id": user_question.id,
                "user_id": user_question.user_id,
                "language_id": user_question.language_id,
                "questions_category": user_question.questions_category,
                "question_JSON": user_question.question_JSON,
                "create_ts": user_question.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                "update_ts": user_question.update_ts.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify({"message": "User Question modified successfully", "data": user_question_data}), 200
        else:
            return jsonify({"error": "User Question not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a user question by ID
@kneg_bp.route('/kneg/user-question/<int:user_question_id>', methods=['DELETE'])
def delete_user_question_by_id_route(user_question_id):
    if delete_user_question_by_id(user_question_id):
        return jsonify({"message": "User question deleted successfully"}), 200
    else:
        return jsonify({"error": "User question not found"}), 404


#####################################
# Route to add a new menu text
@kneg_bp.route('/kneg/menu_text', methods=['POST'])
def add_menu_text_route():
    try:
        data = request.json
        language_id = data.get('language_id')
        menu_text_JSON = data.get('menu_text_JSON')
        create_ts = data.get('create_ts')  # You can format this as needed
        update_ts = data.get('update_ts')  # You can format this as needed

        if language_id and menu_text_JSON and create_ts and update_ts:
            new_menu_text = add_menu_text(language_id, menu_text_JSON, create_ts, update_ts)
            return jsonify({"message": "Menu Text added successfully"}), 200
        else:
            return jsonify({"error": "Missing required data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all menu texts
@kneg_bp.route('/kneg/menu_texts', methods=['GET'])
def get_all_menu_texts_route():
    menu_texts = get_all_menu_texts()
    menu_texts_data = [{"id": menu_text.id, "language_id": menu_text.language_id, "menu_text_JSON": menu_text.menu_text_JSON}
                       for menu_text in menu_texts]
    return jsonify({"data": menu_texts_data}), 200


# Route to modify an existing menu text
@kneg_bp.route('/kneg/menu_text/<int:menu_text_id>', methods=['PUT'])
def modify_menu_text_route(menu_text_id):
    try:
        data = request.json
        language_id = data.get('language_id')
        menu_text_JSON = data.get('menu_text_JSON')
        update_ts = data.get('update_ts')  # You can format this as needed

        menu_text = modify_menu_text(menu_text_id, language_id, menu_text_JSON, update_ts)
        if menu_text:
            menu_text_data = {
                "id": menu_text.id,
                "language_id": menu_text.language_id,
                "menu_text_JSON": menu_text.menu_text_JSON,
                "create_ts": menu_text.create_ts.strftime('%Y-%m-%d %H:%M:%S'),
                "update_ts": menu_text.update_ts.strftime('%Y-%m-%d %H:%M:%S')
            }
            return jsonify({"message": "Menu Text modified successfully", "data": menu_text_data}), 200
        else:
            return jsonify({"error": "Menu Text not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a menu text by ID
@kneg_bp.route('/kneg/menu-text/<int:menu_text_id>', methods=['DELETE'])
def delete_menu_text_by_id_route(menu_text_id):
    if delete_menu_text_by_id(menu_text_id):
        return jsonify({"message": "Menu text deleted successfully"}), 200
    else:
        return jsonify({"error": "Menu text not found"}), 404
    

# Route For image upload and retrieve
# Endpoint to upload an image
@kneg_bp.route('/kneg/upload_image', methods=['POST'])
def upload_image():
    try:
        data = request.json
        user_id = data.user_id
        if user_id == None:
            return jsonify({"error": "User Id not found"})
        # Check if the 'file' key is in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']

        # Check if the file has an allowed extension
        if file and allowed_file(file.filename):
            # Save the file to the upload folder
            extension = os.path.splitext(file.filename)[1]
            image_file_name = f'user_image_{user_id}.{extension}'
            file.save(os.path.join(UPLOAD_FOLDER, image_file_name))
            return jsonify({"message": "File uploaded successfully"}), 200
        else:
            return jsonify({"error": "Invalid file or file type"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve an image by filename
@kneg_bp.route('/kneg/images/<string:filename>', methods=['GET'])
def get_image(filename):
    try:
        # Ensure the requested file exists in the upload folder
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, filename)):
            return send_from_directory(UPLOAD_FOLDER, filename)
        else:
            return jsonify({"error": "Image not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# User input filtering
# Route to filter data based on user, title, question, and answer
@kneg_bp.route('/kneg/filter_data', methods=['GET'])
def filter_data_route():
    try:
        # Get parameters from the request query string
        user_id = request.args.get('user_id', type=int)
        title = request.args.get('title')
        question = request.args.get('question')
        answer = request.args.get('answer')

        # Query UserQuestion records based on user_id
        user_questions = UserQuestion.query.filter_by(user_id=user_id).all()

        # Initialize an empty list to store filtered results
        filtered_results = []

        # Loop through the user questions and apply filtering
        for user_question in user_questions:
            # Parse the question_JSON string to extract data
            data = json.loads(user_question.question_JSON)

            # Call the filter_data function to filter the data
            result = filter_data(data, user_id, title, question, answer)

            # If there is filtered data, add it to the filtered results list
            if result["filtered_data"]:
                filtered_results.append(result)

        # Check if there is any filtered data or not
        if filtered_results:
            return jsonify(filtered_results), 200
        else:
            return jsonify({"message": "No matching data found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500