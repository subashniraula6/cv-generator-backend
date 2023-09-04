from mysql.connector import Error


def insert_application_user_roles(connection, role_name, create_ts, update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO application_user_roles (role_name, create_ts, update_ts)
    VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(query, (role_name, create_ts, update_ts))
        connection.commit()
        print("application_user_roles record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_application_users(connection, email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO application_users (email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts))
        connection.commit()
        print("application_users record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_application_languages(connection, lang_abb, language_full, create_ts, update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO application_languages (lang_abb, language_full, create_ts, update_ts)
    VALUES (%s,%s,%s,%s)
    """
    try:
        cursor.execute(query,(lang_abb ,language_full ,create_ts ,update_ts))
        connection.commit()
        print("application_languages record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_application_questions(connection ,language_id ,question_category ,question_JSON ,create_ts ,update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO application_questions (language_id ,question_category ,question_JSON ,create_ts ,update_ts)
    VALUES (%s,%s,%s,%s,%s)
    """
    try:
        cursor.execute(query,(language_id ,question_category ,question_JSON ,create_ts ,update_ts))
        connection.commit()
        print("application_questions record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_user_sessions(connection,user_id ,create_ts ,update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO user_sessions (user_id ,create_ts ,update_ts)
    VALUES (%s,%s,%s)
    """
    try:
        cursor.execute(query,(user_id ,create_ts ,update_ts))
        connection.commit()
        print("user_sessions record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_user_questions(connection,user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts):
    cursor = connection.cursor()
    query = """
    INSERT INTO user_questions (user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    try:
        cursor.execute(query,(user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts))
        connection.commit()
        print("user_questions record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_application_menu_text(connection,id_, language_id_, menu_text_JSON_, create_ts_, update_ts_):
    cursor = connection.cursor()
    query = """
    INSERT INTO application_menu_text(id_, language_id_, menu_text_JSON_, create_ts_, update_ts_)
    VALUES(%d,%d,%d,%d,%d)
    """
    try:
        cursor.execute(query,(id_, language_id_, menu_text_JSON_, create_ts_, update_ts_))
        connection.commit()
        print("application_menu_text record inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
