import json
from dateutil import parser
from datetime import datetime
from models.kneg_models import db, Language, Question, UserRole

# Load seed JSON files
try:
    with open("languages.json", "r") as f:
        languages_data = json.load(f)
except FileNotFoundError:
    languages_data = []
    print("languages.json not found, skipping language seeding.")

try:
    with open("roles.json", "r") as f:
        roles_data = json.load(f)
except FileNotFoundError:
    roles_data = []
    print("roles.json not found, skipping role seeding.")

try:
    with open("questions.json", "r") as f:
        questions_data = json.load(f)
except FileNotFoundError:
    questions_data = {}
    print("questions.json not found, skipping question seeding.")


def seed_defaults():
    # ----------------------
    # 1. Seed Languages
    # ----------------------
    for lang in languages_data:
        existing = Language.query.filter_by(lang_abb=lang["lang_abb"]).first()
        if not existing:
            create_ts = parser.parse(lang.get("create_ts")) if "create_ts" in lang else datetime.utcnow()
            update_ts = parser.parse(lang.get("update_ts")) if "update_ts" in lang else datetime.utcnow()
            new_lang = Language(
                lang_abb=lang["lang_abb"],
                language_full=lang["language_full"],
                create_ts=create_ts,
                update_ts=update_ts
            )
            db.session.add(new_lang)
            print(f"Inserted language: {lang['language_full']}")

    db.session.commit()  # commit languages first (needed for FK)

    # ----------------------
    # 2. Seed User Roles
    # ----------------------
    for role in roles_data:
        existing = UserRole.query.filter_by(role_name=role["role_name"]).first()
        if not existing:
            create_ts = parser.parse(role.get("create_ts")) if "create_ts" in role else datetime.utcnow()
            update_ts = parser.parse(role.get("update_ts")) if "update_ts" in role else datetime.utcnow()
            new_role = UserRole(
                role_name=role["role_name"],
                create_ts=create_ts,
                update_ts=update_ts
            )
            db.session.add(new_role)
            print(f"Inserted role: {role['role_name']}")

    db.session.commit()

    # ----------------------
    # 3. Seed Questions
    # ----------------------
    if questions_data:
        lang_id = questions_data.get("language_id")
        question_category = questions_data.get("question_category")

        exists = Question.query.filter_by(
            language_id=lang_id,
            question_category=question_category
        ).first()

        if not exists:
            create_ts = parser.parse(questions_data.get("create_ts")) if "create_ts" in questions_data else datetime.utcnow()
            update_ts = parser.parse(questions_data.get("update_ts")) if "update_ts" in questions_data else datetime.utcnow()
            new_question = Question(
                language_id=lang_id,
                question_category=question_category,
                question_JSON=json.dumps(questions_data.get("question_JSON", {})),
                create_ts=create_ts,
                update_ts=update_ts
            )
            db.session.add(new_question)
            db.session.commit()
            print(f"Inserted questions for language_id={lang_id}, category={question_category}")
        else:
            print(f"Questions for language_id={lang_id}, category={question_category} already exist")

    print("Seeding complete!")


# Run manually
if __name__ == "__main__":
    from app import app

    with app.app_context():
        db.create_all()  # create tables if not exist
        seed_defaults()
