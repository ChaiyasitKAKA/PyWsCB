import re
import os


def showoption():
    print("1.สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล.txt")
    print("2.เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
    print("3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
    print("4.เลือกวิชาและลบไฟล์")
    print("0.จบการทำงาน")

def get_choice():
    while True:
        try:
            print("เลือกการทำงาน ")
            choice = int(input("เลือกเมนู:"))
            if 0 <= choice <= 5:
                return choice
            else :
                print("ไม่มีตัวเลือก")
        except ValueError:
            print("ใส่ได้แต่ตัวเลข")
        
        finally:
            try:
                input("กด Enter เพื่อยืนยัน")
            except SyntaxError:
                pass
def checkResault(totalscore):
    if totalscore >= 50:
        return"ผ่าน"
    else:
        return"ไม่ผ่าน"

def option1():
    while True:  
        try:
            file_name = (input("ชื่อวิชา(ภาษาอังกฤษ):"))
            id_name = (input("ชื่อ-นามสกุล: "))
            point_frist = float(input("ป้อนคะแนนสอบกลางภาค: "))
            pointl_half = float(input("ป้อนคะแนนสอบปลายภาค: "))
            point_gpa = float(input("ป้อนคะแนนเก็บ: "))
        
            #re.match บังคับใช้ตัวอักษร
            if re.match("^[a-zA-Z0-9]+$",file_name):
                break
            else :
                print("เขียนชื่อวิชาเป็นภาษาอังกฤษ")

        except ValueError:
            print("ป้อนตัวเลข")
   
    file_name += ".txt"
    totalscore = point_gpa+point_frist+pointl_half
    resault = checkResault(totalscore)

    with open(file_name, "w", encoding="utf-8") as f_dti:
        f_dti.write(f"วิชา:{file_name}\n")
        f_dti.write(f"ชื่อ-นามสกุล:{id_name}\n")
        f_dti.write(f"คะแนนสอบปลายภาค:{point_frist}\n")
        f_dti.write(f"คะแนนสอบกลางภาค:{pointl_half}\n")            
        f_dti.write(f"คะแนนเก็บ:{point_gpa}\n")
        f_dti.write(f"คะแนนรวม:{totalscore} = {resault}\n")
        print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")        


def option2():
    file_list = [f for f in os.listdir() if f.endswith(".txt")]
    if not file_list:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
        return
    
    print("ไฟล์ทั้งหมด")
    for i, file in enumerate(file_list,):
        print(f"{i}.{file}")
    selected_file_name = input("เลือกไฟล์ที่ต้องการ (ใส่ชื่อไฟล์.txt): ")
    if selected_file_name not in file_list:
        print("คุณพิมพ์ชื่อไฟล์ผิด")      
        return
    
    selected_file = selected_file_name  
    with open(selected_file, "a", encoding="utf-8") as f_dti:
        try:
            id_name = input("ชื่อ-นามสกุล: ")
            point_frist = float(input("ป้อนคะแนนสอบกลางภาค: "))
            pointl_half = float(input("ป้อนคะแนนสอบปลายภาค: "))
            point_gpa = float(input("ป้อนคะแนนเก็บ: "))

            totalscore = point_frist + pointl_half + point_gpa
            result = checkResault(totalscore)

            f_dti.write(f"ชื่อ-นามสกุล: {id_name}\n")
            f_dti.write(f"คะแนนสอบปลายภาค: {point_frist}\n")
            f_dti.write(f"คะแนนสอบกลางภาค: {pointl_half}\n")
            f_dti.write(f"คะแนนเก็บ: {point_gpa}\n")
            f_dti.write(f"คะแนนรวม: {totalscore} = {result}\n")
            print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
        except ValueError:
             print("ป้อนข้อมูลไม่ถูกต้อง")
    
def option3():
    file_list = [f for f in os.listdir() if f.endswith(".txt")]
    if not file_list:
        print("ไม่มีไฟล์วิชาใดๆอยู่เลย")
        return

    print("ไฟล์ทั้งหมด")
    for i, file in enumerate(file_list, start=1):
        print(f"{i}. {file}")

    selected_file_name = input("เลือกไฟล์ที่ต้องการ (ใส่ชื่อไฟล์.txt): ")

    if selected_file_name not in file_list:
        print("ไม่พบไฟล์ที่ระบุ") 
        return

    selected_file = selected_file_name
    with open(selected_file, "r", encoding="utf-8") as f_dti:
        data = f_dti.read()
        print("ข้อมูลในไฟล์:")
        print(data)
    
def option4():
    file_list = [f for f in os.listdir() if f.endswith(".txt")]
    if not file_list:
        print("ไม่มีไฟล์วิชาใดๆอยู่เลย")
        return

    print("ไฟล์ทั้งหมด")
    for i, file in enumerate(file_list, start=1):
        print(f"{i}. {file}")

    selected_file_name = input("เลือกไฟล์ที่ต้องการลบ (ใส่ชื่อไฟล์.txt): ")
    
    if selected_file_name not in file_list:
        print("ไม่พบไฟล์ที่ระบุ")  # Provide a clear message for file not found
        return

    selected_file = selected_file_name

    try:
        os.remove(selected_file)
        print("ลบไฟล์เรียบร้อยแล้ว")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการลบไฟล์: {e}")

    
print("|[][][][][][][][][][][][][][]|")
print("|----- Student profile  -----|")
print("|____________________________|")

showoption()
choice = get_choice()

if choice == 1:
    option1()
elif choice == 2:
    option2()
elif choice == 3:
    option3()
elif choice == 4:
    option4()
elif choice == 0:
    print("จบการทำงาน")
else:
    print("ไม่รู้จักตัวเลือกนี้")
   