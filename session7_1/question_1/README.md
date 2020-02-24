IN TERMINAL:

sqlite3 todo.db
sqlite> .exit

python
>>> from app import db
>>> db.create_all()
>>> exit()

python app.py

^^^ If get "OSError: [Errno 48] Address already in use", run "kill $(lsof -t -i:5000)" in Terminal to kill whatever's running on port 5000.


THEN GO TO http://127.0.0.1:5000/

