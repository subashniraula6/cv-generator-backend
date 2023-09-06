# import mysql.connector
# from mysql.connector import Error

# def create_connection():
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='knegUser',
#             passwd='MyPassw0rd123!',
#             database='kneg',
#             connect_timeout=28800
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# def execute_query(connection, query):
#     connection = create_connection()
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#         return cursor.fetchall()  # or cursor.fetchone() for a single row
#     except Error as e:
#         print(f"The error '{e}' occurred")
#     finally:
#         cursor.close()

# def show_grant(connection):
#     query ="""
#     SHOW GRANTS;
#     """
#     print(execute_query(connection, query))

# def create_application_user_roles_table(connection):
#     query = """
#     CREATE TABLE IF NOT EXISTS application_user_roles (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         role_name VARCHAR(20),
#         create_ts DATETIME,
#         update_ts DATETIME
#     );
#     """
#     print(execute_query(connection, query))

# def show_application_user_roles_table(connection):
#     query="""
#     SELECT * FROM kneg.application_user_roles;
#     """
#     execute_query(connection,query)

# def create_application_users_table(connection):
#     query = """
#     USE kneg;
#     CREATE TABLE IF NOT EXISTS application_users (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         email VARCHAR(255),
#         user_fname NVARCHAR(255),
#         user_lname NVARCHAR(255),
#         user_role_id INT,
#         u_id VARCHAR(255),
#         create_ts DATETIME,
#         update_ts DATETIME,
#         FOREIGN KEY (user_role_id) REFERENCES application_user_roles(id)
#     );
#     """
#     print(execute_query(connection, query))

# def create_application_languages_table(connection):
#     query = """
#     USE kneg;
#         id INT PRIMARY KEY,
#     CREATE TABLE IF NOT EXISTS application_languages (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         lang_abb VARCHAR(3),
#         language_full VARCHAR(15),
#         create_ts DATETIME,
#         update_ts DATETIME
#     );
#     """
#     print(execute_query(connection, query))

# def create_application_questions_table(connection):
#     query = """
#     USE kneg;
#     CREATE TABLE IF NOT EXISTS application_questions (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         language_id INT,
#         question_category VARCHAR(255),
#         question_JSON NVARCHAR(10000),
#         create_ts DATETIME,
#         update_ts DATETIME,
#         FOREIGN KEY (language_id) REFERENCES application_languages(id)
#     );
#     """
#     print(execute_query(connection, query))

# def create_user_sessions_table(connection):
#     query = """
#     USE kneg;
#     CREATE TABLE IF NOT EXISTS user_sessions (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       user_id INT,
#       create_ts DATETIME,
#       update_ts DATETIME,
#       FOREIGN KEY (user_id) REFERENCES application_users(id)
#     );
#     """
#     print(execute_query(connection, query))

# def create_user_questions_table(connection):
#     query = """
#     USE kneg;
#     CREATE TABLE IF NOT EXISTS user_questions (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         user_sessions INT,
#         language_id INT,
#         questions_category VARCHAR(20),
#         question_JSON NVARCHAR(10000),
#         create_ts DATETIME,
#         update_ts DATETIME,
#         FOREIGN KEY (user_sessions) REFERENCES user_sessions(id),
#         FOREIGN KEY (language_id) REFERENCES application_languages(id)
#     );
#     """
#     print(execute_query(connection, query))

# def create_application_menu_text_table(connection):
#     query = """
#     USE kneg;
#     CREATE TABLE IF NOT EXISTS application_menu_text (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         language_id INT,
#         menu_text_JSON NVARCHAR(10000),
#         create_ts DATETIME,
#         update_ts DATETIME,
#         FOREIGN KEY (language_id) REFERENCES application_languages(id)
#     )
#     """
#     print(execute_query(connection, query))

# def main():
#     connection = create_connection()

#     # show_grant(connection)
#     create_application_user_roles_table(connection)
#     show_application_user_roles_table(connection)
#     create_application_users_table(connection)
#     create_application_languages_table(connection)
#     create_application_questions_table(connection)
#     create_user_sessions_table(connection)
#     create_user_questions_table(connection)
#     create_application_menu_text_table(connection)
    
#     connection.close()  # Close the connection when done

# if __name__ == "__main__":
#     main()
