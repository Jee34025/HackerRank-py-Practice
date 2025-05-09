if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ar = [
            [i,j,k] # สร้าง list เก็บ ตัวแปร

            # loop i j k เก็บไว้ใน list
            for i in range(x+1) 
            for j in range(y+1)
            for k in range(z+1)
            if i + j + k != n # ใส่เงื่อนไขลบ list ที่ผลรวมมีค่าเท่ากับ n ออกไป
        ]
    print(ar)