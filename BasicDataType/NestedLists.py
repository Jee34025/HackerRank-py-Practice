if __name__ == '__main__':
    students = [] # สร้าง list เก็บชื่อและคะแนนนักเรียน
    n = int(input())

    for i in range(n):
        name = input()
        score = float(input())
        students.append([name,score])
    
    # แยก list ของ score
    students_score = sorted(set([score for name,score in students]))
    second_score = students_score[1] # เลือกคะแนนอันดับสอง
    # แยกลิสต์ของ name และแมชต์ name ที่มี score เป็นอันดับสอง
    name_second = sorted(set([name for name,score in students if score == second_score]))


    '''
    name_second = []
    for name,score in students :
        if score == second_score :
            name_second.append(name)     
    '''


    print("\n".join(sorted(name_second)))
    