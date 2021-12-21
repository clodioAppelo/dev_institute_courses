# Exercise 1

# C:\Users\lejai>py
# Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import flask
# >>> dir(flask)
# ['Blueprint', 'Config', 'Flask', 'Markup', 'Request', 'Response', '__builtins__', '__cached__',
#  '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__',
#  '_app_ctx_stack', '_request_ctx_stack', 'abort', 'after_this_request', 'app', 'appcontext_popped',
#  'appcontext_pushed', 'appcontext_tearing_down', 'before_render_template', 'blueprints', 'cli', 'config',
#  'copy_current_request_context', 'ctx', 'current_app', 'escape', 'flash', 'g', 'get_flashed_messages',
#  'get_template_attribute', 'globals', 'got_request_exception', 'has_app_context', 'has_request_context',
#  'helpers', 'json', 'jsonify', 'logging', 'make_response', 'message_flashed', 'redirect', 'render_template', 'render_template_string', 'request', 'request_finished', 'request_started', 'request_tearing_down', 'safe_join', 'scaffold', 'send_file', 'send_from_directory', 'session', 'sessions', 'signals', 'signals_available',
#  'stream_with_context', 'template_rendered', 'templating', 'typing', 'url_for', 'wrappers']


#-------------------------------------------------------------

# Exercise 2
# Using Flask, create a template for your CV.
# Your CV should contain:
# Your name
# A picture
# Your hobbies
# Your skills
# Your strengths
# Your weaknesses
# Bonus: Add some CSS
# Hint : To add some CSS take a look at the video called Static Files in the Online Learning section.

# Exercise 2
import flask

app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template('CV.html')


app.run(debug=True, port=8080)