# oop stands for object-oriented programing
# a clss is a blueprint of an object
# an object is an instance of a class
class Student:
# constructor method
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    # Member function
    def display(self):
        print(f"The Student's Name is:,{self.name},Age :,{self.age},with a Score of:,{self.score}")
# instance of the class(object)
myobj=Student("Kasudi",17,"A")
myobj.display()
myobj2=Student("Joy",17,"B")
myobj2.display()
myobj3=Student("Sharon",18,"A-")
myobj3.display()
myobj4=Student("Elias",19,"B")
myobj4.display()
myobj5=Student("Kesly",16,"B+")
myobj5.display()

# create a new file oop2 a class called cars make modelcolour as attributes in a constructor method
# then member function.... create five objects of the above
