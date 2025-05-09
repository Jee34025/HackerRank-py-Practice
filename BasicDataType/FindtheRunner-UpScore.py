if __name__ == '__main__':
    n = int(input())
    l = input()

    # จัดข้อมูลให้เป็น list ออกมาด้วย strip split
    # เปลี่ยนข้อมูลให้เป็น integer ด้วย map
    # ลบค่าซ้ำด้วย set
    # เรียงข้อมูลด้วย sorted
    result = sorted(set(map(int, l.strip().split())))

    # แสดงผลข้อมูลใน index รองสุดท้าย จะได้ second top score
    print(result[-2])

    
        
