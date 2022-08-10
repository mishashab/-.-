class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if type(grade) != str:
            return f'\"{grade}\" не является оценкой'
        elif grade < 0 or grade > 10:
            return f'\"{grade}\" не является баллом в пределах от 1 до 10'
        elif isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return f'Студент не посещает курс {grade}, значит он не может ' \
                   f'оценить текущего преподавателя преподавателя'

    def avg_grade(self):
        if len(self.grades) == 0:
            return 'неопределенна'
        else:
            all_grades = []
            for course, course_grades in self.grades.items():
                all_grades += course_grades
            return '%.1f' % sum(all_grades) / len(all_grades)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.avg_grade()}\n'\
               f'Курсы в процессе изучения: ' \
               f'{", ".join([_ for _ in self.courses_in_progress])}\n' \
               f'Завершенные курсы: ' \
               f'{", ".join([_ for _ in self.finished_courses])}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def avg_lecture_grade(self):
        if len(self.lectures_grades) == 0:
            return 'неопределенна'
        else:
            all_grades = []
            for lecture, lecture_grades in self.lectures_grades.items():
                all_grades += lecture_grades
            return '%.1f' % sum(all_grades) / len(all_grades)

    def __str__(self):
        avg_grade = self.avg_lecture_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grade}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return f'Данный преподаватель не может проверить курс {course}'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
