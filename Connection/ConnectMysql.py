def connectmysql():
    return (
        'driver=MySQL ODBC 5.3 Unicode Driver;'
        'server=localhost;'
        'database=pythondbs;'
        'uid=root;'
        'pwd=1234'
    )
    # print(pyodbc.connect(con_string))
