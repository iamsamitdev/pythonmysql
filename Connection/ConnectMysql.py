def connectmysql():
    con_string = 'driver=MySQL ODBC 5.3 Unicode Driver;' \
             'server=localhost;' \
             'database=pythondbs;' \
             'uid=root;' \
             'pwd=1234'
    return con_string
    # print(pyodbc.connect(con_string))
