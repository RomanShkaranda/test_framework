from utilities.data_base.base_repository import BaseRepo


class OrdersRepository(BaseRepo):
    def __init__(self):
        super().__init__()
        self.table_name = 'orders'

    def create_table_orders(self, table_name):
        self._cursor.execute(f'create table {table_name} '
                             f'(id int primary key, product_id int, constraint fk_product_id foreign key(product_id) '
                             f'references products(id));')

    def insert_one(self, order_id, product_id, quantity):
        self._cursor.execute(f"insert into {self.table_name} (id, product_id, quantity) values (%s, %s, %s);",
                             (order_id, product_id, quantity))

