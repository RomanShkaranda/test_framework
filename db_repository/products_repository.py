from utilities.data_base.base_repository import BaseRepo


class ProductsRepository(BaseRepo):
    def __init__(self):
        super().__init__()
        self.table_name = 'products'

    def create_table_products(self, table_name):
        self._cursor.execute(f'create table {table_name} (id serial, name varchar(10), price int);')

    def set_products_primary_key(self):
        self._cursor.execute(f'alter table products add primary key(id);')

    def get_product_by_id(self, product_id):
        self._cursor.execute(f'select * from {self.table_name} where id = {product_id}')
        return self._cursor.fetchone()

    def insert_one(self, name, price):
        self._cursor.execute(f"insert into {self.table_name} (name, price) values (%s, %s);", (name, price))

    def delete_by_name(self, name):
        self._cursor.execute(f"delete from {self.table_name} where {self.table_name}.name = '{name}';")


