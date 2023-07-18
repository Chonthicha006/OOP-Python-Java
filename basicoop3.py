#ฟังก์ชันเสริม

class Employee:#การสร้างclass
 
    
     def __init__(self,name,salary,department): #จะถูกเรียกใช้งานพร้อมกับตอนเริ่มต้นที่เราสร้าง Object ขึ้นมา ส่วนตัวอื่น ๆ จะถูกเรียกทำงานหลังสร้าง Object
         self.name=name          #self.name เป็นการบอกว่าส่วนนี้คือ Attribute            
         self.salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
         self.department=department
        
         
         
     def  showdata(self): #กำหนดรายละเอียดผ่าน Method => detail โดยสร้าง Method ขึ้นมาใหม่
         print("Name={}".format(self.name)) #print name,salary ที่กำหนดเข้าไปใน object แต่ละตัวออกมาอีกที
         print("Salary={}".format(self.salary))      #เรียกใช้งาน Method 
         print("Department={}".format(self.department))
         
     
#การเรียกใช้งานclass โดยการสร้างObject
obj1=Employee("A",50000,"วิศวกร")
#Edit data
obj1.salary=55000

obj2=Employee("B",40000,"ผู้จัดการ")
obj3=Employee("C",35000,"ครู")


print(isinstance(obj1,Employee)) #ตรวจสอบว่า obj1 ถูกสร้างจากคลาส Employee รึเปล่า
print(isinstance(obj1,int)) #ตรวจสอบว่า obj1 ถูกสร้างจากคลาส int รึเปล่า

print(dir(obj1)) #dir มี Method, Attributeอะไรบ้างให้ใช้งาน
print(obj1.__class__) # Object ถูกสร้างมาจาก Class อะไร
