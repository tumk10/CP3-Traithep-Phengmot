userInput = input("Username:")
passwordInput = input(("Password:"))
mama = 5
banana = 6
pepsi = 17
lays = 5

if userInput == "Tumk" and passwordInput == "456789":
    print("เข้าระบบโปรแกรม")
    print("______________________")
    print("โปรดเลือกรายการสินค้า")
    print("1.มาม่า 5 บาท")
    print("2.กล้วยหอม 6 บาท")
    print("3.pepsi 17 บาท")
    print("4.เลย์ 5 บาท")
    li = input("ใส่รายการสินค้าเป็นตัวเลข: ")
    if li == "1":
        x = int(input("จำนวนสินค้า: "))
        y = mama * x
        print("มาม่า", mama, "*", x)
        print("ราคารวมทั้งสิ้น:", y, "บาท")
    elif li == "2":
        x = int(input("จำนวนสินค้า: "))
        y = banana * x
        print("กล้วยหอม", banana, "*", x)
        print("ราคารวมทั้งสิ้น:", y, "บาท")
    elif li == "3":
        x = int(input("จำนวนสินค้า: "))
        y = pepsi * x
        print("pepsi", pepsi, "*", x)
        print("ราคารวมทั้งสิ้น:", y, "บาท")
    elif li == "4":
        x = int(input("จำนวนสินค้า: "))
        y = lays * x
        print("เลย์", lays, "*", x)
        print("ราคารวมทั้งสิ้น:", y, "บาท")
    else:
        print("ไม่มีรายการสินค้าที่เลือก")

else:
    print("เข้าระบบไม่ได้ค่ะ")