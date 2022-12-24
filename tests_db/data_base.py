from db_repository.orders_repository import OrdersRepository
from db_repository.products_repository import ProductsRepository
from utilities.data_base.base_repository import BaseRepo

products_repo = ProductsRepository()
orders_repo = OrdersRepository()

products_repo.create_table_products('products')
products_repo.set_products_primary_key()
orders_repo.create_table_orders('orders')
orders_repo.insert_row('orders', 'quantity')
products_repo.insert_one('soup', 20)
products_repo.insert_one('salad', 30)
products_repo.insert_one('potato', 30)
products_repo.insert_one('pasta', 50)
products_repo.insert_one('beverage', 10)
orders_repo.insert_one(1, 3, 2)
orders_repo.insert_one(2, 4, 1)
orders_repo.insert_one(3, 1, 2)
orders_repo.insert_one(4, 2, 2)
orders_repo.insert_one(5, 5, 6)
BaseRepo().execute_script("select p.name, p.price, o.quantity from products as p join orders as o on o.product_id = p.id;")


