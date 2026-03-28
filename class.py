class Student:
    name = "Parth Kale"

    def __init__(self, name, address, cgpa):
        print("adding new student:")
        self.name = name
        self.address = address
        self.cgpa = cgpa


# object creation
s1 = Student("Parth kale", "Sambhajinagar", 8.55)
s2 = Student("neeraj","gwalior",8.01)
s3 = Student("aniruddha","jodhpur",8.2)

print(s1.name,s2.name)
print(s2.address,s3.address)
print(s1.cgpa,s3.cgpa)