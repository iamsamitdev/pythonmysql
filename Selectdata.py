import pyodbc
import Connection


def select_data():
    with pyodbc.connect(Connection.connectmysql()) as con:
        sql_cmd = sql_cmd = """
            SELECT * FROM person WHERE name='Samit';
        """

        # keep value in list
        raw_data = []  # empty list

        # loop data
        for row in con.execute(sql_cmd):
            raw_data.append(row)

            # insert to table log_person
            sql_cmd_insert = " \
                    INSERT INTO log_person(name,weight,height,date_log) \
                    VALUES('{}',{},{},NOW()); \
                ".format(row[1], row[2], row[3])
            con.execute(sql_cmd_insert)

        print(raw_data)

# call select_data()
select_data()
