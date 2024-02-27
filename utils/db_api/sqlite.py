import sqlite3
conn = sqlite3.connect('data/main.db')


def is_user_in_db(id):
    count_of_user_id_in_db = conn.execute(f'''SELECT COUNT(id) FROM Users WHERE id = {id}''')
    return count_of_user_id_in_db.fetchall()[0][0]


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data



    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
        id	integer,
        balance integer,
        number integer,
        ref_father integer
        );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    def add_user_to_db(self, id: int, ref_father: int=0, balance: int=0, number:int=None,):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, ref_father, balance, number) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, ref_father, balance, number), commit=True)

    def update_user_balance(self, balance, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET balance = (balance + ?) WHERE id=?
        """
        return self.execute(sql, parameters=(balance, id), commit=True)

    def update_user_number(self, number, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET number = ? WHERE id=?
        """
        return self.execute(sql, parameters=(number, id), commit=True)

    def add_user(self, tg_id: int, number: int, balance: int=0):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(tg_id, number, balance ) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(tg_id, number, balance), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def count_users(self, user):
        return self.execute(f"SELECT COUNT(id)as count FROM Users WHERE ref_father={user}", fetchone=True)[0]

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)




def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")