import Models
import datetime

# lưu thông tin sản phẩm và hóa đơn
products, receipts = [], []
p1 = Models.Product(1, "product_demo", 20000, 8000, 10,
                    "18-11-2023", "1-12-2023")
p2 = Models.Product(2, "product_demo2product_demo2", 15000, 12000, 15,
                    "18-11-2023", "1-12-2023")
products.append(p1)
products.append(p2)

# mua sản phẩm
op1 = Models.OrderProduct(p1.get_pid(), p1.get_product_name(), 4, p1.get_product_price(),
                          4 * p1.get_product_price())
op2 = Models.OrderProduct(p2.get_pid(), p2.get_product_name(), 2, p2.get_product_price(),
                          2 * p2.get_product_price())

# tạo và lưu hóa đơn
r1 = Models.Receipt(1, datetime.datetime.now().strftime('%d-%m-%Y'), [op1],
                    int(op1.get_product_price()) * int(op1.get_order_quantity()))
receipts.append(r1)


# tổng doanh thu 1 mặt hàng
def product_revenue(pid: int) -> int:
    _total = 0
    for _receipt in receipts:
        _list_order_product = _receipt.get_list_product()
        for _order_product in _list_order_product:
            if _order_product.get_pid() == pid:
                _total += _order_product.get_total_amount()

    return _total


def get_revenue(product):
    return product[1]


class ManageProduct:
    # Thêm mới hàng hóa
    pass

    # Tìm kiếm hàng hóa
    pass

    # Sửa thông tin hàng hóa
    pass

    # Sắp xếp tổng doanh thu từng mặt hàng(Dựa vào lựa chọn của người dùng: cao xuống thấp hay thấp lên cao)
    @staticmethod
    def sort_product_revenue(reverse: bool):
        _data_revenues = []
        for _product in products:
            _product_revenue = [_product.get_product_name(), product_revenue(_product.get_pid())]
            _data_revenues.append(_product_revenue)

        _data_revenues.sort(key=get_revenue, reverse=reverse)
        return _data_revenues

    # Tính tổng doanh thu theo ngày từng mặt hàng
    pass

    # Tính tổng doanh thu theo ngày của cửa hàng(theo tháng, năm)
    pass

    # Hiển thị 5 mặt hàng có tổng doanh thu cao nhất, 5 mặt hàng có tổng doanh thu thấp nhất.
    @staticmethod
    def listed_highest_product_revenue():
        _data_revenues = ManageProduct.sort_product_revenue(True)
        return _data_revenues[:5]

    @staticmethod
    def listed_lowest_product_revenue():
        _data_revenues = ManageProduct.sort_product_revenue(False)
        return _data_revenues[:5]

    # Tổng hợp những hàng hóa đang có trong cửa hàng mà sắp hết hạn sử dụng (hạn sử
    # dụng còn 6 tuần) rồi tính giá mới cho các mặt hàng đó: hàng có hạn sử dụng từ 3
    # tuần giảm 23.5%, hàng có hạn sử dụng dưới 3 tuần giảm 56.9%.
    pass

    # Thêm mới hóa đơn
    pass

    # Hiển thị danh sách hàng hóa
    pass

    # Xóa hàng hóa
    pass
