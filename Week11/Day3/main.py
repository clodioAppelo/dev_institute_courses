import flask
from flask import render_template

app = flask.Flask(__name__, template_folder="views")


@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/home_page/<username>/<int:age>')
def home_page(username, age):
    return flask.render_template("home_page.html", template_username=username, user_age=age)


@app.route("/nowhere")
def redirecting_view():
    return flask.redirect(flask.url_for('users_page')) # Redirect the user to the /home route


if __name__ == '__main__':
    app.run(port=8080, debug=True)
