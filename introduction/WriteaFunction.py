def is_leap(year) :  
    # เซ็ตค่าเริ่มต้น
    leap = False

    #เ ซ็ตเงื่อนไขของ leap year
    if year%4 == 0 : # หาร 4 ลงตัว
        if year%100 == 0 : # หาร 100 ลงตัว
            if year%400 == 0 : # หาร 400 ลงตัว
                leap = True
        else : # หาร 4 ลงตัว หาร 100 ไม่ลงตัว
            leap = True

    return leap # ค่าอื่นๆนอกจากเงื่อนไขเป็น false
year = int(input())
print(is_leap(year))
