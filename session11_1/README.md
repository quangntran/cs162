## Security and Authentication

Webservers often need to serve confidential information securely.  
There are several things that can be done to help secure users' information.
For today's session we will focus on securing a simple user/password
combination, this is known as HTTP basic authentication.

We will also briefly touch on SQL injection, although if you are using
SQLAlchemy to query your data then you should be protected from these
vulnerabilities.

### HTTP Basic Authentication
A good introduction to basic authentication can be found at:
https://www.httpwatch.com/httpgallery/authentication/

You are also encouraged to explore the code contained in the current directory.
```bash
python3 runserver.py
```

Notice how the first request generates a 401 response, and your browser will
automatically show a username and password dialog box.  This username and
password is then sent in the HTTP request headers.

If the username and password are correct then the site will respond with a 200
response code, and return the confidential information.  If the username and
password do not match then there is again a 401 response.

The code is neatly separated in the sense that all authentication occurs in a
single file, and to use this functionality, a client simply has to decorate the
appropriate endpoints with `requires_authorization`.

For this section a lot of the code has been adapted from:
https://larsbergqvist.wordpress.com/2016/09/03/basic-authentication-with-python-flask/

### SQL Injection
This section borrows from:
https://www.acunetix.com/websitesecurity/sql-injection/

Imagine the follow short excerpt of Python code:
```python3
# Define POST variables
uname = request.form.get('username')
passwd = request.form.get('password')

# SQL query vulnerable to SQL injection
sql = "SELECT id FROM users WHERE username='" + uname + "' AND password='" + passwd + "';"

# Execute the SQL statement
database.execute(sql)
```
This code is dangerous, and can lead to all sorts of damage being done to your
database.

If a malicious user carefully crafted the following:
```
user="alice';--"
password="password"
```
then the sql query would become:
```sqlite3
SELECT id FROM users WHERE username='alice'; --' AND password='password';"
```
Notice how the "--" will comment out the rest of the line, and so the check for
a matching password is ignored. Most probably the calling code assumes that if
an ID is returned then the password matched, and authentication has succeeded.

In this case a malicious intruder can now log in with any username they choose,
and do not need to know the password!

But it gets worse than that.  If an intruder is able to inject any SQL code
they choose, then they can perform a denial of service query (ie. they can
create an query that would output trillions of rows, and the database will
start flooding the server with garbage).  They could insert any data that they
wanted, or they could even drop tables!


This comic is relevant: https://xkcd.com/327/


## Questions

Come to class with the Python code for your multi-user Kanban board, and
make sure that your passwords are suitably protected.
You should also have your SQL injection attack code ready and be able to
explain how and why your attack will work.

You must be able to paste any part of your code into a poll response.

### 1. Try an SQL Injection Hack 

It's time to give SQL Injection a shot using the `'' OR ''=''` SQL trick (which always returns True). Here's a hack to try at https://sqlzoo.net/hack/ to see if you can successfully gain access to a user's account.

1. Log in to the forum as "Jake" by passing "xxx" into the username and an SQL injection into the password. 
2. (Optional) Acquire a user's password and then log into the main forum. Post something there as the user. 

Walk through each of the tutorials to try to gain access to a user's account, then post something on the forum if you are able to! 

### 2. Write an SQL injection
Assume the following tables exist:
```sqlite3
CREATE TABLE users (
    userid INT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT
);
CREATE TABLE friends (
    friendid INT PRIMARY KEY,
    userid INT,
    name TEXT,
    phone DATETIME,
    age INT
);
```
And you have found the following two queries:
```python3
"SELECT userid FROM users WHERE username='" + uname + "' AND password='" + passwd + "';"
"SELECT name, phone, age FROM friends WHERE friendid = " + id + ";"
```
The webserver code will return an error if the first query returns a set of
results without a column called `id` that contains integers.  There will also be a
webserver error if the second query returns results without a column containing
`name` (of strings), a column containing `phone` (of strings), and `age` (of
integers).  If you're modifying or deleting things in the database then it
doesn't matter if the server raises an error, but if you'd like to see data
that's not meant for you then you need to make sure that the database doesn't
raise any errors.

Now do the following:
1. Write an attack which will list all the usernames and their passwords.
2. Write an attack which will update the table so that every entry in the
friends table has their userid set to 42.  (Hopefully this is the id of *your*
account, and now everyone has to be friends with you.  Who said hackers were
loners and never had any friends!)
3. Write an attack which will drop both tables.
4. (Optional) If you didn't know the name or schema of the tables, then write an
SQL injection attack which will list all the tables.  Now write an attack which
will list all columns within a given table.


### 3. Multiple User Kanban

Extend your Kanban board from previous weeks to allow multiple users.  Each
user should have their own username and password. For now assume that each
user wants their own **private** board (i.e. there are no shared Kanban boards).

### 4. Secure the user passwords
If you used the example code from `requires_authorization.py` then you will see
that usernames and passwords are stored directly in code, and passwords are
stored as plain text. To solve this properly, you will need to:
1. Store the user details in the database
2. Do not store the password in the database, instead store a cryptographic hash
of the password.
3. Make sure that the password is salted, and that the salt is unique for each
user. This helps significantly slows down intruders if they gain access to the
usernames and password hashes.

To read more about salting passwords, consider reading:
https://crackstation.net/hashing-security.htm
Although for our purposes, a standard hash function like md5 will be sufficient
and is already available in the standard Python libraries.

### 5. (Optional) SSL Certificates
HTTP basic authentication sends the username and password in plain text.  This
means that anyone who is handling web traffic and handles the request will be
able to see the username and password.  To avoid this the connection should
always be encrypted - HTTPS.  

In the original example
https://larsbergqvist.wordpress.com/2016/09/03/basic-authentication-with-python-flask/
there was already support for ssl.  

```python3
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=443)
```

HTTPS usually runs on port 443.  To run a webserver with a port in the range
0-1023 you will need root permissions.  Typically this can be run using:
```
$ sudo python3 runserver.py
```
In production the ssl security layer is usually handled separately by a reverse
proxy server like nginx or Apache.

### 6. (Optional) Change the password

It's a pretty essential requirement that at some point you are able to log into
the system and change your password.  Add this functionality to your Kanban
board.  

If you're also interested then you can also think about the required
flow for implementing a "Forgot your password" user flow.  This would require
having access to an SMTP server, and is overkill for our requirements!
Instead when the forgot password link is clicked, simply print the appropriate
URL to visit in the server logs.  This URL should contain a large random token
which makes it difficult for anyone else to guess the URL.

### 7. (Optional) Use a third party OAuth2 for user authentication

The complexity required in terms of managing a multitude of different passwords
across many different websites has meant that users typically prefer third party
authentication. This leads us to the final optional question.

There are several Python packages which simplify the process of getting a third
party login.  

 - https://pythonhosted.org/Flask-GoogleLogin/
 - https://authomatic.github.io/authomatic/

Do some research on the internet and find out how to get client credentials from
one of the main identity providers - eg. Google or Facebook.  Now add the third
party authentication to your Kanban application!
