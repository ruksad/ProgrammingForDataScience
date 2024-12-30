from timeit_util import time_decorator
import mysql.connector
import csv


@time_decorator
def import_into_mysq(file):
    connect = mysql.connector.connect(user='root', password='springBankPassword', host='localhost',
                                      database='ds_projects', use_pure=True)
    cursor = connect.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE BABY_NAMES (
            Id INT ,
            Name VARCHAR(255),
            Year INT,
            Sex VARCHAR(5),
            Count INT,
            PRIMARY KEY (Id)
        )
    ''')

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for row in reader:
            cursor.execute('insert into BABY_NAMES values(%s,%s,%s,%s,%s)', row)
    connect.commit()
    cursor.close()
    connect.close()


if __name__ == "__main__":
    import_into_mysq('sources/babynames.csv')
