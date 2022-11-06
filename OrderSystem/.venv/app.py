from flask import Flask
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
from flask import flash, request


app = Flask(__name__)
app.debug = True
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'order system'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# User Role
@app.route('/createUser', methods=['POST'])
def create_user():
    try:        
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        if _name and _email and request.method == 'POST':	
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)	
            sqlQuery = "INSERT INTO user(name, email) VALUES(%s, %s)"
            bindData = (_name, _email)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# Admin Role
@app.route('/users')
def user():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        userRows = cursor.fetchall()
        respone = jsonify(userRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# Admin Role
@app.route('/user/<userid>')
def user_details(userid):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE userid=%s", userid)
        userRow = cursor.fetchone()
        respone = jsonify(userRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# User Role
@app.route('/updateUser', methods=['PUT'])
def update_user():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _userid = _json['userid']
        if _name and _email and _userid and request.method == 'PUT':			
            sqlQuery = "UPDATE user SET name=%s, email=%s WHERE userid=%s"
            bindData = (_name, _email, _userid,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# User/Admin Role
@app.route('/deleteUser/<userid>', methods=['DELETE'])
def delete_user(userid):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM user WHERE userid=%s", (userid,))
		conn.commit()
		respone = jsonify('User deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Admin Role
@app.route('/createProduct', methods=['POST'])
def create_product():
    try:        
        _json = request.json
        _product_name = _json['product_name']
        _price = _json['price']
        if _product_name and _price and request.method == 'POST':	
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO product(product_name, price) VALUES(%s, %s)"
            bindData = (_product_name, _price)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Product added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# User/Admin Role
@app.route('/products')
def product():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT product_id, product_name, price FROM product")
        productRows = cursor.fetchall()
        respone = jsonify(productRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# User/Admin Role
@app.route('/product/<product_id>')
def product_details(product_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT product_id, product_name, price FROM product WHERE product_id =%s", product_id)
        productRow = cursor.fetchone()
        respone = jsonify(productRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# Admin Role
@app.route('/updateProduct', methods=['PUT'])
def update_product():
    try:
        _json = request.json
        _product_name = _json['product_name']
        _price = _json['price']
        _product_id = _json['product_id']
        if _product_name and _price and _product_id and request.method == 'PUT':			
            sqlQuery = "UPDATE product SET product_name=%s, price=%s WHERE product_id=%s"
            bindData = (_product_name, _price, _product_id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Product updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# Admin Role
@app.route('/deleteProduct/<product_id>', methods=['DELETE'])
def delete_product(product_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM product WHERE product_id=%s", (product_id,))
		conn.commit()
		respone = jsonify('Product deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# User Role
@app.route('/createOrder', methods=['POST'])
def create_order():
    try:        
        _json = request.json
        _userid = _json['userid']
        _order_details = _json['order_details']
        _amount = _json['amount']
        if _userid and _order_details and _amount and request.method == 'POST':	
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO orders(userid, order_details, amount) VALUES(%s, %s, %s)"
            bindData = (_userid, _order_details, _amount)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Order placed successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# Admin Role
@app.route('/orders')
def order():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT order_id, userid, order_details, amount FROM orders")
        orderRows = cursor.fetchall()
        respone = jsonify(orderRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# Admin Role
@app.route('/order/<order_id>')
def order_details(order_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT order_id, userid, order_details, amount FROM orders WHERE order_id =%s", order_id)
        orderRow = cursor.fetchone()
        respone = jsonify(orderRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()