import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='newuser',
            passwd='password',
            database='csv'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

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



# First, create a connection object
connection = create_connection()

# Insert data into the application_user_roles table
insert_application_user_roles(connection, "admin", "2023-09-04 19:42:35", "2023-09-04 19:42:35")
insert_application_user_roles(connection, "user", "2023-09-04 19:42:35", "2023-09-04 19:42:35")

# Insert data into the application_users table
insert_application_users(connection, "john.doe@example.com", "John", "Doe", 1, "johndoe123", "2023-09-04 19:42:35", "2023-09-04 19:42:35")
insert_application_users(connection, "jane.doe@example.com", "Jane", "Doe", 2, "janedoe123", "2023-09-04 19:42:35", "2023-09-04 19:42:35")

# Insert data into the application_languages table
insert_application_languages(connection, 'en', 'English', '2023-09-04 19:42:35', '2023-09-04 19:42:35')
insert_application_languages(connection, 'fr', 'French', '2023-09-04 19:42:35', '2023-09-04 19:42:35')

# Insert data into the application_questions table
question_JSON = '{"question": "What is your name?", "options": ["John", "Jane", "Bob", "Alice"]}'
insert_application_questions(connection, 1, 'personal', question_JSON, '2023-09-04 19:42:35', '2023-09-04 19:42:35')
question_JSON = '{"question": "What is your age?", "options": ["Under 18", "18-24", "25-34", "35 and above"]}'
insert_application_questions(connection, 1, 'personal', question_JSON, '2023-09-04 19:42:35', '2023-09-04 19:42:35')

# Insert data into the user_sessions table
insert_user_sessions(connection,1,'2023-09-04 19:42:35','2023-09-04 19:42:35')
insert_user_sessions(connection,2,'2023-09-04 19:42:35','2023-09-04 19:42:35')

# Insert data into the user_questions table
question_JSON = '{"question": "What is your favorite color?", "options": ["Red", "Blue", "Green", "Yellow"]}'
insert_user_questions(connection,1 ,1 ,'personal' ,question_JSON ,'2023-09-04 19:42:35' ,'2023-09-04 19:42:35')
question_JSON = '{"question": "What is your favorite food?", "options": ["Pizza", "Burger", "Pasta", "Sushi"]}'
insert_user_questions(connection,2 ,1 ,'personal' ,question_JSON ,'2023-09-04 19:42:35' ,'2023-09-04 19:42:35')

# Insert data into the application_menu_text table
menu_text_JSON = '{"menu_text": ["Home","About Us","Contact Us"]}'
insert_application_menu_text(connection,1 ,1 ,menu_text_JSON ,'2023-09-04 19:06:9', '2023-09-05 12:23:1')