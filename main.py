class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __average(self):
        self.mean = [grade for grades in self.grades.values() for grade in grades]
        if self.mean:
            self.midl_grade = (sum(self.mean) / len(self.mean))
            return self.midl_grade
        else:
            return "Нет оценок"

    def __str__(self):
        return ( f"Имя Студента : {self.name} \nФамилия Студента : {self.surname} \nСредний балл за ДЗ : {self.__average()} \nКурсы в процессе изучения :{self.courses_in_progress} \nЗавершенные курсы : {self.finished_courses} ")

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() == other.__average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() < other.__average

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average() > other.__average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __average(self):
        self.mean = [grade for grades in self.grades.values() for grade in grades]
        if self.mean:
            self.midl_grade = sum(self.mean) / len(self.mean)
            return self.midl_grade
        else:
            return "Нет оценок"

    def __str__(self):
        return (
            f"Имя Лектора : {self.name} \nФамилия Лектора : {self.surname} \nСредний балл : {self.__average()}")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() == other.__average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() < other.__average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average() > other.__average()

class Reviewer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname, )
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Имя и Фамилия Ревьюера : {self.name} {self.surname}"

Student1 = Student("Bob", "Tong", "man")
Student1.courses_in_progress += ["Python", "Git"]
Student1.finished_courses += ["Введение в программирование"]

Student2 = Student("Amy", "White", "woman")
Student2.courses_in_progress += ["Python", "Git"]
Student2.finished_courses += ["Введение в программирование"]

Reviewer1 = Reviewer("Bruce", "Ice")
Reviewer1.courses_attached += ["Введение в программирование", "Python", "Git"]
Reviewer2 = Reviewer("Tim", "Black")
Reviewer2.courses_attached += ["Введение в программирование", "Python", "Git"]

Reviewer1.rate_hw(Student2, "Введение в программирование", 7)
Reviewer1.rate_hw(Student2, "Введение в программирование", 9)
Reviewer1.rate_hw(Student2, "Введение в программирование", 6)

Reviewer1.rate_hw(Student1, "Введение в программирование", 10)
Reviewer1.rate_hw(Student1, "Введение в программирование", 8)
Reviewer1.rate_hw(Student1, "Введение в программирование", 10)

Reviewer2.rate_hw(Student2, "Python", 9)
Reviewer2.rate_hw(Student2, "Python", 9)
Reviewer2.rate_hw(Student2, "Python", 10)

Reviewer2.rate_hw(Student1, "Python", 8)
Reviewer2.rate_hw(Student1, "Python", 7)
Reviewer2.rate_hw(Student1, "Python", 10)

Lecturer1 = Lecturer("Albert", "Einschtein")
Lecturer1.courses_attached += ["Git", "Python"]

Student1.rate_lc(Lecturer1, "Git", 7)
Student1.rate_lc(Lecturer1, "Git", 7)
Student1.rate_lc(Lecturer1, "Git", 6)

Student2.rate_lc(Lecturer1, "Python", 10)
Student2.rate_lc(Lecturer1, "Python", 10)
Student2.rate_lc(Lecturer1, "Python", 10)

Lecturer2 = Lecturer("Mike", "Tyson")
Lecturer2.courses_attached += ["Git", "Python"]

Student1.rate_lc(Lecturer2, "Git", 9)
Student1.rate_lc(Lecturer2, "Git", 8)
Student1.rate_lc(Lecturer2, "Git", 10)

Student2.rate_lc(Lecturer2, "Python", 7)
Student2.rate_lc(Lecturer2, "Python", 5)
Student2.rate_lc(Lecturer2, "Python", 6)

print(f'Список студентов и средний бал за Домашнее задание : \n{Student1} \n{Student2}')
print()
print(f' Список Лекторов и средние оценки за лекцию : \n{Lecturer1} \n{Lecturer2}')
print()
print(f'Список проверяющих Домашние задания : \n{Reviewer1} \n{Reviewer2}')

Student_list = [Student1, Student2]
Lecturer_list = [Lecturer1, Lecturer2]

def course_m_grade_stud(Students_list, course):
    midl_grade = []
    for student in Students_list:
        if course in student.grades:
            midl_grade += student.grades[course]
    if midl_grade:
        return sum(midl_grade) / len(midl_grade)

def course_m_grade_lect(Lecture_list, course):
    midl_grade = []
    for lecturer in Lecture_list:
        if course in lecturer.grades:
            midl_grade += lecturer.grades[course]
    if midl_grade:
        return sum(midl_grade) / len(midl_grade)