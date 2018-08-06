# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:45:16 2018

@author: SilverDoe
"""

#========= Inheritance ========================================================
class Person:
    def display(self):
        print("from parent")

class Student(Person):
    pass

issubclass(Student,Person)
obj = Student()
obj.display()


#========== Single Inheritance ================================================
x=0
class Person:
    def __init__(self):
        global x
        x+=1
        print('I am a person')
        
class Student(Person):
    def __init__(self):
        #super().__init__()
        global x
        x +=2
        print('I am a student')
        

obj = Student()
print(x)
obj = Person()
print(x)

#=========== Multilevel Inheritance ===========================================

class A:
    x=1
class B(A):
    pass
class C(B):
    pass

cobj = C()
cobj.x



#============== Multiple Inheritance ==========================================

class A:
    pass

class B:
    pass

class C(A,B):
    pass

issubclass(C,A) and issubclass(C,B)


#============== Multiple Inheritance ==========================================

class A:
    name ='Peter'

class B:
    name = 'Wendy'

class C(A,B):
    pass
    #name = 'Hook'


nobj = C()
nobj.name
C.mro() # Method resolution order

#============= Hierarchical Inheritance =======================================

class A:
    pass

class B(A):
    pass

class C(A):
    pass

issubclass(B,A) and issubclass(C,A)


#============= Hybrid Inheritance =============================================

class A:
    x=1

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

dobj = D()
dobj.x


#============== Super function ================================================

class Vehicle : 
    def start(self):
        print('starting engine')
        
    def stop(self):
        print('stopping engine')
        
class TwoWheeler(Vehicle):
    def say(self):
        super().start()
        print('I have two wheels')
        super().stop()
        
        
tobj = TwoWheeler()
tobj.say()


#============ Method Overriding ===============================================

class A:
    def display(self):
        print('wake up at 6am')
        
class B(A):
    def display(self):
        print('wake up at 10am')
        
bobj = B()
bobj.display()


#=========== Method Overloading 1===============================================

class MyClass:
 
    def dispName(self, name=None):
 
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
 

obj = MyClass()

obj.dispName()
obj.dispName('Neverland')


#=========== Method Overloading 2===============================================

class MyClass:
 
    def dispName(self,dtype, name=None):
 
        if dtype is int:
            print('Number accepted')
        elif dtype is str:
            print('String accepted')
        
        else:
            print('unexpected type')
 

obj = MyClass()

obj.dispName(int,23)
obj.dispName(str,'Neverland')














































