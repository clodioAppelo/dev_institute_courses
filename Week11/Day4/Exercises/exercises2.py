
import flask
import json

app = flask.Flask(__name__)


def load_database(src_file='product_db.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data


@app.route('/')
def home():
    return flask.render_template('homepage.html')


@app.route('/products')
def products():
    info = load_database()
    return flask.render_template('products.html', products=info)


@app.route('/product/<product_id>')
def prod_details(product_id):
    info = load_database()
    return flask.render_template('product_details.html', products=info, prod_id=product_id)


if __name__ == "__main__":
    app.run(debug=True,port=4545)