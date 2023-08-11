#Encapsulation
#Private
#instance variable

class Employee:
     
    #Private Method
    def __init__(self,name,salary,department): #Constructor or  Method #จะถูกเรียกใช้งานพร้อมกับตอนเริ่มต้นที่เราสร้าง Object ขึ้นมา ส่วนตัวอื่น ๆ จะถูกเรียกทำงานหลังสร้าง Object
                                                    #Public Attribute
                                                        #  self._name=name          #self.name เป็นการบอกว่าส่วนนี้คือ Attribute            
                                                        #  self._salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
                                                        #  self._department=department
        #ถ้าเป็น Private จะมี_ _ 2 ตัว
         self.__name=name              
         self.__salary=salary #อ้างอิงตามพารามิเตอร์salaryที่เราส่งเข้ามา
         self.__department=department  
   
    #ถ้าเป็น Private จะมี_ _ 2 ตัว
    def _showdata(self): #กำหนดรายละเอียดผ่าน Method => detail โดยสร้าง Method ขึ้นมาใหม่
         print("Name= "+self.__name) #print name,salary ที่กำหนดเข้าไปใน object แต่ละตัวออกมาอีกที
         print("Salary= "+str(self.__salary))    
        #  print("Salary={}".format(self.__salary))         
        #  print("Salary= ",format(self.__salary))      
         print("Department= "+self.__department)
         
    #setter method          #ทำการแก้ไขข้อมูล โดยระบุรูปแบบการกระทำผ่านตัว Method 
    def setName(self,newname):     #newnameชื่อใหม่
         self.__name=newname    
    def setSalary(self,newsalary):
         self.__salary=newsalary     
    def setDepartment(self,newdepartment):
         self.__department=newdepartment
         
     #getter Method ดึงค่าไปใช้งาน
     
    def getName(self):
          return self.__name
    def getSalary(self):
          return self.__salary
    def getDepartment(self):
          return self.__department
     

         
         
#การเรียกใช้งานclass โดยการสร้างObject
obj1=Employee("A",50000,"วิศวกร")
#obj1.__salary=27000 #แก้ไม่ได้ เพราะ private นอกจากจะใช้ setter method
obj1.setSalary(27000)
obj1.setName("AAA")
print("ชื่อ= ",format(obj1.getName()))
print("ตำแหน่ง = ",format(obj1.getDepartment()))   
print("เงินเดือน= ",format(obj1.getSalary()))     



# obj1._showdata()
# print(obj1._name) 
# obj2=Employee("B",40000,"ผู้จัดการ")
# obj3=Employee("C",35000,"ครู")
# print(isinstance(obj1,Employee)) #ตรวจสอบว่า obj1 ถูกสร้างจากคลาส Employee รึเปล่า
# print(isinstance(obj1,int)) #ตรวจสอบว่า obj1 ถูกสร้างจากคลาส int รึเปล่า
# print(dir(obj1)) #dir มี Method, Attributeอะไรบ้างให้ใช้งาน
# print(obj1.__class__) # Object ถูกสร้างมาจาก Class อะไร
