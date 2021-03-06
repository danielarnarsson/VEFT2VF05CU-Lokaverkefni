from bottle import route, run, request, get, post, template, static_file, error
import pymysql.cursors
from sys import argv


@route('/')
@route('/category')
def forsida():
	try:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
		cur = connection.cursor()
		sql = "SELECT `category` FROM `products` GROUP BY category ORDER BY category"
		cur.execute(sql)
		categories=cur.fetchall()
		return template('index.tpl', categories=categories)
		connection.close()
	except Exception as e:
		return template('villa.tpl', e=e)


@route('/sell', method='GET')
def sell():
	try:
		return template('sell', saved=False)
	except Exception as e:
		return template('villa.tpl', e=e)


@route('/sell', method = 'POST')
def save():
	try:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
		cur = connection.cursor()
		category = request.forms.get('category')
		title = request.forms.get('title')
		price = request.forms.get('price')
		info = request.forms.get('info') 
		sql = "INSERT INTO `products` (`CATEGORY`, `TITLE`, `PRICE`, `INFO`) VALUES (%s, %s, %s, %s)"
		cur.execute(sql, (category, title, price, info))
		connection.commit()
		return template('sell.tpl', saved=True)
		connection.close()
	except Exception as e:
		return template('villa.tpl', e=e)


@route('/books')
@route('/Books')
def books():
	try:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
		cur = connection.cursor()
		sql = "SELECT title, price, info FROM `products` WHERE category LIKE 'books'"
		cur.execute(sql)
		products = cur.fetchall()
		return template('products.tpl', products=products)
		connection.close()
	except Exception as e:
		return template('villa.tpl', e=e)


@route('/Computers')
@route('/computers')
def computer():
	try:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
		sql = "SELECT title, price, info FROM `products` WHERE category LIKE 'computers'"
		cur = connection.cursor()
		cur.execute(sql)
		products = cur.fetchall()
		return template('products.tpl', products=products)
		connection.close()
	except Exception as e:
		return template('villa.tpl', e=e)


@route('/Cars')
@route('/cars')
def cars():
	try:
		connection = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1907002160', passwd='mypassword', db='1907002160_VEFTH2_lokaverkefni')
		cur = connection.cursor()
		sql = "SELECT title, price, info FROM `products` WHERE category LIKE 'cars'"
		cur.execute(sql)
		products = cur.fetchall()
		return template('products.tpl', products=products)
		connection.close()
	except Exception as e:
		return template('villa.tpl', e=e)


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


@error(404)
def custom404(error):
	return template('villa404.tpl')

if __name__ == "__main__":
	run(host='0.0.0.0', port=argv[1])
