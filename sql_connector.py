import configparser
import pyodbc

def get_sql_connection():
	try:
		config = configparser.ConfigParser()
		config.read('config.ini')

		server = config['DevSQL']['server']
		database = config['DevSQL']['database']
		username = config['DevSQL']['username']
		password = config['DevSQL']['password']

		conn = pyodbc.connect(
				'DRIVER={SQL Server};' \
				rf'SERVER={server};' \
				rf'DATABASE={database};' \
				rf'UID={username};' \
				rf'PWD={password}'
			)
		return conn
	except:
		raise

def execute_sql(sql_command, query_type = 'select', result_set_count = 1):
	try:
		conn = get_sql_connection()
		cursor = conn.cursor()
		cursor.execute(sql_command)

		if query_type == 'insert':
			conn.commit()

		result_set = []

		if query_type == 'select':
			while True:
				columns = [column[0] for column in cursor.description]
				rows = cursor.fetchall()

				if result_set_count == 1:
					result_set = [dict(zip(columns, row)) for row in rows]
				else:
					result_set.append([dict(zip(columns, row)) for row in rows])

				if not cursor.nextset():
					break

		cursor.close()
		return result_set
	except:
		raise
	finally:
		conn.close()