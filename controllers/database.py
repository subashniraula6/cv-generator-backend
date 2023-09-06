# import os
# from dotenv import load_dotenv
# import mysql.connector
# from mysql.connector import Error

# load_dotenv()

# def create_connection():
#     connection = None
#     try:
#         db_host = os.getenv('DB_HOST')
#         # db_port = os.getenv('DB_PORT')
#         db_name = os.getenv('DB_NAME')
#         db_user = os.getenv('DB_USER')
#         db_password = os.getenv('DB_PASSWORD')
#         connection = mysql.connector.connect(
#             host=db_host,
#             # port=db_port,
#             database=db_name,
#             user=db_user,
#             password=db_password
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# def create_user_role_table(connection):
#     cursor = connection.cursor()
#     query = """
#     CREATE TABLE IF NOT EXISTS userRole (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       type VARCHAR(255) NOT NULL
#     )
#     """
#     try:
#         cursor.execute(query)
#         print("userRole table created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def create_user_table(connection):
#     cursor = connection.cursor()
#     query = """
#     CREATE TABLE IF NOT EXISTS user (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       uid VARCHAR(255) NOT NULL,
#       name NVARCHAR(255) NOT NULL,
#       user_type INT,
#       FOREIGN KEY (user_type) REFERENCES userRole(id)
#     )
#     """
#     try:
#         cursor.execute(query)
#         print("user table created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def search_user_by_uid(connection, uid):
#     cursor = connection.cursor()
#     query = """
#     SELECT u.id, u.uid, u.name, r.type
#     FROM user u
#     INNER JOIN userRole r ON u.user_type = r.id
#     WHERE u.uid = %s
#     """
#     result = None
#     try:
#         cursor.execute(query, (uid,))
#         result = cursor.fetchone()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")



# def insert_user_role(connection, role_type):
#     cursor = connection.cursor()
#     query = "INSERT INTO userRole (type) VALUES (%s)"
#     try:
#         cursor.execute(query, (role_type,))
#         connection.commit()
#         print("User role inserted successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def insert_user(connection, uid, name, user_type):
#     cursor = connection.cursor()
#     query = "INSERT INTO user (uid, name, user_type) VALUES (%s, %s, %s)"
#     try:
#         cursor.execute(query, (uid, name, user_type))
#         connection.commit()
#         print("User inserted successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")


# def insert_application_users(email: str
#                              , user_fname: str
#                              , user_lname: str
#                              , u_id: str
#                              ):
#     connection = create_connection()
#     cursor = connection.cursor()
#     query = """
#     INSERT INTO kneg.application_users(email
#                                     , user_fname
#                                     , user_lname
#                                     , user_role_id
#                                     , u_id
#                                     , create_ts
#                                     , update_ts
#                                     , delete_ts) 
#     VALUES(%s, %s, %s, 0, %s, NOW(), NOW(), NULL)
#     """
#     values = (email, user_fname, user_lname, u_id)
#     cursor.execute(query, values)
#     connection.commit()
#     cursor.close()
#     connection.close()





# connection = create_connection()

# create_user_role_table(connection)
# create_user_table(connection)


# # Insert user roles
# insert_user_role(connection, "admin")
# insert_user_role(connection, "editor")
# insert_user_role(connection, "viewer")

# # Insert users
# insert_user(connection, "user1", "Alice", 1)
# insert_user(connection, "user2", "Bob", 2)
# insert_user(connection, "user3", "Charlie", 3)


# def search_user_role(uid):
#     connection = create_connection()
#     result = search_user_by_uid(connection, uid)
#     if result:
#         id_, uid_, name_, role_ = result
#         return role_
#     else:
#         return None
