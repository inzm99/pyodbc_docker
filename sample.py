import pyodbc

server = 'XXXXXX'
username = 'XXXXXXX'
password = 'XXXXXX'
port ='1433'

try:
    cnn = pyodbc.connect('DRIVER={FreeTDS};SERVER='+server+';PORT='+port+';UID='+username+';PWD='+ password)
    cur = cnn.cursor()
    type_no = 7
    cur.execute("""select @@version""")
    rows = cur.fetchall()
    print(rows)

    cur.close()
    cnn.close()
except (pyodbc.Error) as e:
    print (e)
    print (e.args[1])
