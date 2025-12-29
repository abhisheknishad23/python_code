class Student:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
Student1 =Student()
Student1.set_name("Abhishek")
print(Student1.get_name())

Student2 = Student()
Student2.set_name("kumar")
print(Student2.get_name())