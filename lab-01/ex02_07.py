print("nhap cac dong van ban(nham 'done' de ket thuc): ")
lines =[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    print("\ncac dong da nhap sau khi chuyen thanh in hoa: ")
    for line in lines:
        print(line.upper())