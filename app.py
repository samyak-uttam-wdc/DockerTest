from flask import Flask, request, make_response

from sql_connector import execute_sql

app = Flask(__name__)

@app.route('/select', methods = ['GET'])
def select():
	try:
		table_name = request.args.get('table_name', '')
		query = rf'SELECT TOP 5 * FROM {table_name}' 
		return execute_sql(query, 'select')
	except:
		return 'Some error occured while executing the sql query.'

@app.route('/insert', methods = ['POST'])
def insert():
	try:
		data = request.get_json()
		value1 = data.get('value1', '')
		value2 = data.get('value2', '')
		query = 'INSERT INTO DockerTest VALUES (\'' + value1 + '\', \'' + value2 + '\')'
		execute_sql(query, 'insert')
		return 'Records inserted successfully.'
	except:
		return 'Some error occured while executing the sql query.'

if __name__ == '__main__':
	app.run(debug=False)