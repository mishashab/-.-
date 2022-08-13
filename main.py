import random

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if grade < 0 or grade > 10:
            return f'\"{grade}\" не является баллом в пределах от 1 до 10'
        elif isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return f'Студент не посещает курс {grade} или лектор не ведёт ' \
                   f'его, значит {self.name} не может поставить оценку'

    def avg_grade(self, inside_course = "empty"):
        if len(self.grades) == 0:
            return
        else:
            all_grades = []
            for course, course_grades in self.grades.items():
                if course == inside_course or inside_course == "empty":
                    all_grades += course_grades
            return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: ' \
               f'{", ".join([_ for _ in self.courses_in_progress])}\n' \
               f'Завершенные курсы: ' \
               f'{", ".join([_ for _ in self.finished_courses])}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        else:
            return self.avg_grade() < other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def avg_lecture_grade(self, inside_lecture = "empty"):
        if len(self.lectures_grades) == 0:
            return
        else:
            all_grades = []
            for lecture, lecture_grades in self.lectures_grades.items():
                if lecture == inside_lecture or inside_lecture == "empty":
                    all_grades += lecture_grades
            return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg_grade = self.avg_lecture_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grade}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        else:
            return self.avg_lecture_grade() < other.avg_lecture_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return f'Данный преподаватель не может проверить курс {course} ' \
                   f'у {student.name}'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Создание объектов класса
student1 = Student("Евгений", "Васильев", "мужской")
student2 = Student("Анна", "Васильева", "женский")
lecturer1 = Lecturer("Аглая", "Петрова")
lecturer2 = Lecturer("Виктор", "Фомин")
reviewer1 = Reviewer("Виктор", "Петров")
reviewer2 = Reviewer("Ангелина", "Ефремова")


# Проставление пройденных и проходимых курсов студентам
courses = ["Разработка компьютерных игр", "DevOps", "HTML-верстальщик",
           "Веб-программист PHP", "Английский язык"]

student1.finished_courses.append(courses[0])
student1.finished_courses.append(courses[1])
student1.courses_in_progress.append(courses[2])
student1.courses_in_progress.append(courses[3])

student2.finished_courses.append(courses[2])
student2.finished_courses.append(courses[0])
student2.courses_in_progress.append(courses[1])
student2.courses_in_progress.append(courses[3])
student2.courses_in_progress.append(courses[4])

reviewer1.courses_attached.append(courses[0])
reviewer1.courses_attached.append(courses[1])
reviewer1.courses_attached.append(courses[2])
reviewer2.courses_attached.append(courses[2])
reviewer2.courses_attached.append(courses[3])
reviewer2.courses_attached.append(courses[4])

lecturer1.courses_attached.append(courses[0])
lecturer1.courses_attached.append(courses[1])
lecturer1.courses_attached.append(courses[2])
lecturer2.courses_attached.append(courses[2])
lecturer2.courses_attached.append(courses[3])
lecturer2.courses_attached.append(courses[4])


#Так же при выполнении затргивается и режим исключений,
#когда нельзя оценивать за определённые курсы
for i in range(30):
    student1_mark = int(random.random() * 10 + 1)
    student1_course = random.choice(courses)

    reviewer1.rate_hw(student1, student1_course, student1_mark)

    student2_mark = int(random.random() * 10 + 1)
    student2_course = random.choice(courses)

    reviewer1.rate_hw(student2, student2_course, student2_mark)

    lecturer1_mark = int(random.random() * 10 + 1)
    lecturer1_course = random.choice(courses)
    student1.rate_lecture(lecturer1, lecturer1_course, lecturer1_mark)

    lecturer2_mark = int(random.random() * 10 + 1)
    lecturer2_course = random.choice(courses)
    student1.rate_lecture(lecturer2, lecturer2_course, lecturer2_mark)

    student1_mark = int(random.random() * 10 + 1)
    student1_course = random.choice(courses)

    reviewer2.rate_hw(student1, student1_course, student1_mark)

    student2_mark = int(random.random() * 10 + 1)
    student2_course = random.choice(courses)

    reviewer2.rate_hw(student2, student2_course, student2_mark)

    lecturer1_mark = int(random.random() * 10 + 1)
    lecturer1_course = random.choice(courses)
    student2.rate_lecture(lecturer1, lecturer1_course, lecturer1_mark)

    lecturer2_mark = int(random.random() * 10 + 1)
    lecturer2_course = random.choice(courses)
    student2.rate_lecture(lecturer2, lecturer2_course, lecturer2_mark)

# Проверка на заполняемость оценок
# print(student1.grades)
# print(student2.grades)
# print(lecturer1.lectures_grades)
# print(lecturer2.lectures_grades)

print('Работа функции __str__')
print('-' * 80)
print('-' * 80)
print(student1)
print('-' * 80)
print(student2)
print('-' * 80)
print(lecturer1)
print(print('-' * 80))
print(lecturer2)
print('-' * 80)
print(reviewer1)
print('-' * 80)
print(reviewer2)
print('-' * 80)
print('-' * 80)

print('Работа функции __lt__')
print('-' * 80)
print(f'Средний балл лектора {lecturer1.name}:{lecturer1.avg_lecture_grade()}')
print(f'Средний балл лектора {lecturer2.name}:{lecturer2.avg_lecture_grade()}')
print(f'Срдний балл лектора {lecturer1.name} больше среднего балла '
      f'лектора {lecturer2.name}: {lecturer1 > lecturer2}')
print('-' * 80)
print(f'Средний балл студента {student1.name}:{student1.avg_grade()}')
print(f'Средний балл студентки {student2.name}:{student2.avg_grade()}')
print(f'Срдний балл студента {student1.name} больше среднего балла '
      f'студентки {student2.name}: {student1 > student2}')
print('-' * 80)
print('-' * 80)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Задание 4
#def avg_grade_for_lection_on_the_course(students, course):

def avg_grade_for_hw_on_the_course(students, course):
    grades = []
    for student in students:
        try:
            grades += student.grades[course]
        except:
            1
    if len(grades) != 0:
        return round(sum(grades) / len(grades), 1)
    else:
        return f"Оценок по курсу не выставленно"


def avg_grade_for_lection_on_the_course(lectors, course):
    grades = []
    for lector in lectors:
        try:
            grades += lector.lectures_grades[course]
        except:
            1
    if len(grades) != 0:
        return round(sum(grades) / len(grades), 1)
    else:
        return f"Оценок по курсу не выставленно"


students_list = [student1, student2]
print(f"Оценки студентов по курсу {courses[3]}")
for student in students_list:
    try:
        print(student.name, student.grades[courses[3]])
    except:
        1

print(f'Средняя оценка по курсу: '
      f'{avg_grade_for_hw_on_the_course(students_list, courses[3])}')
print('-' * 80)

lecturers_list = [lecturer1, lecturer2]
print(f"Оценки преподавателей по курсу {courses[2]}")
for lecturer in lecturers_list:
    try:
        print(lecturer.name, lecturer.lectures_grades[courses[2]])
    except:
        1

print(f'Средняя оценка по курсу: '
      f'{avg_grade_for_lection_on_the_course(lecturers_list, courses[4])}')