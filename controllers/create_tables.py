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

def create_application_user_roles_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS application_user_roles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        role_name VARCHAR(20),
        create_ts DATETIME,
        update_ts DATETIME
    )
    """
    try:
        cursor.execute(query)
        print("application_user_roles table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_application_users_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS application_users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255),
        user_fname NVARCHAR(255),
        user_lname NVARCHAR(255),
        user_role_id INT,
        u_id VARCHAR(255),
        create_ts DATETIME,
        update_ts DATETIME,
        FOREIGN KEY (user_role_id) REFERENCES application_user_roles(id)
    )
    """
    try:
        cursor.execute(query)
        print("application_users table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_application_languages_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS application_languages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        lang_abb VARCHAR(3),
        language_full VARCHAR(15),
        create_ts DATETIME,
        update_ts DATETIME
    )
    """
    try:
        cursor.execute(query)
        print("application_languages table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_application_questions_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS application_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        language_id INT,
        question_category VARCHAR(255),
        question_JSON NVARCHAR(10000),
        create_ts DATETIME,
        update_ts DATETIME,
        FOREIGN KEY (language_id) REFERENCES application_languages(id)
    )
    """
    try:
        cursor.execute(query)
        print("application_questions table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_user_sessions_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS user_sessions (
      id INT AUTO_INCREMENT PRIMARY KEY,
      user_id INT,
      create_ts DATETIME,
      update_ts DATETIME,
      FOREIGN KEY (user_id) REFERENCES application_users(id)
    )
    """
    try:
        cursor.execute(query)
        print("user_sessions table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_user_questions_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS user_questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_sessions INT,
        language_id INT,
        questions_category VARCHAR(20),
        question_JSON NVARCHAR(10000),
        create_ts DATETIME,
        update_ts DATETIME,
        FOREIGN KEY (user_sessions) REFERENCES user_sessions(id),
        FOREIGN KEY (language_id) REFERENCES application_languages(id)
    )
    """
    try:
        cursor.execute(query)
        print("user_questions table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_application_menu_text_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS application_menu_text (
        id INT AUTO_INCREMENT PRIMARY KEY,
        language_id INT,
        menu_text_JSON NVARCHAR(10000),
        create_ts DATETIME,
        update_ts DATETIME,
        FOREIGN KEY (language_id) REFERENCES application_languages(id)
    )
    """
    try:
        cursor.execute(query)
        print("application_menu_text table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection()

create_application_user_roles_table(connection)
create_application_users_table(connection)
create_application_languages_table(connection)
create_application_questions_table(connection)
create_user_sessions_table(connection)
create_user_questions_table(connection)
create_application_menu_text_table(connection)
