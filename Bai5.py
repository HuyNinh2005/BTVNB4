n = int(input("Nhập số lượng phần tử: "))
 
a = [input("Nhập phần tử thứ {}: ".format(i + 1)) for i in range(n)]

b = tuple(a)
print("Tuple b: ", b)

def demSO(s):
    return s.isdigit()
count_Number = sum(1 for i in b if demSO(i))

print("Số phần tử có dạng số là: ", count_Number)