import random
from datetime import datetime
import faker
from random import randint, choice
from datetime import datetime, timedelta

import sqlite3

NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20

subjects = [
        "Mathematics", "Physics", "Chemistry", "Biology", "Geography",
        "History", "World History", "English", "Literature", "French",
        "Computer Science", "Physical Education", "Music", "Art",
        "Economics", "Psychology", "Philosophy", "Drama", "Sociology"
    ]

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


fake_grades_list = [random.randint(1, 12) for _ in range(10)]
# print(fake_grades)

group_prefixes = ["A", "B", "C", "D", "E", "F"]
fake_groups_list = []
for i in group_prefixes:
    for j in range(10):
        fake_groups_list.append(f"{i}-{j}")

def generate_fake_data(number_groups, number_teachers, number_grades, number_students, number_subjects) -> tuple:

    fake_students = []  # тут зберігатимемо компанії
    fake_subjects = []  # тут зберігатимемо співробітників
    fake_grades = []  # тут зберігатимемо посади
    fake_groups = []  # тут зберігатимемо посади
    fake_teachers = []  # тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_subjects):
        temp = random.choice(subjects)
        if temp not in fake_subjects:
            fake_subjects.append(temp)

    # Та number_post набір посад
    for _ in range(number_grades):
        fake_grades.append(random.choice(fake_grades_list))

    for _ in range(number_groups):
        temp = random.choice(fake_groups_list)
        if temp not in fake_groups:
            fake_groups.append(temp)

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
    is_unique = len(fake_subjects) == len(set(fake_subjects))
    print(is_unique)
    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_grades


def prepare_data(students, groups, teachers, subject, grades) -> tuple():
    print(students, groups, teachers, subject, grades, sep='\n')

    for_students = []
    for i in students:
        for_students.append((i,))
    for_groups = []
    for i in groups:
        for_groups.append((i,))
    for_teachers = []
    for i in teachers:
        for_teachers.append((i,))
    for_subject = []
    for i in subject:
        for_subject.append((i,))
    for_grades = []
    for i in grades:
        for_grades.append((random_date, i))
    print(for_grades)
    return for_students, for_groups, for_teachers, for_subject, for_grades



def insert_data_to_db(students, groups, teachers, subjects, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) '''

        sql_to_students = """INSERT INTO students(student_name)
                               VALUES (?)"""

        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим - дані (список кортежів).'''

        cur.executemany(sql_to_students, students)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_groups, groups)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                              VALUES (?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name)
                                      VALUES (?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(date_of, grade)
                                              VALUES (?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    students, groups, teachers, subjects, grades = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_GRADES, NUMBER_STUDENTS, NUMBER_SUBJECTS))
    insert_data_to_db(students, groups, teachers, subjects, grades)
