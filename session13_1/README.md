## Integration testing
Unit testing occurs at a very low level.  It typically involves extensively
testing a single function so that all edge cases are correctly handled.

Integration testing occurs at the other end of the spectrum.  It typically
involves far fewer tests, and ensures that all parts of the system are correctly
working together.


## Questions

### Q1. Synthesis

For this session, you will write a short Python program to verify that the
computation server is correctly storing the information in the database.

You will need to get the computation server up and running (`docker stack
deploy` should be sufficient in this case).

Your program must do the following things:
1. POST an HTTP request with a valid expression to the server.
Examine the response and confirm that the correct answer is returned.
2. Establish a connection to the database directly and verify
that the string you sent has been correctly stored in the database.
For this step, you can use SQLAlchemy, or write the SQL directly if you prefer,
however note that this is a postgres database which does have subtly different
syntax from sqlite.  (For simple queries this shouldn't be a big issue.)
3. POST an HTTP request with an invalid expression to the server.
Examine the response and confirm that an error is raised.
4. Confirm that no more rows have been added to the database since the last
valid expression was sent to the server. (For the purposes of this class, you
can assume that no-one else is accessing the database while the tests are
running.)
5. If any of the tests fail, then your program should raise an exception, and
stop running.  Your program should only complete successfully if all tests pass.

**Store your Python code on Github as either a gist or a repo. When you come to
class have the URL ready to paste into a poll answer.**
