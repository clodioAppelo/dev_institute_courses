# Instructions:
# Build a lesson page for the di-learning platform !
#
# Create a directory called lesson1.
#
# Inside the directory there should be 2 markdown files (.md) : in-this-chapter.md and exercises.md
# Check out the hint below for more information on markdown file.
# Check out the markdown documentation.
#
# The first file in-this-chapter.md should contain a lesson of your choice.
#
# The second file exercises.md should contain exercises (it can be yours or it can be from the platform).
#
# Make a beautiful flask website that displays the content (like the DI platform). The page needs to have two tabs,
# one for the lesson and one for the exercises.


import flask

app = flask.Flask(__name__, template_folder='lesson1')


@app.route("/")
def chapter():
    return flask.render_template('in-this-chapter.md')


@app.route("/exercises")
def exercises():
    return flask.render_template('exercises.md')


app.run(debug=True, port=8080)