def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
number = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(number)
print("Dãy số được nhập vào là:", number)
print("Tuple được tạo là:", my_tuple)
