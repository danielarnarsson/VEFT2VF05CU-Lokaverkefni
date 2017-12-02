from bottle import route, run, request, get, post, template, static_file
import pymysql.cursors

@route('/')
def forsida():
    return template('index')

@route('/sell', method='GET')
def sell():
    return template('sell', saved=False)

@route('/sell', method = 'POST')
def save():
	category = request.forms.get('category')
	title = request.forms.get('title')
	price = request.forms.get('price')
	info = request.forms.get('info')
	connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
	cur = connection.cursor()
	cur.execute("INSERT INTO `products` (`CATEGORY`, `TITLE`, `PRICE`, `INFO`) VALUES (%s, %s, %s, %s)", (category, title, price, info))
	connection.commit()
	return template('sell', saved=True)

# CSS skrár.  Leitar að öllum css skráarheitum í static/css möppunni á vefrót
@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
	# static/css directory
	return static_file(filename, root='static/css')

# JPG og PNG skrár
@route('/static/img/<filename:re:.*\.(jpg|jpeg|png)>')
def send_image(filename):
    # static/img directory
    return static_file(filename, root='static/img', mimetype='image/jpeg,image/png')


run(host='localhost', port=8080, debug=True)