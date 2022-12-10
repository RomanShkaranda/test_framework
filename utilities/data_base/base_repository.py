import psycopg2


class BaseRepo:
    def __init__(self):
        self._connection = psycopg2.connect(user='mac',
                                            password='123',
                                            host='127.0.0.1',
                                            port='5432',
                                            database='testdb'
                                            )
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()
        self.table_name = ''

    def get_all(self):
        self._cursor.execute(f'select * from {self.table_name};')
        return self._cursor.fetchall()

    def insert_row(self, table_name, row_name):
        self._cursor.execute(f'alter table {table_name} add column {row_name} int;')

    def execute_script(self, script):
        return self._cursor.execute(script)

    def __del__(self):
        if self._connection:
            if self._cursor:
                self._cursor.close()
            self._connection.close()



