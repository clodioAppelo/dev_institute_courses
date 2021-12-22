import flask

app = flask.Flask(__name__)


list_of_articles = [
	{
		'title': 'article1',
		'content': 'this is article 1',
		'author': 'bob1'
	},
	{
		'title': 'article2',
		'content': 'this is article 2',
		'author': 'bob2'
	}
]


for article in list_of_articles:
	print(article['title'])
	print(article['content'])
	print(article['author'])

@app.route('/blog')
def blog():
	return flask.render_template('homepage.html')


@app.route('/blog/articles')
def articles():
	return flask.render_template('articles.html', list_of_articles=list_of_articles)


app.run()
