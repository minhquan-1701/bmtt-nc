def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("nhap danh sach cac so")
numbers = list(map(int,input_list.split(',')))
my_tupel = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print("tupel tu list: ", my_tupel)