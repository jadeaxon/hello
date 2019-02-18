# https://cx-oracle.readthedocs.io/en/latest/index.html
# Even though PyCharm thinks this module DNE, it does.
# Conforms to Python Database API Specification 2.0.
#
# PRE: Make a python3 user in your Oracle database.
# PRE: Install Oracle database on localhost.
# PRE: Install Oracle client files.
# PRE: Install cx_Oracle Python module.
# PRE: Put user python3's password in password.dat file.
# PRE: Create table python3.person table.  Insert some data.
import cx_Oracle

file = open("password.dat")
password = file.read().strip()

connection = cx_Oracle.connect('python3/{}@localhost'.format(password))

cursor = connection.cursor()
query = 'select * from person'
cursor.execute(query)
# This returns all the rows fetched by the query as tuples.
rows = cursor.fetchall()
for row in rows:
    print(row)

exit(0)
