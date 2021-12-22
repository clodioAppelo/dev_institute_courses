
import flask

app = flask.Flask(__name__)

list_of_articles = [
    {
        'title': 'articles',
        'content': 'This is my article',
        'author': "R R Martin"
    },
    {
        'title': 'article2',
        'content': 'article number two',
        'author': 'Mark Twain'
    }
]
@app.route('/blog')
def blog():
    return flask.render_template('homepage.html')

@app.route('/blog/articles')
def articles():
    return flask.render_template('article.html', articles=list_of_articles)

app.run()