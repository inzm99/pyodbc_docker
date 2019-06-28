import pyodbc

server = 'XXXXXX'
username = 'XXXXXXX'
password = 'XXXXXX'
port ='1433'
tsql ="select @@version"

cnn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT='+port+';UID='+username+';PWD='+ password)
cur = cnn.cursor()
cur.execute(tsql)
row = cur.fetchone()
print(str(row[0]))
