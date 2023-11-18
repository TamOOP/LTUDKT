import math
import datetime
import Models
import ManageProduct


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

    choice = enter_type_number(msg_choice)
    while choice < 0 or choice > len(func):
        print("Không hợp lệ")
        choice = enter_type_number(msg_choice)

    if choice != 0:
        func[choice]["exe"]()


# Thêm mới hàng hóa
def add_new_product():
    pass


# Tìm kiếm hàng hóa
def search_product():

    pass


# Sửa thông tin hàng hóa
def show_all_product():
    pass


# Sắp xếp theo doanh thu hàng hóa ( cao xuống thấp, thấp lên cao )
def sort_product_revenue():
    pass


# Thống kê doanh thu theo ngày của cửa hàng
def store_revenue():
    pass


# Thống kê top hàng hóa có doanh thu cao nhất, doanh thu thấp nhất
def listed_highest_and_lowest_product_revenue():
    pass


# Hiển thị hàng hóa sắp hết hạn
def product_nearly_expire():
    pass


# Bán hàng
def order():
    pass


# Xóa hàng hóa
def delete_product():
    pass


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
            "display": "Thống kê doanh thu theo ngày của cửa hàng",
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
        }

    }

    msg_choice = "Chọn chức năng (1- {}) (0 để thoát): ".format(len(func))
    enter_funtion_selection()