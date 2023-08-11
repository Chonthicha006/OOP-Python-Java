#Encapsulation
#Private
#instance variable

class Employee:
    #class variable ไม่จำเป็นต้องสร้างก้อน object ขึ้นมาก็สามารถเข้าถึงได้ ต้องระบุในรูปแบบ public , protected 
    _minSalary = 13000
    _maxSalary = 70000
    _companyName = "SIN X"
    #private
    __CEO="Mr.John"
    #Private Method
    def __init__(self,name,salary,department): #Constructor or  Method #จะถูกเรียกใช้งานพร้อมกับตอนเริ่มต้นที่เราสร้าง Object ขึ้นมา ส่วนตัวอื่น ๆ จะถูกเรียกทำงานหลังสร้าง Object
        #instance variable    ตัวเเปรของobject                                      
         self.__name=name              
         self.__salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
         self.__department=department  
   
        #ถ้าเป็น Private จะมี_ _ 2 ตัว
    def _showdata(self): #กำหนดรายละเอียดผ่าน Method => detail โดยสร้าง Method ขึ้นมาใหม่
         print("Name= "+self.__name) 
         print("Salary= ",format(self.__salary))    #or   print("Salary= {}".format(self.__salary)) 
         print("Department= "+self.__department)


obj1=Employee("A",50000,"วิศวกร")
#อ้างอิงไปที่class แล้วเข้าถึงตัวแปรได้เลย+++
print("เงินเดือนต่ำสุดของพนักงาน = "+str(Employee._minSalary)) #แปลงให้เป็นstring
print("Company Name : ")
print(Employee._companyName)

#Prvate ไม่สามารถเเสดงผลได้
print(Employee.__CEO)


