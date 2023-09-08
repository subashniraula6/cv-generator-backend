## Add User Role (POST):
```
POST http://127.0.0.1:5000/kneg/user-role
Content-Type: application/json

{
    "role_name": "Admin",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get All User Roles (GET):
```
GET http://127.0.0.1:5000/kneg/user-roles
```

## Get User Role by ID (GET):
```
GET http://127.0.0.1:5000/kneg/user-role/{role_id}
```

## Modify User Role (PUT):
```
PUT http://127.0.0.1:5000/kneg/user-role/{role_id}
Content-Type: application/json

{
    "role_name": "Super Admin",
    "update_ts": "2023-09-07T12:00:00"
}
```

## Add User (POST):
```
POST http://127.0.0.1:5000/kneg/user
Content-Type: application/json

{
    "email": "user@example.com",
    "user_fname": "John",
    "user_lname": "Doe",
    "user_role_id": 1,
    "u_id": "123456789",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get All Users (GET):
```
GET http://127.0.0.1:5000/kneg/users
```

## Get User by ID (GET):
```
GET http://127.0.0.1:5000/kneg/user/{user_id}
```

## Modify User (PUT):
```
PUT http://127.0.0.1:5000/kneg/user/{user_id}
Content-Type: application/json

{
    "email": "updated_user@example.com",
    "user_fname": "Jane",
    "user_lname": "Doe",
    "user_role_id": 2,
    "u_id": "987654321",
    "update_ts": "2023-09-07T12:00:00"
}
```

## Add Language (POST):
```
POST http://127.0.0.1:5000/kneg/language
Content-Type: application/json

{
    "lang_abb": "en",
    "language_full": "English",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get All Languages (GET):
```
GET http://127.0.0.1:5000/kneg/languages
```

## Get Language by ID (GET):
```
GET http://127.0.0.1:5000/kneg/language/{language_id}
```

## Modify Language (PUT):
```
PUT http://127.0.0.1:5000/kneg/language/{language_id}
Content-Type: application/json

{
    "lang_abb": "fr",
    "language_full": "French",
    "update_ts": "2023-09-07T12:00:00"
}
```

## Add Question (POST):
```
POST http://127.0.0.1:5000/kneg/question
Content-Type: application/json

{
    "language_id": 1,
    "question_category": "General",
    "question_JSON": "What is the capital of France?",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get All Questions (GET):
```
GET http://127.0.0.1:5000/kneg/questions
```

## Get Question by ID (GET):
```
GET http://127.0.0.1:5000/kneg/question/{question_id}
```

## Get Question by User ID (GET):
```
GET http://127.0.0.1:5000/kneg/questions_per_user/{user_id}
```

## Modify Question (PUT):
```
PUT http://127.0.0.1:5000/kneg/question/<question_id>
Content-Type: application/json

{
    "language_id": 2,  ## Replace with a valid language ID
    "question_category": "Specific",
    "question_JSON": "{'text': 'How are you today?'}",
    "update_ts": "2023-09-07T10:00:00"
}
```

## Add a new user question:
```
POST http://127.0.0.1:5000/kneg/user_question
Content-Type: application/json

{
    "user_sessions": 1,  ## Replace with a valid user session ID
    "language_id": 1,    ## Replace with a valid language ID
    "questions_category": "General",
    "question_JSON": "{'text': 'What is your favorite color?'}",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get all user questions:
```
GET http://127.0.0.1:5000/kneg/user_questions
```

## Get a user question by ID (replace <user_question_id> with the actual user question ID):
```
GET http://127.0.0.1:5000/kneg/user_question/<user_question_id>
```

## Modify an existing user question (replace <user_question_id> with the actual user question ID):
```
PUT http://127.0.0.1:5000/kneg/user_question/<user_question_id>
Content-Type: application/json

{
    "user_sessions": 2,  ## Replace with a valid user session ID
    "language_id": 2,    ## Replace with a valid language ID
    "questions_category": "Specific",
    "question_JSON": "{'text': 'What is your favorite food?'}",
    "update_ts": "2023-09-07T10:00:00"
}
```

## Add a new menu text:
```
POST http://127.0.0.1:5000/kneg/menu_text
Content-Type: application/json

{
    "language_id": 1,  ## Replace with a valid language ID
    "menu_text_JSON": "{'home': 'Home', 'about': 'About Us'}",
    "create_ts": "2023-09-06T10:00:00",
    "update_ts": "2023-09-06T10:00:00"
}
```

## Get all menu texts:
```
GET http://127.0.0.1:5000/kneg/menu_texts
```

## Get a menu text by ID (replace <menu_text_id> with the actual menu text ID):
```
GET http://127.0.0.1:5000/kneg/menu_text/<menu_text_id>
```

## Modify an existing menu text (replace <menu_text_id> with the actual menu text ID):
```
PUT http://127.0.0.1:5000/kneg/menu_text/<menu_text_id>
Content-Type: application/json

{
    "language_id": 2,  ## Replace with a valid language ID
    "menu_text_JSON": "{'home': 'Accueil', 'about': 'À propos de nous'}",
    "update_ts": "2023-09-07T10:00:00"
}

```