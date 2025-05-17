import frontend
import pandas as pd
import sqlite3
import re

DATABASE_PATH = 'medicine.db'
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
pattern_date = re.compile(r'^\d{4}-\d{2}-\d{2}$')
Medicine_List = []


def create_table():
    sql = ("""
            CREATE TABLE IF NOT EXISTS medicine (
            MedicineId INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) NOT NULL,
            Expiration_date TIMESTAMP
            )
            """
           )
    cursor.execute(sql)


def show_table():

    df = pd.read_sql_query("SELECT * FROM medicine", connection)
    print(df)

# check if there is such medicine


def insert_medicine(name: str, expiration_date: str):
    if pattern_date.match(expiration_date):
        sql = (
            """
            INSERT INTO medicine (Name, Expiration_date)
            VALUES
                (?,?);
            """
        )
        data_tuple = (name, expiration_date)
        cursor.execute(sql, data_tuple)
        connection.commit()
        Medicine_List.append(name)
    else:

        return False


def delete_medicine(name: str) -> None:
    sql = (
        """
        DELETE FROM medicine WHERE Name = (?);
        """
    )
    data_tuple = (name,)
    cursor.execute(sql, data_tuple)
    connection.commit()


def save_as_file():
    ...


if __name__ == "__main__":
    create_table()
    insert_medicine("Ibuprom", "2030-07-04")
    show_table()
    delete_medicine("Ibuprom")
    print("\nThere is the end\n")
    show_table()
    connection.close()
    frontend.Window().window.mainloop()
