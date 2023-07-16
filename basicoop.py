 #ชื่อ , เงินเดือน 

class Employee:#การสร้างclass
    #สร้างMethod
     def detail(self):                             #ถ้าเป็นการเขียนโปรเเกรมทั่วไปเรียกว่า  ฟังก์ชัน ถ้าเขียนโปรเเกรมเชิงวัตถุจะเรียกว่า Method #ใส่self เพื่อให้รู้ว่าคือ Method/Behavier 
         self.name="A"                             #กำหนด Attribute ผ่าน keyword => self nameคือชื่อ Attribute
         self.salary=20000
         print("Name={}".format(self.name))
         print("Salary={}".format(self.salary))      #เรียกใช้งาน Method 
         
#การเรียกใช้งานclass โดยการสร้างObject
emp1 = Employee()
emp1.detail()
#กำหนดชื่อattribute(คุณลักษณะ)
