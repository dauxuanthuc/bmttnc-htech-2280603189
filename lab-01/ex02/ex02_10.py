def dao_nguoc_chieu(chuoi):
    return chuoi[::-1]
int_string = input("Mời nhập vào chuỗi cần đổi ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chieu(int_string))