#!/bin/bash

python create_schema.py

backend_url="http://127.0.0.1:5000/kneg"

curl -X POST "$backend_url/language" \
  -H "Content-Type: application/json" \
  -d '{"lang_abb": "en", "language_full": "English", "create_ts": "2023-09-06T10:00:00", "update_ts": "2023-09-06T10:00:00"}'

curl -X POST "$backend_url/user-role" \
  -H "Content-Type: application/json" \
  -d '{"role_name": "superadmin", "create_ts": "2023-09-06T10:00:00", "update_ts": "2023-09-06T10:00:00"}'

curl -X POST "$backend_url/user-role" \
  -H "Content-Type: application/json" \
  -d '{"role_name": "admin", "create_ts": "2023-09-06T10:00:00", "update_ts": "2023-09-06T10:00:00"}'

curl -X POST "$backend_url/user-role" \
  -H "Content-Type: application/json" \
  -d '{"role_name": "user", "create_ts": "2023-09-06T10:00:00", "update_ts": "2023-09-06T10:00:00"}'

curl -v -g -X POST "$backend_url/question" \
     -H "Content-Type: application/json" \
     -d @questions.json
