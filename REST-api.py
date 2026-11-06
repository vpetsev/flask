from flask import Flask, url_for, request, json, Response, jsonify

app = Flask(__name__)

# Simple flask.route decorator specifying route
@app.route('/')
def hello_world():
    return 'Hello World!'


# Another simple flask.route decorator without additional options
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


# The flask.route decorator can be replaced with
# specified converters with <converter:name>

# By default the route is a string - which accepts text without slashes
# @app.route('/articles/<article_reid>')
@app.route('/articles/<int:article_id>')
@app.route('/articles/<float:article_id>')
@app.route('/articles/<path:article_id>')
def api_article(article_id):
    return f'You are reading {article_id}'


# GET Parameters
    # Import request from flash
@app.route('/hello')
def api_hello():
    # GET /hello?name=Victor
    # > Hello Victor
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


# Request Methods (HTTP Verbs)
@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == "GET":
        return "ECHO: POST\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


# Request Data and Headers
    # import 'json' from flask
    # Files from forms can be posted via an HTML form with "request.files"
@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        """
            Request.data returns bytes? 
        """
        return "Text Message: " + str(request.data)

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'applications/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


# Configuring a response with Flask's Response class
@app.route('/helloResponse', methods=['GET'])
def api_hello_response():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)

    # Initializing a Response object. HTML mimetype by default.
    # Make_response() function is an alternative to manually initializing
    # Flask.jsonify() is also an alternative which sets appropriate headers
    resp = Response(js, status=200, mimetype='application/json')
    # Adds a value to resp header for the key Link
    resp.headers['Link'] = 'http://vpetsev.com'

    return resp


if __name__ == '__main__':
    app.run()
