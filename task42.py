class GroupLimitError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years, {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, "
                f"{self.age} years, {self.gender}, "
                f"record book: {self.record_book}")

class Group:

    MAX_STUDENTS = 10   

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= Group.MAX_STUDENTS:
            raise GroupLimitError("У групі не може бути більше 10 студентів!")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += str(student) + "\n"
        return f"Group number: {self.number}\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1)
assert gr.find_student('Jobs2') is None
assert isinstance(gr.find_student('Jobs'), Student)

gr.delete_student('Taylor')
print("Після видалення Taylor:")
print(gr)

gr.delete_student('Taylor')  

for i in range(8):
    st = Student('Male', 20+i, f'Name{i}', f'Surname{i}', f'RB{i}')
    gr.add_student(st)

print("Додано 10 студентів")

try:
    extra = Student('Female', 22, 'Extra', 'Student', 'RB11')
    gr.add_student(extra)
except GroupLimitError as e:
    print("Помилка:", e)