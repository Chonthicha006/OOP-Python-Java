#การสร้าง  Constructor คำสั่งจะถูกทำงานเมื่อสร้างObject ขึ้นมา มีเรียกใช้งานClass=> Employee ซึ่งคำสั่งที่อยู่ในConstructor ไม่จำเป็นต้องเขียนก็ได้
# ในกรณีที่ต้องเขียนก็คือ เราสร้าง Object ขึ้นมาแล้วอยากให้ทำอะไร


class Employee:#การสร้างclass
    # def __init__(self): #จะถูกเรียกใช้งานพร้อมกับตอนเริ่มต้นที่เราสร้าง Object ขึ้นมา ส่วนตัวอื่น ๆ จะถูกเรียกทำงานหลังสร้าง Object
    #      print("Default Constructor")
    #ไม่มีการส่งค่าเข้ามา
    
    #สร้าง Object และกำหนดรายละเอียดในครั้งเดียว
     def __init__(self,name,salary,department): #จะถูกเรียกใช้งานพร้อมกับตอนเริ่มต้นที่เราสร้าง Object ขึ้นมา ส่วนตัวอื่น ๆ จะถูกเรียกทำงานหลังสร้าง Object
         self.name=name          #self.name เป็นการบอกว่าส่วนนี้คือ Attribute            
         self.salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
         self.department=department
        
         
         
     def  showdata(self): #กำหนดรายละเอียดผ่าน Method => detail โดยสร้าง Method ขึ้นมาใหม่
         print("Name={}".format(self.name)) #print name,salary ที่กำหนดเข้าไปใน object แต่ละตัวออกมาอีกที
         print("Salary={}".format(self.salary))      #เรียกใช้งาน Method 
         print("Department={}".format(self.department))
         
     def __del__(self): #ทุกครั้งที่สร้าง Object ขึ้นมา พอสร้างเสร็จ แล้วจะทำงานหลังที่สิ้นสุดการเรียกใช้งาน Class=>Emplyee 
        #ตัวDestructorจะถูกเรียกใช้งาน ซึ่งคำสั่งที่จะระบุในนั้นจะเป็นเรื่องของการคืนค่าในหน่วยความจำให้กับตัวระบบ Clear Ram,Tempt
         print("Call Destructor")  
         ###บางภาษามีระบบที่คอย Clear Memory คืนค่าหน่วยความจำให้กับระบบอัตโนมัติ บางภาษาต้องเขียนเอง ส่วนใหญ่เขียนในรูปแบบDestructure ถ้าแบบรูปแบบของOOP
         
#การเรียกใช้งานclass โดยการสร้างObject
obj1=Employee("A",50000,"วิศวกร")
#Edit data
obj1.salary=55000

obj2=Employee("B",40000,"ผู้จัดการ")
obj3=Employee("C",35000,"ครู")


obj1.showdata()
obj2.showdata()
obj3.showdata()


