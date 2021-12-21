import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!!!!!"

@app.route('/home_page/<username>')
def home_page(username):
    return f"Hello, {username} World this is my Home page!!!!!"

app.run()