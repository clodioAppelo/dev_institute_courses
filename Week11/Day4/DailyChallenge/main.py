
import flask

app = flask.Flask(__name__)


@app.route('/')
def main():
    return flask.render_template('homepage.html', color= 'white')


@app.route('/blue')
def blue():
    return flask.render_template('homepage.html', color= 'blue')


@app.route('/red')
def red():
    return flask.render_template('homepage.html', color= 'red')


@app.route('/green')
def green():
    return flask.render_template('homepage.html', color= 'green')


@app.route('/yellow')
def yellow():
    return flask.render_template('homepage.html', color= 'yellow')


if __name__ == '__main__':
    app.run(port=4545)