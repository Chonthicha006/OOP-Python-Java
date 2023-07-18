 #ชื่อ , เงินเดือน 

class Employee:#การสร้างclass
    #สร้างMethod   #วิธีเปลี่ยนชื่อคือ ส่งพารามิเตอร์เข้าไปใน Method => detail
     def detail(self,name,salary,department):     #ถ้าเป็นการเขียนโปรเเกรมทั่วไปเรียกว่า  ฟังก์ชัน ถ้าเขียนโปรเเกรมเชิงวัตถุจะเรียกว่า Method #ใส่self เพื่อให้รู้ว่าคือ Method/Behavier 
       #กำหนด Attribute ผ่าน keyword => self       nameคือ ชื่อAttribute
         self.name=name          #self.name เป็นการบอกว่าส่วนนี้คือ Attribute            
         self.salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
         self.department=department
        #  print("Name={}".format(self.name)) #print name,salary ที่กำหนดเข้าไปใน object แต่ละตัวออกมาอีกที
        #  print("Salary={}".format(self.salary))      #เรียกใช้งาน Method 
        #  print("Department={}".format(self.department))
        
         
         
     def  showdata(self): #กำหนดรายละเอียดผ่าน Method => detail โดยสร้าง Method ขึ้นมาใหม่
         print("Name={}".format(self.name)) #print name,salary ที่กำหนดเข้าไปใน object แต่ละตัวออกมาอีกที
         print("Salary={}".format(self.salary))      #เรียกใช้งาน Method 
         print("Department={}".format(self.department))
         
         
#การเรียกใช้งานclass โดยการสร้างObject
obj1 = Employee()
obj1.detail("A",50000,"วิศวกร")

obj2=Employee()
obj2.detail("B",40000,"ผู้จัดการ")

obj3=Employee()
obj3.detail("C",35000,"ครู")
#กำหนดชื่อattribute(คุณลักษณะ)

obj1.showdata()
obj2.showdata()
obj3.showdata()
