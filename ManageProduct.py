import Models
import datetime

# data sản phẩm
p1 = Models.Product(1, "product_demo", 20000, 8000, 10,
                    "18-11-2023", "1-12-2023")
p2 = Models.Product(2, "product_demo2product_demo2", 15000, 12000, 15,
                    "18-11-2023", "1-12-2023")

# data sản phẩm được mua
op1 = Models.OrderProduct(p1.get_pid(), p1.get_product_name(), 4, p1.get_product_price(),
                          4 * p1.get_product_price())
op2 = Models.OrderProduct(p2.get_pid(), p2.get_product_name(), 2, p2.get_product_price(),
                          2 * p2.get_product_price())

# data hóa đơn
r1 = Models.Receipt(1, datetime.datetime.now().strftime('%d-%m-%Y'), [op1],
                    int(op1.get_product_price()) * int(op1.get_order_quantity()))


def get_revenue(product):
    return product[1]


class ManageProduct:
    products, receipts = [], []

    def __init__(self):
        self.products.append(p1)
        self.products.append(p2)
        self.receipts.append(r1)

    # Thêm mới hàng hóa
    def them_moi_hang_hoa(self, product):
        self.products.append(product)

    # Tìm kiếm hàng hóa
    def tim_kiem_hang_hoa(self, pid):
        ket_qua = []
        for product in self.products:
            if product.pid == pid:
                ket_qua.append(product)
                return ket_qua
            else:
                print("Không tìm thấy ID hàng hóa nào có ID này.")
        return None

    # Sửa thông tin hàng hóa
    def sua_thong_tin_hang_hoa(self, pid):
        try:
            products = self.tim_kiem_hang_hoa(pid)

            if products is not None:
                # print("Thông tin hàng hóa cần sửa:")
                # print(product)
                for product in products:
                    product_name = input("Nhập tên hàng hóa mới (Nhấn Enter để giữ nguyên): ")
                    product_price = int(input("Nhập giá bán mới (Nhấn Enter để giữ nguyên): "))
                    product_cost = int(input("Nhập giá nhập mới (Nhấn Enter để giữ nguyên): "))
                    quantity = int(input("Nhập số lượng mới (Nhấn Enter để giữ nguyên): "))
                    production_date = datetime(input("Nhập ngày sản xuất mới (Nhấn Enter để giữ nguyên): "))
                    expiration_date = datetime(input("Nhập hạn sử dụng mới (Nhấn Enter để giữ nguyên): "))

                    product.sua_thong_tin(product_name, product_price, product_cost, quantity,
                                          production_date, expiration_date)
                    print(f"Đã sửa thông tin hàng hóa có mã {pid}")
            else:
                print(f"Không tìm thấy hàng hóa có mã {pid}")
        except ValueError:
            print("Lỗi: Dữ liệu không hợp lệ")

    # Sắp xếp tổng doanh thu từng mặt hàng(Dựa vào lựa chọn của người dùng: cao xuống thấp hay thấp lên cao)
    def sort_product_revenue(self, reverse: bool):
        _data_revenues = []
        for _product in self.products:
            _total = 0
            # duyet hoa don mua hang
            for _receipt in self.receipts:
                _list_order_product = _receipt.get_list_product()
                for order_product in _list_order_product:
                    if order_product.get_pid() == _product.get_pid():
                        _total += order_product.get_total_amount()

            # luu ten mat hang va tong doanh thu
            _product_revenue = [_product.get_product_name(), _total]
            _data_revenues.append(_product_revenue)

        # sap xep theo tong doanh thu
        _data_revenues.sort(key=get_revenue, reverse=reverse)
        return _data_revenues

    # Tính tổng doanh thu theo ngày từng mặt hàng
    pass

    # Tính tổng doanh thu theo ngày của cửa hàng(theo tháng, năm)
    pass

    # Hiển thị 5 mặt hàng có tổng doanh thu cao nhất, 5 mặt hàng có tổng doanh thu thấp nhất.
    def listed_highest_product_revenue(self):
        _data_revenues = ManageProduct.sort_product_revenue(self, True)
        return _data_revenues[:5]

    def listed_lowest_product_revenue(self):
        _data_revenues = ManageProduct.sort_product_revenue(self, False)
        return _data_revenues[:5]

    # Tổng hợp những hàng hóa đang có trong cửa hàng mà sắp hết hạn sử dụng (hạn sử
    # dụng còn 6 tuần) rồi tính giá mới cho các mặt hàng đó: hàng có hạn sử dụng từ 3
    # tuần giảm 23.5%, hàng có hạn sử dụng dưới 3 tuần giảm 56.9%.
    pass

    # Thêm mới hóa đơn
    pass

    # Hiển thị danh sách hàng hóa
    def hien_thi_danh_sach(self):
        for product in self.products:
            ManageProduct.hien_thi_thong_tin(product)

    @staticmethod
    def hien_thi_thong_tin(product):
        print(f"ID hàng hóa: {product.pid}")
        print(f"Tên hàng hóa: {product.product_name}")
        print(f"Giá bán hàng hóa: {product.product_price}")
        print(f"Giá nhập hàng hóa: {product.product_cost}")
        print(f"Số lượng: {product.quantity}")
        print(f"Ngày sản xuất: {product.production_date}")
        print(f"Hạn sử dụng: {product.expiration_date}")

    def thong_ke_doanh_thu_theo_ngay(self):
        doanh_thu_theo_ngay = {}
        for receipt in self.receipts:
            ngay_xuat = receipt.date_create
            if ngay_xuat not in doanh_thu_theo_ngay:
                doanh_thu_theo_ngay[ngay_xuat] = 0
            doanh_thu_theo_ngay[ngay_xuat] += receipt.total
        return doanh_thu_theo_ngay

    # Xóa hàng hóa
    def xoa_hang_hoa(self, pid):
        for product in self.products:
            if product.pid == pid:
                self.products.remove(pid)
                print(f"Hàng hóa có mã {pid} đã được xóa.")
                return
        print(f"Không tìm thấy hàng hóa có mã {pid}.")
