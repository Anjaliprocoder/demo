#real world entity is an object and it have ts own properties and methods.
#class-blueprint for creating an object-object constructor, keyword is class
#syntax-class classname:

class classname:
    x=20
a=classname()
print(a.x)

#built in functions are __init__()[used  when a class is initiated for assigning values into object properties or operations]
#self(a parameter used for accessing variables at that instance , for representing the current instance of a class when it is created.

class person:
    def __init__(self,name,age):
        self.name=name#self.any other variable can be used
        self.age=age
a=person("anju",24)
print(a.name)
print(a.age)

#functions inside class is methods        
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print("my name is",self.name ,"my age is",self.age)
a=person("anjali",24)
a.fun()


#basic concepts of oops are class,inheritance,polymorphism,data encapsulation and data abstraction
#properties or methods of one class are inherited to another class - parent class(from where it is inherited) and child/derived class(to which it is)
#types of inheritance - single inheritance[one parent and one child],multiple inheritance[multiple parent class and one child class]
# ,multilevel inheritance[one child class is again inherited to another child class,hierarchical inheritance-one parent class and more than one child
#,hybrid inheritance-combination of inheritances.]

#inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print("my name is",self.name ,"my age is",self.age)
class child(person):
    pass
a=child("anju",17)
a.fun()

#polymorphisms-same named methods,functions and operators are executed in different object or class.
#function polymorphism-len(),type()-same function name

#encapsulation-within the unit to which the data is bind,protect-it increases readability

#abstraction-essential are hide after its usage

#method overloading-same class uses same named methods-last method only work
#method overriding-different class same methods
#operator overloading-same operators can be used in different objects-eg : "+" in integer and string     
     
         