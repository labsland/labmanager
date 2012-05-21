import getpass
from optparse import OptionParser

from config import USERNAME, PASSWORD, HOST, DBNAME

try:
    from config import USE_PYMYSQL
    if USE_PYMYSQL:
        import pymysql as dbi
    else:
        import MySQLdb as dbi
except:
    USE_PYMYSQL = False
    import MySQLdb as dbi

from labmanager.database import init_db

ROOT_USERNAME = None
ROOT_PASSWORD = None

def create_user():
    sentences = (
        "DROP USER '%s'@'localhost'" % USERNAME,
        "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'" % (USERNAME, PASSWORD),
        "GRANT ALL PRIVILEGES ON %s.* TO '%s'@'localhost' IDENTIFIED BY '%s'"  % (DBNAME, USERNAME, PASSWORD),
    )

    global ROOT_USERNAME, ROOT_PASSWORD
    ROOT_USERNAME = raw_input("MySQL administrator username (default 'root'): ") or "root"
    ROOT_PASSWORD = getpass.getpass( "MySQL administrator password: " )

    for num, sentence in enumerate(sentences):
        try:
            connection = dbi.connect(user=ROOT_USERNAME, passwd=ROOT_PASSWORD)
            cursor = connection.cursor()
            cursor.execute(sentence)
            connection.commit()
            connection.close()
        except:
            if num != 0: # If user does not exist
                raise

def create_db():
    global ROOT_USERNAME, ROOT_PASSWORD
    if ROOT_USERNAME is None or ROOT_PASSWORD is None:
        ROOT_USERNAME = raw_input("MySQL administrator username (default 'root'): ") or "root"
        ROOT_PASSWORD = getpass.getpass( "MySQL administrator password: " )

    try:
        connection = dbi.connect(user=ROOT_USERNAME, passwd=ROOT_PASSWORD, db = DBNAME, host = HOST) 
    except:
        pass # DB does not exist
    else:
        cursor = connection.cursor()
        cursor.execute("DROP DATABASE IF EXISTS %s" % DBNAME)
        connection.commit()
        connection.close()

    connection = dbi.connect(user=ROOT_USERNAME, passwd=ROOT_PASSWORD, host = HOST) 
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE %s" % DBNAME)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-c", "--create-user",
                    action="store_true", dest="create_user", default=False,
                    help="Creates the user and password in the database first")
    parser.add_option("-d", "--create-db",
                    action="store_true", dest="create_db", default=False,
                    help="Creates the database")

    (options, args) = parser.parse_args()

    if options.create_user:
        create_user()

    if options.create_db:
        create_db()

    init_db()
