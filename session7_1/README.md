## The Flask Microframework

Flask is called a microframework because it is lightweight and minimalistic, providing the bare bones of features a simple web application requires. It is able to support basic HTTP requests, connections to databases and a frontend.

## Preclass

1. Work through one of option A, option B, or option C.
2. Question 1 applies what you've learned to creating a kanban board. This must
be answered. You will be asked to paste in a portion of your Kanban server code
in as a poll response, so please have this handy when you come to class. Note
that this preclass work forms the basis of assignment 2.
3. Question 2 is optional, but will give you insight into some of the techniques
used to create a more seamless user experience.

### Option A. Flaskr Microblogging Tutorial:

The official Flask tutorial covers setting up a simple microblogging
application. Work through the application here:
http://flask.pocoo.org/docs/0.12/tutorial/

If you want to compare your results with the final output, have a look here:
https://github.com/pallets/flask/tree/master/examples/flaskr/


### Option B. A Basic Todo Application:

Follow the youtube video at: https://www.youtube.com/watch?v=4kD-GRF5VPs

```bash
pip3 install flask Flask-SQLAlchemy
```

Once the program is running, then you can visit: http://127.0.0.1:5000/ and see
everything working!  Try adding new tasks and then marking them as done.

Notice how straightforward it is to use SQLAlchemy with Flask.  It is strongly
encouraged that you use SQLAlchemy for both your final project and your web
assignment.

(Optional) Find out how to use checkboxes to mark an item as complete.

### Option C. The Simplest Flask Application Ever:

Build a super-simple Flask application to your liking. Some ideas include:

1. Dice rolling service;
2. Email generator service;
3. A service that builds on the pre-class work you did for 9.1, the HTTP Requests class, like:
	- For instance, a simple maps service that pulls map data from Google Maps API
	- A service to query for current weather in different cities
	- A service to query for current cryptocurrency market prices
	- A service to query times in another time zone
4. Password generator (although it's bad to generate the passwords server side!)

Your web application should incorporate at least:
1. One HTTP `GET` request that retrieves something from either a local database or an online service.
2. One HTTP `POST` request. This will involve creating a form that takes user input (via HTML forms or Flask forms like WTForms).
3. A simple HTML frontend that has a form and has fields to output the values for your service.

Keep it short and simple!

You should be able to visit your site at: http://127.0.0.1:5000/.

### 1. Kanban server

After working through a Flask example and watching the ToDo application being
built, you should feel comfortable building your own Kanban application.

Your Kanban application should be able to:
1. Create a new item in the "To do" state.
2. Move any item from any state ("To do", "Doing", or "Done") to any other state.
3. Delete an item when it is done.
4. Perform some basic styling using a CSS file.  (This is shown in step 8 of the
   Flaskr tutorial)

### 2. (Optional) Building a JSON API in Flask

It is best practice to separate out your application data from the presentation
of the data.  Taken to its logical conclusion this leads to a clean separation
between static HTML and a JSON API.  (Just like those APIs that were queried
in the previous session.)  

Investigate the `jsonify()` method in Flask, as well as Flask `MethodViews`.
Together these can build a JSON API using sound object oriented principles.
As an example, one can use inheritance to ensure consistency between similar
end points.

One downside of this approach is that you now need to make client side requests.
Typically this is done in the webpage using JavaScript (or a JavaScript
framework).  There isn't enough time in this course to adequately cover
JavaScript, but if you already know some, or are willing to put the effort into
learning it, then please do so for this unit and/or the final project!
