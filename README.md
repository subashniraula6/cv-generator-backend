# README
### Local Dev
```
python app.py
```
### For Server
```
gunicorn app:app
```

# Create a newuser and Grant Privileges 
```SQLcommand
CREATE USER 'newuser'@'localhost' IDENTIFIED by 'password';

USE cvGenerator;
GRANT ALL PRIVILEGES ON cvGenerator TO 'newuser'@'localhost'
```

# To search User-role using uid
```
http://localhost:5000/search?uid=user1 

# returns 
role is 	"editor"
uid	      "user2"

```

