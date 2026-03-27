from app import app
from flask_mysqldb import MySQL
import os

# MySQL Settings - leídas directo de variables de entorno
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'db')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'flaskcrud')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_UNIX_SOCKET'] = None  # fuerza conexión TCP

mysql = MySQL(app)