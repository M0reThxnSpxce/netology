def average_grade(grades: dict):
    if grades:
        average_course_grade = []
        for grade_list in grades.values():
            average_course_grade.append(
                round(sum(grade_list) / len(grade_list), 1)
            )
        return sum(average_course_grade) / len(grades)
    else:
        return 0

def total_average_grade(person_list: list, course: str):
    result = 0
    qty = 0
    for person in person_list:
        if course in person.finished_courses:
            qty += 1
            result += average_grade(person.grades)
        elif course in person.courses_fixed:
            qty += 1
            result += average_grade(person.grades)
        elif course in person.courses_in_progress:
            qty += 1
            result += average_grade(person.grades)
    if qty > 0:
        return round(result/qty, 1)
    else:
        return 0

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_fixed = []
        self.grades = {}

class Student(Person):
    def __str__(self):
        print('Имя: ', self.name)
        print('Фамилия: ', self.surname)
        print('Средняя оценка за домашнее задание: ', average_grade(self.grades))
        print('Курсы в процессе обучения: ', self.courses_in_progress)
        print('Завершенные курсы: ', self.finished_courses)

    def lecturer_grades(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_fixed:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor(Person):
    pass

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print('Имя: ', self.name)
        print('Фамилия: ', self.surname)
        print('Средняя оценка за домашнее задание: ', average_grade(self.grades))
        print(' ')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        print('Имя: ', self.name)
        print('Фамилия: ', self.surname)
        print(' ')

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_fixed and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer_0 = Lecturer('Elena', 'Sokolova')
lecturer_0.courses_fixed += ['Python']

lecturer_1 = Lecturer('Vitaly', 'Levin')
lecturer_1.courses_fixed += ['Git']

student_0 = Student('Gennady', 'Markovin')
student_0.courses_in_progress += ['Python']
student_0.courses_in_progress += ['Git']
student_0.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Pavel', 'Antonov')
some_reviewer.courses_fixed += ['Python']
some_reviewer.courses_fixed += ['Git']

some_reviewer.rate_hw(student_0, 'Python', 10)
some_reviewer.rate_hw(student_0, 'Python', 7)
some_reviewer.rate_hw(student_0, 'Python', 6)
student_0.lecturer_grades(lecturer_0, 'Python', 10)
student_0.lecturer_grades(lecturer_0, 'Python', 7)
student_0.lecturer_grades(lecturer_0, 'Python', 6)

some_reviewer.rate_hw(student_0, 'Git', 10)
some_reviewer.rate_hw(student_0, 'Git', 10)
some_reviewer.rate_hw(student_0, 'Git', 10)
student_0.lecturer_grades(lecturer_1, 'Git', 10)
student_0.lecturer_grades(lecturer_1, 'Git', 10)
student_0.lecturer_grades(lecturer_1, 'Git', 10)

st_group = [student_0]
print('')
print('Средняя оценка студентов по курсу Python:', total_average_grade(st_group, 'Python'))
print('Средняя оценка студентов по курсу Git:', total_average_grade(st_group, 'Git'))

lec_group = [lecturer_0, lecturer_1]
print('Средняя оценка лекторов по курсу Python:', total_average_grade(lec_group, 'Python'))
print('Средняя оценка лекторов по курсу Git:', total_average_grade(lec_group, 'Git'))
print('')