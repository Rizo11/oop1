""" class My:
    #this is do string

    def __init__(self):
        self.name = "Name1"

    
    i = 12345

    def f(self):
        self.i = 0
        return 'hello world'
c = My()
print(c.name) """

""" class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

spark = Car("a", "b")
print(spark.name) """

""" class Student:
    #Student Class
    def __init__(self, id:int, name:str, birthday:str):
        self.id = id
        self.birthday = birthday
        Student.name = name
    
    def __str__(self):
        return "%d %s %s" % (self.id, self.name, self.birthday)
rizo = Student(1, "Mrizo", "123123")
print(rizo) """

""" class Math:
    #math functions

    PI = 3.1415

    @classmethod
    def pow(cls, a:int, b:int):
        return a**b

    @classmethod
    def area(cls, radius):
        return(cls.PI * Math.pow(radius, 2))

    def length(self, length:int):
        return length


print(Math.pow(2, 5))
print(Math.area(2))
l = Math()
print(l.length(12)) """



""" class Human:
    #Human Class

    def __init__(self, name = "Unknown", gender = "male", age = "0", phone = "0"):
        self.gender = gender
        self.name = name
        self.age = age
        self.phone = phone

class  Student(Human):
    #student class
    def __init__(self, name, gender, age, phone, id = "", faculty = ""):
        super().__init__(name=name, gender=gender, age=age, phone=phone)
        self.id = id
        self.faculty = faculty


eshmat = Student("Eshmat", "male", "17", "123123", "001", "Data Science")
odam = Human()
print(eshmat.name)
print(odam.name) """

class Student:
    def __init__(self, name):
        self._name = ""
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name
    
    name = property(get_name, set_name, del_name)


odil = Student("Odil")
print(odil._name)


odil._name = "Shuxrat"
print(odil._name)

odil.set_name("Jamshid")
print(odil._name)
    
odil.name = "Shuxrat"
print(odil.name)

del odil.name
print(odil._name)
    










