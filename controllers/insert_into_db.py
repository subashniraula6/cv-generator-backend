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
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")

class InsertInDB:

    def __init__(self):
        self.connection = create_connection()

    def insert_application_user_roles(self,  role_name, create_ts, update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO application_user_roles (role_name, create_ts, update_ts)
        VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(query, (role_name, create_ts, update_ts))
            self.connection.commit()
            print("application_user_roles record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

  
    def insert_application_users(self, email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO application_users (email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (email, user_fname, user_lname, user_role_id, u_id, create_ts, update_ts))
            self.connection.commit()
            print("application_users record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_application_languages(self, lang_abb, language_full, create_ts, update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO application_languages (lang_abb, language_full, create_ts, update_ts)
        VALUES (%s,%s,%s,%s)
        """
        try:
            cursor.execute(query,(lang_abb ,language_full ,create_ts ,update_ts))
            self.connection.commit()
            print("application_languages record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_application_questions(self,language_id ,question_category ,question_JSON ,create_ts ,update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO application_questions (language_id ,question_category ,question_JSON ,create_ts ,update_ts)
        VALUES (%s,%s,%s,%s,%s)
        """
        try:
            cursor.execute(query,(language_id ,question_category ,question_JSON ,create_ts ,update_ts))
            self.connection.commit()
            print("application_questions record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_user_sessions(self,user_id ,create_ts ,update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO user_sessions (user_id ,create_ts ,update_ts)
        VALUES (%s,%s,%s)
        """
        try:
            cursor.execute(query,(user_id ,create_ts ,update_ts))
            self.connection.commit()
            print("user_sessions record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_user_questions(self, user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO user_questions (user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        try:
            cursor.execute(query,(user_sessions ,language_id ,questions_category ,question_JSON ,create_ts ,update_ts))
            self.connection.commit()
            print("user_questions record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_application_menu_text(self,id_, language_id_, menu_text_JSON_, create_ts_, update_ts_):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO application_menu_text(id_, language_id_, menu_text_JSON_, create_ts_, update_ts_)
        VALUES(%d,%d,%d,%d,%d)
        """
        try:
            cursor.execute(query,(id_, language_id_, menu_text_JSON_, create_ts_, update_ts_))
            self.connection.commit()
            print("application_menu_text record inserted successfully")
        except Error as e:
            print(f"The error '{e}' occurred")




# create an instance of the InsertInDB class
db = InsertInDB()

# First, create a connection object
connection = create_connection()

# Insert data into the application_user_roles table
db.insert_application_user_roles( "admin", "2023-09-04 19:42:35", "2023-09-04 19:42:35")
db.insert_application_user_roles( "user", "2023-09-04 19:42:35", "2023-09-04 19:42:35")

# Insert data into the application_users table
db.insert_application_users( "john.doe@example.com", "John", "Doe", 1, "johndoe123", "2023-09-04 19:42:35", "2023-09-04 19:42:35")
db.insert_application_users( "jane.doe@example.com", "Jane", "Doe", 2, "janedoe123", "2023-09-04 19:42:35", "2023-09-04 19:42:35")

# Insert data into the application_languages table
db.insert_application_languages( 'fr', 'French', '2023-09-04 19:42:35', '2023-09-04 19:42:35')

# Insert data into the application_questions table
question_JSON = '{"question": "What is your name?", "options": ["John", "Jane", "Bob", "Alice"]}'
db.insert_application_questions( 1, 'personal', question_JSON, '2023-09-04 19:42:35', '2023-09-04 19:42:35')
question_JSON = '{"question": "What is your age?", "options": ["Under 18", "18-24", "25-34", "35 and above"]}'
db.insert_application_questions( 1, 'personal', question_JSON, '2023-09-04 19:42:35', '2023-09-04 19:42:35')

# Insert data into the user_sessions table
db.insert_user_sessions(1,'2023-09-04 19:42:35','2023-09-04 19:42:35')
db.insert_user_sessions(2,'2023-09-04 19:42:35','2023-09-04 19:42:35')

# Insert data into the user_questions table
question_JSON = '{"question": "What is your favorite color?", "options": ["Red", "Blue", "Green", "Yellow"]}'
db.insert_user_questions(1 ,1 ,'personal' ,question_JSON ,'2023-09-04 19:42:35' ,'2023-09-04 19:42:35')
question_JSON = '{"question": "What is your favorite food?", "options": ["Pizza", "Burger", "Pasta", "Sushi"]}'
db.insert_user_questions(2 ,1 ,'personal' ,question_JSON ,'2023-09-04 19:42:35' ,'2023-09-04 19:42:35')

# Insert data into the application_menu_text table
menu_text_JSON = '{"menu_text": ["Home","About Us","Contact Us"]}'
db.insert_application_menu_text(1 ,1 ,menu_text_JSON ,'2023-09-04 19')