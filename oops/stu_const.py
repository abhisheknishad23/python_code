class student:
    def __init__(self, name, age, section):
        self.name=name
        self.age=age
        self.section=section

#creating object
student1 = student('abhishek',24,'A')
student2= student('kumar',25,'B')

print(student1.name, student1.age, student1.section)
print(student2.name, student2.age, student2.section)