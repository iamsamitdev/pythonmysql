import pyodbc
import Connection


def insert_data(inp_data):
    with pyodbc.connect(Connection.connectmysql()) as con:
        sql_cmd = " \
            INSERT INTO person(name,weight,height) \
            VALUES({}); \
        ".format(inp_data)
        con.execute(sql_cmd)
        print("Insert data success")


# recieve data from user
inp_name = input("Input your name: ")
inp_weight = float(input("Input your weight: "))
inp_height = float(input("Input your height: "))

my_data = f"'{inp_name}',{inp_weight},{inp_height}"

# call function
insert_data(my_data)
