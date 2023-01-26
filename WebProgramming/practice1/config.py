db = {
    'user'     : 'root',
    'password' : '1234',
    'host'     : '127.0.0.1',
    'port'     : '3307',
    'database' : 'flyai'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
