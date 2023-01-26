import mysql.connector
from mysql.connector import errorcode


config = {
  'host':'mydemoserver35.mysql.database.azure.com',
  'user':'user35',
  'password':'qwer12341234!',
  'database':'testdb1',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': './DigiCertGlobalRootG2.crt.pem'
}