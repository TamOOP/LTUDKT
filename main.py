import datetime
import Models
import ManageProduct

manageProduct = ManageProduct.ManageProduct()


# Nhập dữ liệu kiểu số
def enter_type_number(msg):
    while True:
        try:
            num = int(input(msg))
            if num < 0:
                print("Hãy nhập số > 0")
                num = int(input(msg))
            return num
        except:
            print("Hãy nhập ký tự số")


# Nhập dữ liệu kiểu datetime, format DD-MM-YYY
def enter_type_date(msg):
    while True:
        try:
            date_entry = input(msg + "(DD-MM-YYYY): ")
            day, month, year = map(int, date_entry.split('-'))
            return datetime.date(year, month, day)
        except:
            print("Không đúng định dạng")


# Nhập lựa chọn chức năng
def enter_funtion_selection():
    for i in range(1, len(func) + 1):
        print("{i}. {func}".format(
            i=i,
            func=func[i]["display"]
        ))
    print("{i}. {func}".format(
        i=0,
        func="Thoát chương trình"
    ))

    _choice = enter_type_number(msg_choice)
    while _choice < 0 or _choice > len(func):
        print("Không hợp lệ")
        _choice = enter_type_number(msg_choice)

    return _choice


# Thêm mới hàng hóa
def add_new_product():
    try:
        pid = enter_type_number("Nhập mã hàng hóa: ")
        product_name = input("Nhập tên hàng hóa: ")
        product_price = enter_type_number("Nhập giá bán: ")
        product_cost = enter_type_number("Nhập giá nhập: ")
        quantity = enter_type_number("Nhập số lượng: ")
        production_date = enter_type_date("Nhập ngày sản xuất: ")
        expiration_date = enter_type_date("Nhập hạn sử dụng: ")
        new_product = Models.Product(pid, product_name, product_price, product_cost, quantity, production_date,
                                     expiration_date)
        manageProduct.them_moi_hang_hoa(new_product)
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ.")


# Tìm kiếm hàng hóa
def search_product():
    try:
        pid_can_tim = enter_type_number("Nhập mã ID hàng hóa cần tìm: ")
        ket_qua_tim_kiem = manageProduct.tim_kiem_hang_hoa(pid_can_tim)
        if not ket_qua_tim_kiem:
            print("Không tìm thấy ID hàng hóa nào có ID này.")
        else:
            for product in ket_qua_tim_kiem:
                manageProduct.hien_thi_thong_tin(product)
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ")


# Sửa thông tin hàng hóa
def show_all_product():
    try:
        pid = enter_type_number("Nhập mã hàng hóa cần sửa thông tin: ")
        manageProduct.sua_thong_tin_hang_hoa(pid)
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ")


# Sắp xếp theo doanh thu hàng hóa ( cao xuống thấp, thấp lên cao )
# _reverse: True => cao xuống thấp, False => thấp lên cao
def sort_product_revenue():
    sort = {
        1: {
            "display": "Từ cao xuống thấp",
            "val": True
        },
        2: {
            "display": "Từ thấp lên cao",
            "val": False
        }
    }
    # hiển thị lựa chọn
    print("\nSắp xếp doanh thu hàng hóa")
    for i in range(1, len(sort) + 1):
        print("{}. {}".format(i, sort[i]["display"]))
    print("0. Quay lại")
    _choice = enter_type_number("Nhập lựa chọn(1-2) (0 để quay lại): ")

    if _choice != 0:
        print()
        _reverse = sort[_choice]["val"]
        # sắp xếp doanh thu
        _table_data = manageProduct.sort_product_revenue(_reverse)

        # hiển thị doanh thu theo tên
        for i in range(len(_table_data)):
            print("{name} \t {revenue}đ".format(
                name=_table_data[i][0],
                revenue=_table_data[i][1]
            ))
        print()


# Thống kê doanh thu theo ngày của cửa hàng
def store_revenue():
    # Gọi phương thức và lưu kết quả vào biến
    doanh_thu_theo_ngay, doanh_thu_tung_mat_hang = manageProduct.total_revenue_per_day_per_product()

    # Hiển thị tổng doanh thu theo ngày
    for ngay, doanh_thu in doanh_thu_theo_ngay.items():
        print(f"Doanh thu ngày {ngay}: {doanh_thu}")

    # Duyệt qua các mặt hàng và hiển thị doanh thu
    for pid, ngay_doanh_thu in doanh_thu_tung_mat_hang.items():
        for ngay, doanh_thu in ngay_doanh_thu.items():
            print(f"Doanh thu ngày {ngay} cho sản phẩm có mã {pid}: {doanh_thu}")

# Thống kê top hàng hóa có doanh thu cao nhất, doanh thu thấp nhất
def listed_highest_and_lowest_product_revenue():
    # 5 doanh thu cao nhat
    _highest = manageProduct.listed_highest_product_revenue()
    # 5 doanh thu thap nhat
    _lowest = manageProduct.listed_lowest_product_revenue()

    # hien thi doanh thu theo ten
    print("\n5 sản phẩm doanh thu cao nhất:")
    for i in range(len(_highest)):
        print("{name} \t {revenue}đ".format(
            name=_highest[i][0],
            revenue=_highest[i][1]
        ))

    print("\n5 sản phẩm doanh thu thấp nhất:")
    for i in range(len(_lowest)):
        print("{name} \t {revenue}đ".format(
            name=_lowest[i][0],
            revenue=_lowest[i][1]
        ))


# Hiển thị hàng hóa sắp hết hạn
def product_nearly_expire():
    _data_audit = manageProduct.audit_expiry_product()
    print("\nDanh sách sản phẩm sắp hết hạn:")
    for product in _data_audit:
        print(product)
    print()


# Bán hàng
def order():
    try:
        # Lấy thông tin chi tiết hóa đơn từ người dùng
        receipt_id = enter_type_number("Nhập mã hóa đơn: ")
        date_create = datetime.date.today()

        # Nhập thông tin các sản phẩm trong hóa đơn
        list_order_products = []
        while True:
            pid = enter_type_number("Nhập mã sản phẩm: ")
            quantity = enter_type_number("Nhập số lượng: ")

            # Tìm sản phẩm trong danh sách sản phẩm
            products = manageProduct.tim_kiem_hang_hoa(pid)

            if products:
                product = products[0]
                total_amount = quantity * product.get_product_price()
                list_order_products.append(Models.OrderProduct(pid, product.get_product_name(), quantity,
                                                               product.get_product_price(), total_amount))
            else:
                print(f"Không tìm thấy sản phẩm có mã {pid}")

            add_more = input("Thêm sản phẩm khác? (y/n): ")
            if add_more.lower() != 'y':
                break

        # Tạo đối tượng hóa đơn và thêm vào danh sách hóa đơn
        new_receipt = Models.Receipt(receipt_id, date_create.strftime('%d-%m-%Y'), list_order_products,
                                     sum(op.get_total_amount() for op in list_order_products))
        manageProduct.them_moi_hoa_don(new_receipt)
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ.")


# Xóa hàng hóa
def delete_product():
    try:
        id_hang_hoa_can_xoa = enter_type_number("Nhập ID hàng hóa cần xóa: ")
        manageProduct.xoa_hang_hoa(id_hang_hoa_can_xoa)
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ")


if __name__ == '__main__':
    func = {
        1: {
            "display": "Thêm mới hàng hóa",
            "exe": add_new_product
        },
        2: {
            "display": "Tìm kiếm hàng hóa",
            "exe": search_product
        },
        3: {
            "display": "Sửa thông tin hàng hóa",
            "exe": show_all_product
        },
        4: {
            "display": "Sắp xếp theo doanh thu hàng hóa",
            "exe": sort_product_revenue
        },
        5: {
            "display": "Thống kê doanh thu theo ngày và theo mặt hàng của cửa hàng",
            "exe": store_revenue
        },
        6: {
            "display": "Thống kê top hàng hóa có doanh thu cao nhất, doanh thu thấp nhất",
            "exe": listed_highest_and_lowest_product_revenue
        },
        7: {
            "display": "Hiển thị hàng hóa sắp hết hạn",
            "exe": product_nearly_expire
        },
        8: {
            "display": "Bán hàng",
            "exe": order
        },
        9: {
            "display": "Xóa hàng hóa",
            "exe": delete_product
        },
    }

    msg_choice = "Chọn chức năng (1- {}) (0 để thoát): ".format(len(func))
    choice = enter_funtion_selection()
    while choice != 0:
        func[choice]["exe"]()
        choice = enter_funtion_selection()
