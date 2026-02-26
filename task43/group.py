class GroupLimitError(Exception):
    pass


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