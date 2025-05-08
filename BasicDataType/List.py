if __name__ == '__main__':
    n = int(input())
    l = []
    
    for i in range(n) :
        command = input().strip().split(" ") #รับคำสั่งว่าจะทำอะไร
        cmd = command[0] # เก็บคำสั่งไว้ที่ index 0
        
        if cmd == "print" :
            print(l)
        elif cmd == "insert" :
            in_dex = int(command[1]) #รับข้อมูล index ไว้ที่ index 1
            val = int(command[2]) #รับค่าที่ต้องการใส่ในลิสต์ ไว้ที่ index 2
            l.insert(in_dex,val)
        elif cmd == "remove" :
            val = int(command[1])
            l.remove(val)
        elif cmd == "append" :
            val = int(command[1])
            l.append(val)
        elif cmd == "sort" :
            l.sort()
        elif cmd == "pop" :
            l.pop()
        elif cmd == "reverse" :
            l.reverse()