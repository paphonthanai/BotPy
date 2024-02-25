list_a = [28, 14, 13, 21, 19, 27, 23, 30, 16, 3]  # สร้าง list_a เปล่าเพื่อเก็บค่า input

# ใช้วงวน while เพื่อรับค่า input จนกว่าจะพบค่าว่าง
# while True:
#     value = input("Press Enter to stop): ")
#     if value == "":
#         break  # หยุดการทำงานเมื่อพบค่าว่าง
#     else:
#         list_a.append(value)  # เพิ่มค่า input เข้าไปใน list_a
        
def median_of_median(arr):
    
     # หาค่ามัธยฐานของ list ที่มีความยาว 2 โดยหาค่าเฉลี่ยของทั้งสอง element
    if len(list_a) == 2:
        return sum(list_a) / 2
    
    # หาค่ามัธยฐานของ list ที่มีความยาว 1 โดยใช้ค่าตัวเดียวกัน
    if len(list_a) == 1:
        return list_a[0]
    
    sublists = []  # เตรียม list เก็บ sublist
    sublist = [] # เตรียม list เก็บ sublistที่ย่อยลงมาอีกที
    newSublists = []
    medians = []  # เตรียม list เก็บค่ามัธยฐานของแต่ละ sublist
    sublist_size = len(list_a) // 3  # ดของ sublist แต่ละชุด (3)
    remainder = len(list_a) % 3  # คำนวณเศษที่เหลือจากการแบ่ง (1)
    
    start = 0  # เริ่มต้น index ของ sublist
    
    for i in range(3):  # วน loop 3 ครั้งเพื่อสร้าง sublist ทั้งหมด
        sublist_end = start + sublist_size  # คำนวณ index สิ้นสุดของ sublist
        if i == 2:  # ถ้าเป็น sublist สุดท้าย
            sublist_end += remainder  # เพิ่มเศษไปยัง sublist สุดท้าย

        sublist = list_a[start:sublist_end] # ดึง sublist จาก list_a โดยใช้ slicing
        sublists.append(sublist)  # เพิ่ม sublist เข้าไปใน sublists
        start = sublist_end  # เปลี่ยนค่า start เป็น sublist_end เพื่อใช้สร้าง sublist ถัดไป
        
    # print("sublists", sublists)  

    for sublist in sublists:  # วนลูปเพื่อเรียงลำดับ sublist ใน sublists ด้วย Bubble Sort
        if len(sublist) <= 4:  # กรณี sublist มีความยาวไม่เกิน 4
            for i in range(len(sublist) - 1): 
                for j in range(len(sublist) - 1 - i):
                    if sublist[j] > sublist[j + 1]:
                        sublist[j], sublist[j + 1] = sublist[j + 1], sublist[j]
        else:  # กรณี sublist มีความยาวมากกว่า 4
            if len(sublist) > 4:  # ตรวจสอบว่า sublist มีความยาวมากกว่า 4 หรือไม่
                for i in range(len(sublist)): 
                    for j in range(len(sublist) - 1): 
                        if sublist[i] != sublist[j]:
                            if sublist[i] > sublist[j] and sublist[i] > sublist[j + 1]:
                                sublist[j], sublist[j] = sublist[i], sublist[j]  # สลับค่าให้มากที่สุดมาอยู่ด้านหลัง
        # newSublists.append(sublist)
        
    # ถ้า sublist มีความยาวน้อยกว่าหรือเท่ากับ 4 ให้เพิ่ม sublist เข้าไปใน list ใหม่โดยไม่มีการปรับแต่ง
    for sublist in sublists:
        if len(sublist) >= 4:  # ตรวจสอบว่า sublist มีความยาวมากกว่า 4 หรือไม่
                for i in range(len(sublist)): 
                    for j in range(len(sublist) - 1): 
                        if sublist[i] != sublist[j]:
                            if sublist[i] > sublist[j] and sublist[i] > sublist[j + 1]:
                                sublist[j], sublist[j] = sublist[i], sublist[j]  # สลับค่าให้มากที่สุดมาอยู่ด้านหลัง
                # หาค่าที่น้อยที่สุด 2 ตัวแล้วนำมาบวกกัน
                min1 = min(sublist)
                sublist.remove(min1)
                min2 = min(sublist)
                sublist.remove(min2)
                sublist_avg = (min1 + min2) / 2  # หาค่าเฉลี่ยของค่าที่น้อยที่สุด 2 ตัว
                sublist.insert(0, sublist_avg)  # เพิ่มค่าเฉลี่ยเข้าไปใน list ใหม่
                newSublists.append(sublist)
        else:
            newSublists.append(sublist)
    
    # print("newSublists", newSublists)
    
    for medianList in newSublists:
        # print(medianList)
        medians.append(medianList[1])  # เพิ่มค่ามัธยฐานเข้าไปใน medians
    
    
    return float(medians[1])
    
       
    # เอา sublist มาใช้งาน

    # หาค่ามัธยฐานของ medians
    
    
    # return median_of_median()

print("Input:", list_a)
print("Output:", median_of_median(list_a))  # แสดงผลลัพธ์
