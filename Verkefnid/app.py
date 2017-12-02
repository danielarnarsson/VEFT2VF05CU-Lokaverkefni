from bottle import route, run, request, get, post, template, static_file
import pymysql

@route('/')
def forsida():
    return template('index')

@route('/sell', method = 'get')
def sell():
    return template('sell')

@route('/sell', method = 'post')
def save():
    text = request.forms.get('')

# CSS skrár.  Leitar að öllum css skráarheitum í static/css möppunni á vefrót
@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
	# static/css directory
	return static_file(filename, root='static/css')

# JPG og PNG skrár
@route('/static/img/<filename:re:.*\.(jpg|png)>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='static/img', mimetype='image/jpg')


run(host='localhost', port=8080, debug=True)