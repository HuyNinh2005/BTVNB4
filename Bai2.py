setA = {"SV01", "SV02", "SV03", "SV04", "SV05"}
setB = {"SV04", "SV05", "SV07", "SV08", "SV09"}

set1 = setA.intersection(setB)
print(f"sinh viên đăng ký học tại cả hai bàn là: {set1}")

set2 = setA.union(setB)
print(f"danh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn là: {set2}")

set3 = setA.difference(setB)
print(f"danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2 là: {set3}")