import datetime


class Product:
    def __init__(self, pid: int, product_name: str, product_price: int, product_cost: int, quantity: int,
                 production_date: datetime, expiration_date: datetime):
        # number
        self.pid = pid
        # string
        self.product_name = product_name
        # number, giá bán
        self.product_price = product_price
        # number, giá nhập
        self.product_cost = product_cost
        # number, số lượng
        self.quantity = quantity
        # class datetime.date, NSX
        self.production_date = production_date
        # class datetime.date, HSD
        self.expiration_date = expiration_date

    # Hiển thị sản phẩm
    def __str__(self):
        return (f"{self.pid}. {self.product_name} {self.product_price}đ {self.quantity} "
                f"{self.production_date} {self.expiration_date}")

    def sua_thong_tin(self, product_name_moi: str, product_price_moi: int, product_cost_moi: int, quantity_moi: int,
                      production_date_moi: datetime, expiration_date_moi: datetime):
        # string
        self.product_name = product_name_moi
        # number, giá bán
        self.product_price = product_price_moi
        # number, giá nhập
        self.product_cost = product_cost_moi
        # number, số lượng
        self.quantity = quantity_moi
        # class datetime.date, NSX
        self.production_date = production_date_moi
        # class datetime.date, HSD
        self.expiration_date = expiration_date_moi

    def get_pid(self):
        return self.pid

    def get_product_name(self):
        return self.product_name

    def get_product_price(self):
        return self.product_price

    def get_product_cost(self):
        return self.product_cost

    def get_quantity(self):
        return self.quantity

    def get_production_date(self):
        return self.production_date

    def get_expiration_date(self):
        return self.expiration_date

    def set_pid(self, pid):
        self.pid = pid

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_price(self, product_price):
        self.product_price = product_price

    def set_product_cost(self, product_cost):
        self.product_cost = product_cost

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_production_date(self, production_date):
        self.production_date = production_date

    def set_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date


class OrderProduct:
    def __init__(self, pid: int, product_name: str, order_quantity: int, product_price: int, total_amount: int):
        # pid class Product
        self.pid = int(pid)
        # product_name class Product
        self.product_name = product_name
        # number, số lượng mua
        self.order_quantity = order_quantity
        # product_price class Product
        self.product_price = product_price
        # thành tiền = order_quantity * product_price
        self.total_amount = total_amount

    def get_pid(self):
        return self.pid

    def get_product_name(self):
        return self.product_name

    def get_order_quantity(self):
        return self.order_quantity

    def get_product_price(self):
        return self.product_price

    def get_total_amount(self):
        return self.total_amount

    def set_pid(self, pid):
        self.pid = pid

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_order_quantity(self, order_quantity):
        self.order_quantity = order_quantity

    def set_product_price(self, product_price):
        self.product_price = product_price

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount


class Receipt:
    def __init__(self, rid: int, date_create: datetime, list_product: list, total: int):
        # number
        self.rid = rid
        # datetime.date, ngày xuất hóa đơn
        self.date_create = date_create
        # List, list OrderProduct
        self.list_product = list(list_product)
        # tổng tiền
        self.total = total

    def get_rid(self):
        return self.rid

    def get_date_create(self):
        return self.date_create

    def get_list_product(self):
        return self.list_product

    def get_total(self):
        return self.total

    def set_rid(self, rid):
        self.rid = rid

    def set_date_create(self, date_create):
        self.date_create = date_create

    def set_list_product(self, list_product):
        self.list_product = list_product

    def set_total(self, total):
        self.total = total
