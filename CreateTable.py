import pyodbc
import Connection


def create_table():
    with pyodbc.connect(Connection.connectmysql()) as con:
        sql_cmd = """
            CREATE TABLE person(
              id int PRIMARY KEY AUTO_INCREMENT,
              name varchar(64),
              weight float,
              height float
            )
        """

    try:
        con.execute(sql_cmd)
    except pyodbc.ProgrammingError:
        print("Error Already Table")

# Call create_table()
create_table()