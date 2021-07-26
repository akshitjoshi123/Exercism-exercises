class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        return sorted(self.students, key = lambda x : (self.students.get(x), x))

    def grade(self, grade_number):
        return sorted([ s for s in self.students if self.students[s] == grade_number ])
