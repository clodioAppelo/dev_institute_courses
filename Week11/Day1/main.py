import flask

app = flask.Flask(__name__, template_folder='views')


@app.route('/')
def index():
    return flask.render_template("main_page.html")


@app.route('/users')
def users_page():
    template = """<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello from users</h1>
    </body>
</html>"""

    return template


@app.route('/home_page/<username>/<int:age>')
def home_page(username, age):
    template = """<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ template_username }} {{ user_age }}!</h1>
         <a href={{ url_for('users_page') }}> Users </a>
    </body>
</html>"""

    return flask.render_template_string(template, template_username=username, user_age=age)


@app.route("/nowhere")
def redirecting_view():
    return flask.redirect(flask.url_for('users_page')) # Redirect the user to the /home route


app.run(port=8080, debug=True)
